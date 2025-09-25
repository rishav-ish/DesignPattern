from __future__ import annotations

from abc import ABC, abstractmethod

class GPS(ABC):
    @abstractmethod
    def get_location(self) -> None:
        pass
    
    
class USAGPS(GPS):
    def get_location(self) -> None:
        print("USAGPS location")
        
class Navic(GPS):
    def get_location(self) -> None:
        print("Navic location")
        
        