from __future__ import annotations

from abc import ABC, abstractmethod
from gps import GPS
from engine import Engine
from trip_computer import TripComputer
from car import Car

class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass
    
    @abstractmethod
    def set_seats(self, seats: int) -> None:
        pass
    
    @abstractmethod
    def set_engine(self, engine: Engine) -> None:
        pass
    
    @abstractmethod
    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        pass
    
    @abstractmethod
    def set_gps(self, gps: GPS) -> None:
        pass
    
class CarBuilder(Builder):     
    def __init__(self) -> None:
        self.data = {}
        
    def reset(self) -> None:
        self.data = {}
        
    def set_seats(self, seats: int) -> None:
        self.data['seats'] = seats
        
    def set_engine(self, engine: Engine) -> None:
        self.data['engine'] = engine
        
    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        self.data['trip_computer'] = trip_computer
        
    def set_gps(self, gps: GPS) -> None:
        self.data['gps'] = gps
        
    def get_result(self) -> Car:
        return Car(engine=self.data['engine'], trip_computer=self.data['trip_computer'], gps=self.data['gps'])