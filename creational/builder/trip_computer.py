from __future__ import annotations

from abc import ABC, abstractmethod

class TripComputer(ABC):
    @abstractmethod
    def get_trip_info(self) -> None:
        pass
    
    
class SonnyTripComputer(TripComputer):
    def get_trip_info(self) -> None:
        print("SonnyTripComputer trip info")
        
class AppleTripComputer(TripComputer):
    def get_trip_info(self) -> None:
        print("AppleTripComputer trip info")
        
        