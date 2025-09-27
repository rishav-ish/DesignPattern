from __future__ import annotations
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass
    
    @abstractmethod
    def enable(self) -> None:
        pass
    
    @abstractmethod
    def disable(self) -> None:
        pass
    
    @abstractmethod
    def get_volume(self) -> int:
        pass
    
    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass
    
    @abstractmethod
    def get_channel(self) -> int:
        pass
    
    @abstractmethod
    def set_channel(self, channel: int) -> None:
        pass
    
class Radio(Device):
    def __init__(self):
        self.volume = 0
        self.channel = 0
    
    def is_enabled(self) -> bool:
        return True
    
    def enable(self) -> None:
        print("Radio is enabled")
    
    def disable(self) -> None:
        print("Radio is disabled")
    
    def get_volume(self) -> int:
        print(f"Radio volume: {self.volume}")
        return self.volume
    
    def set_volume(self, volume: int) -> None:
        print(f"Radio volume set to {volume}")
        self.volume = volume
        
    def get_channel(self) -> int:
        print(f"Channel: {self.channel}")
        return self.channel
    
    def set_channel(self, channel: int) -> None:
        print(f"Channel set to {channel}")
        self.channel = channel
        
class TV(Device):
    def __init__(self):
        self.volume = 0
        self.channel = 0
        self.is_on = False
        
    def is_enabled(self) -> bool:
        return self.is_on
    
    def enable(self) -> None:
        self.is_on = True
        print("TV is enabled")
    
    def disable(self) -> None:
        self.is_on = False
        print("TV is disabled")
    
    def get_volume(self) -> int:
        print(f"TV volume: {self.volume}")
        return self.volume
    
    def set_volume(self, volume: int) -> None:
        print(f"TV volume set to {volume}")
        self.volume = volume
    
    def get_channel(self) -> int:
        print(f"Channel: {self.channel}")
        return self.channel
    
    def set_channel(self, channel: int) -> None:
        print(f"Channel set to {channel}")
        self.channel = channel