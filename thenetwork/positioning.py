from collections import defaultdict
from typing import Tuple, Dict, List, Any

from thenetwork.proto import network_pb2

import numpy as np
import shapefile
from pydantic import BaseModel


class CampusBbox(BaseModel):
    ne: Tuple[float, float, float]
    sw: Tuple[float, float, float]


class BuildingAlignment(BaseModel):
    offset: Tuple[float, float, float]
    height: float


class CampusAlignment(BaseModel):
    bbox: CampusBbox
    buildings: Dict[str, BuildingAlignment]


class CampusPositioning:
    _alignment: CampusAlignment
    _building_bboxes: Dict[str, Tuple[float, float, float, float, int]]
    _records: shapefile.ShapeRecords
    _global_bbox: Tuple[float, float, float, float]
    _buildings: set
    # TODO: Actually figure out typing for this
    _rooms: Dict[str, Any]
    _room_precision: bool
    _buildings_heights: Dict[str, int]

    def __init__(
        self,
        alignment: CampusAlignment,
        building_bboxes: Dict[str, Tuple[float, float, float, float, int]],
        shape_data: shapefile.Reader,
    ):
        self._alignment = alignment
        self._building_bboxes = building_bboxes
        self._records = shape_data.shapeRecords()
        self._global_bbox = shape_data.bbox
        self._buildings = set()
        self._buildings_heights = defaultdict(lambda: 0)
        self._build_building_data()
        self._rooms = {}
        self._room_precision = False
        self._calculate_mapped_room_points()

    def _build_building_data(self):
        for record in list(self._records):
            bldg_name = record.record.BLDG_SHORT
            self._buildings.add(bldg_name)

            level = record.record.BLDG_LEVEL
            if level > self._buildings_heights[bldg_name]:
                self._buildings_heights[bldg_name] = level

    def set_room_precision(self, precise):
        self._room_precision = precise
        self._calculate_mapped_room_points()

    def _calculate_mapped_room_points(self):
        for i, record in enumerate(self._records):
            # This centers the data on the building instead of the room
            # the code below will center on the exact room
            if self._room_precision:
                self._rooms[record.record.ROOM_ID] = (
                    *(
                        np.average(np.array(record.shape.points), axis=0)
                        - np.array([self._global_bbox[0], self._global_bbox[1]])
                    )
                    / np.array(
                        [
                            self._global_bbox[2] - self._global_bbox[0],
                            self._global_bbox[3] - self._global_bbox[1],
                        ]
                    ),
                    record.record.BLDG_LEVEL,
                    record.record.BLDG_SHORT,
                )
            else:
                bldg_bbox = self._building_bboxes[record.record.BLDG_SHORT]
                x = (bldg_bbox[0] + bldg_bbox[2]) / 2
                y = (bldg_bbox[1] + bldg_bbox[3]) / 2
                self._rooms[record.record.ROOM_ID] = (
                    *(
                        np.array([x, y])
                        - np.array([self._global_bbox[0], self._global_bbox[1]])
                    )
                    / np.array(
                        [
                            self._global_bbox[2] - self._global_bbox[0],
                            self._global_bbox[3] - self._global_bbox[1],
                        ]
                    ),
                    record.record.BLDG_LEVEL,
                    record.record.BLDG_SHORT,
                )

    def _aligned_room_data(self, mapped_room_points):
        rooms = {}
        # delta = 1000 * np.sin(time.time() / 2.0)
        ue_bbox = np.array([self._alignment.bbox.ne, self._alignment.bbox.sw])

        horizontal_range = np.subtract(*ue_bbox[:, :2])
        horizontal_base = ue_bbox[1, :2]

        z_range = np.subtract(*ue_bbox[::1, -1])
        # z_base = ue_bbox[1, -1]

        for room, position in mapped_room_points.items():
            x, y, level, building = position
            ax, ay = (np.array([x, y]) * horizontal_range) + horizontal_base

            alignment_building = self._alignment.buildings[building]

            # These are confusingly named. Different coordinate systems.
            z_offset = alignment_building.offset[-1]
            z_height = alignment_building.height

            # az = (
            #     (((level / bldg_heights[building]) * z_height) + z_offset) * z_range
            # ) + z_base

            # Testing this for now just to get things above buildings
            az = ((z_height + z_offset) * z_range) - 250

            rooms[room] = (
                ax,
                ay,
                az,
                # (level * (11000 / 12)) + 8000 + delta,
            )
        return rooms

    @staticmethod
    def tuple_to_pb_position(position: Tuple[float, float, float]):
        x, y, z = position
        return network_pb2.Position(x=x, y=y, z=z)

    def mapped_movements(
        self,
        room_movements: List[Tuple[str, str]],
        *,
        building: str = None,
    ):
        rooms = self._aligned_room_data(self._rooms)
        # print("rooms", len(self._rooms))
        number_of_data_points_dropped = 0
        movements = []
        for movement in room_movements:
            start, end = movement
            bldg_start = start.split(" ")[0]
            bldg_end = end.split(" ")[0]
            if start not in rooms or end not in rooms:
                number_of_data_points_dropped += 1
                continue
            if bldg_start == bldg_end:
                continue
            if building and bldg_start != building and bldg_end != building:
                continue
            room_start = list(rooms[start])
            room_end = list(rooms[end])
            if not self._room_precision:
                jitter = np.random.randn(1, 2) * 200
                room_start[0] += jitter[0, 0]
                room_start[1] += jitter[0, 1]
                room_end[0] += jitter[0, 0]
                room_end[1] += jitter[0, 1]
            movements.append((room_start, room_end))
        # print(f"Movements dropped: {number_of_data_points_dropped}")
        return network_pb2.NetworkMovements(
            movements=[
                network_pb2.NetworkMovement(
                    start=self.tuple_to_pb_position(a), end=self.tuple_to_pb_position(b)
                )
                for a, b in movements
            ]
        )
