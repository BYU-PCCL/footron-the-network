import json
from collections import defaultdict
from datetime import datetime, date, timedelta
from typing import Set, Dict, DefaultDict, List, Tuple
from pathlib import Path

from humiolib import HumioClient, QueryJob
from pydantic import BaseModel
from tqdm import tqdm

from . import logger

WIFI_QUERY_STRING = """
splitString(Roles, by=", ", as=Roles) | 
Roles[0] =~ in(values=["BYU NetID", "BYU Guest 1 Day"]) | 
drop(Message) | 
regex(regex="^P-(?P<Building>[^-]*)-(?P<Room>[^-]*)-.*", field=APLocation)
""".replace(
    "\n", ""
)

HOUR_SECONDS = 60 * 60
THRESHOLD_SECONDS = HOUR_SECONDS * 8

EVENTS_PATH = Path("events")
SAVED_EVENTS_LIMIT = 100


class HumioConfig(BaseModel):
    url: str
    token: str
    repository: str


class AuthEvent(BaseModel):
    event_id: str
    room: str
    building: str
    net_id: str
    mac: str
    timestamp: datetime

    @property
    def room_id(self):
        return f"{self.building} {self.room}"

    @classmethod
    def from_humio_event(cls, event):
        """Note that this assumes "Room" and "Building" fields have been captured
        with regex remotely"""
        return AuthEvent(
            event_id=event["@id"],
            room=event["Room"],
            building=event["Building"],
            net_id=event["Username"],
            mac=event["MACAddress"],
            # timestamp=datetime.fromtimestamp(event["@timestamp"] / 1000),
            timestamp=datetime.strptime(
                "-".join(event["ActualEventTime"].split("-")[:-1]), "%Y-%m-%d %H:%M:%S"
            ),
        )


class BatchDataPuller:
    _event_ids: Set[str]
    _net_id_events: Dict[str, AuthEvent]
    _room_net_ids: DefaultDict[str, Set]
    _move_events: Dict[int, List]
    _stream: QueryJob
    _client: HumioClient

    def __init__(self, client: HumioClient):
        self._event_ids = set()
        self._net_id_events = {}
        self._room_net_ids = defaultdict(set)
        self._move_events = defaultdict(list)
        self._client = client
        self._stream = None

    @property
    def connection_count(self):
        return len(self._net_id_events)

    @property
    def room_net_ids(self):
        return self._room_net_ids

    @property
    def move_events(self):
        return self._move_events

    def poll(self, start, end=None):
        humio_events = self._client.streaming_query(
            WIFI_QUERY_STRING, is_live=False, start=start, end=end
        )

        new_event_count = 0
        remaining_net_ids = set(self._net_id_events.keys())
        events = []

        for event in tqdm(humio_events, desc="Pulling events"):
            event_id = event["@id"]
            if event_id in self._event_ids:
                continue
            self._event_ids.add(event_id)
            new_event_count += 1
            events.append(AuthEvent.from_humio_event(event))

        events.sort(key=lambda e: e.timestamp)

        # TODO: Actually label these in some way that makes any sense
        for event in tqdm(events, desc="Adding sorted events"):
            if event.net_id in self._net_id_events:
                last_event = self._net_id_events[event.net_id]
                last_room_id = last_event.room_id
                last_net_id = last_event.net_id

                # minute = int((datetime.now() - datetime.combine(date.today(), datetime.min.time())).seconds / 60)
                # print(datetime.combine(dt, datetime.min.time()))
                # move_events.append((minute, last_room_id, event.room_id))
                # print(f"MOVED FROM {last_room_id} TO {event.room_id}")
                if event.room_id != last_room_id:
                    self._room_net_ids[last_room_id].remove(last_net_id)
                    self._move_events[
                        event.timestamp.hour * 3600
                        + event.timestamp.minute * 60
                        + event.timestamp.second
                    ].append((last_room_id, event.room_id))

            self._net_id_events[event.net_id] = event
            self._room_net_ids[event.room_id].add(event.net_id)
            if event.net_id in remaining_net_ids:
                remaining_net_ids.remove(event.net_id)

        return new_event_count


def download_latest_data() -> None:
    yesterday_midnight = datetime.combine(
        date.today() - timedelta(days=1), datetime.min.time()
    )

    event_path = EVENTS_PATH / f'{yesterday_midnight.strftime("%Y.%m.%d")}-events.json'

    if event_path.exists():
        logger.log(f"Skipping download of {event_path}")
        return

    midnight = datetime.combine(date.today(), datetime.min.time())
    config = HumioConfig.parse_file("humio-config.json")

    client = HumioClient(
        base_url=config.url, repository=config.repository, user_token=config.token
    )
    puller = BatchDataPuller(client)

    puller.poll(
        int(yesterday_midnight.timestamp() * 1000), int(midnight.timestamp() * 1000)
    )
    move_events = puller.move_events

    if not EVENTS_PATH.exists():
        EVENTS_PATH.mkdir()
    with open(event_path, "w") as f:
        json.dump(move_events, f)


def load_most_recent_events() -> Dict[int, List[Tuple[str, str]]]:
    # List most recent events and sort them by descending timestamp
    # Note that we'll always ship with one of these pre-downloaded because it's totally
    # unclear what we do in the alternative
    descending_events_files = sorted(EVENTS_PATH.glob("*-events.json"), reverse=True)
    # Delete all events files older than the limit
    for event_file in descending_events_files[SAVED_EVENTS_LIMIT:]:
        event_file.unlink()
    # Load first event file
    with open(descending_events_files[0], "r") as f:
        return {int(k): v for k, v in json.load(f).items()}
