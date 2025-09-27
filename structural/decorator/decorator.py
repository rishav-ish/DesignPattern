from __future__ import annotations
from abc import ABC, abstractmethod
from datasource import DataSource

class DataSourceDecorator(DataSource):
    def __init__(self, datasource: DataSource):
        self.datasource = datasource
        
    @abstractmethod
    def read(self) -> str:
        pass
    
    @abstractmethod
    def write(self, data: str) -> None:
        pass
    
class EncryptionDecorator(DataSourceDecorator):
    def read(self) -> str:
        print(f"Reading data from with encryption")
        return 'encrypted data'
    
    def write(self, data: str) -> None:
        print(f"Writing data to with encryption")
        
class CompressionDecorator(DataSourceDecorator):
    def read(self) -> str:
        print(f"Reading data from with compression")
        return 'compressed data'
    
    def write(self, data: str) -> None:
        print(f"Writing data to with compression")
        