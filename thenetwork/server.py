import asyncio
import json
import threading
from typing import Dict, Any, Optional

import foomsg
import grpc
import shapefile

from thenetwork.proto import network_pb2_grpc
import logging

from .data import load_most_recent_events, download_latest_data
from .positioning import CampusPositioning, CampusAlignment


SECONDS_PER_REQUEST = 3

logger = logging.getLogger(__name__)


class TheNetworkServer(network_pb2_grpc.TheNetworkServicer):
    _positioning: CampusPositioning
    _move_events: Dict[int, Any]
    _step: int
    _step_lock: asyncio.Lock
    _building: Optional[str]

    def __init__(self, positioning, move_events):
        self._positioning = positioning
        self._move_events = move_events
        # self._step = int(((11 * 3600) + (30 * 60)) / SECONDS_PER_REQUEST)
        self._step = ((11 * 3600) + (30 * 60)) // SECONDS_PER_REQUEST
        self._step_lock = asyncio.Lock()
        self._building = None

    @property
    def step(self):
        return self._step

    def set_building(self, building):
        self._building = building

    def set_room_precision(self, precise):
        self._positioning.set_room_precision(precise)

    async def set_step(self, step):
        # async with self._step_lock:
        self._step = step

    async def GetNetworkMovements(self, request, context):
        try:
            # print("Serving random movements")
            second_start = self._step
            second_range = range(second_start, second_start + SECONDS_PER_REQUEST)
            movements = []
            for second in second_range:
                if second not in self._move_events:
                    continue
                movements.extend(self._move_events[second])
            # print(list(second_range))
            # print("\r"*100)
            # print(
            #     f"timestamp: {str(int(second_start / 3600)).rjust(2, '0')}:{str(int((second_start / 60) % 60)).rjust(2, '0')}:{str(second_start % 60).rjust(2, '0')}",
            #     f"new movements: {len(movements)}", end=""
            # )
            # async with self._step_lock:
            self._step += SECONDS_PER_REQUEST
            if self._step > 60 * 60 * 24 - 1:
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                print("Resetting step")
                self._step = 0
            # print(len(movements))
            mapped_movements = self._positioning.mapped_movements(
                movements, building=self._building
            )
            print(len(mapped_movements.movements))
            return mapped_movements
            # return random_movements(alignment)
        except Exception:
            logger.exception("Exception while serving room movements")
            raise


server: Optional[TheNetworkServer] = None


def message_handler(message):
    message_type = message["type"]
    print(message)
    if message_type == "building":
        building = message["building"]
        if building == "all" or building == "":
            building = None
        server.set_building(building)
    elif message_type == "room_precision":
        precision = message["precise"]
        server.set_room_precision(precision)
    elif message_type == "step":
        step = message["step"]
        asyncio.get_event_loop().create_task(server.set_step(int(step)))


async def messaging_update_loop(messaging):
    while True:
        await messaging.send_message({"type": "step", "step": server.step})
        await asyncio.sleep(0.1)


async def serve():
    global server
    event_loop = asyncio.get_running_loop()

    grpc_server = grpc.aio.server()

    alignment = CampusAlignment.parse_file("alignment.json")
    bldg_bboxes = json.load(open("bboxes.json", "r"))
    shape_data = shapefile.Reader("floorplans/Floorplans")
    positioning = CampusPositioning(alignment, bldg_bboxes, shape_data)

    server = TheNetworkServer(positioning, load_most_recent_events())
    network_pb2_grpc.add_TheNetworkServicer_to_server(server, grpc_server)
    listen_addr = "[::]:50051"
    grpc_server.add_insecure_port(listen_addr)

    logger.info(f"Starting server on {listen_addr}")

    await grpc_server.start()

    messaging = foomsg.Messaging()
    messaging.add_message_listener(message_handler)
    event_loop.create_task(messaging_update_loop(messaging))
    # messaging_loop = event_loop.create_task(messaging.start())
    await messaging.start()
    # event_loop.(messaging_loop)

    logger.info("Starting Footron messaging")
    # TODO: Make sure to start other loops we want running before starting this—this
    #  includes messaging.

    # await server.wait_for_termination()

    # def shutdown(signal):

    # event_loop.add_signal_handler(signal.SIGTERM,
    #                         functools.partial(asyncio.ensure_future,
    #                                           shutdown(signal.SIGTERM)))

    # try:
    # await server.wait_for_termination()
    # except KeyboardInterrupt:
    #     print("AAAAAH")
    #     event_loop.stop()
    #     raise


def download_most_recent_events_thread() -> None:
    download_latest_data()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="The Network Server")
    parser.add_argument("--download-only", action="store_true")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    if not args.download_only:
        asyncio.get_event_loop().run_until_complete(serve())
        # In another thread, we're going to pull data from yesterday if we haven't
        # already.
        # Otherwise we're just going to hang tight.
        threading.Thread(target=download_most_recent_events_thread, daemon=True).start()
    else:
        download_latest_data()
