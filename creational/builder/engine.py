from __future__ import annotations

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self) -> None:
        pass
    
    @abstractmethod
    def stop(self) -> None:
        pass
    
class PetrolEngine(Engine):
    def start(self) -> None:
        print("PetrolEngine started")
    
    def stop(self) -> None:
        print("PetrolEngine stopped")
        
class DieselEngine(Engine):
    def start(self) -> None:
        print("DieselEngine started")
    
    def stop(self) -> None:
        print("DieselEngine stopped")
        
class ElectricEngine(Engine):
    def start(self) -> None:
        print("ElectricEngine started")
    
    def stop(self) -> None:
        print("ElectricEngine stopped")
        
        
        