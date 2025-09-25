from __future__ import annotations

from engine import Engine
from trip_computer import TripComputer
from gps import GPS

class Car:
    def __init__(self, *, engine: Engine, trip_computer: TripComputer, gps: GPS):
        self.engine = engine
        self.trip_computer = trip_computer
        self.gps = gps
        
    def start(self) -> None:
        self.engine.start()
        self.trip_computer.get_trip_info()
        self.gps.get_location()
        
    def stop(self) -> None:
        self.engine.stop()
        self.trip_computer.get_trip_info()
        self.gps.get_location()