from __future__ import annotations

from device import Device

class Remote:
    def __init__(self, device: Device):
        self.device = device
        
    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()
            
    def volume_up(self) -> None:
        self.device.set_volume(self.device.get_volume() + 10)
        
    def volume_down(self) -> None:
        self.device.set_volume(self.device.get_volume() - 10)
        
    def channel_up(self) -> None:
        self.device.set_channel(self.device.get_channel() + 1)
        
    def channel_down(self) -> None:
        self.device.set_channel(self.device.get_channel() - 1)
        
        
class AdvancedRemote(Remote):
    def mute(self) -> None:
        self.device.set_volume(0)