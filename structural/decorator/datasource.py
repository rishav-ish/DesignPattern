from __future__ import annotations
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read(self) -> str:
        pass
    
    @abstractmethod
    def write(self, data: str) -> None:
        pass
    
    
class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self.filename = filename
        
    def read(self) -> str:
        print(f"Reading data from {self.filename}")
        return 'data'
    
    def write(self, data: str) -> None:
        print(f"Writing data to {self.filename}")