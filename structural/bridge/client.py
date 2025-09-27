from __future__ import annotations

from remote import Remote, AdvancedRemote
from device import Radio, TV, Device

def main() -> None:
    radio = Radio()
    tv = TV()
    
    remote = Remote(radio)
    remote.toggle_power()
    remote.volume_up()
    remote.channel_up()
    remote.toggle_power()
    
    advanced_remote = AdvancedRemote(tv)
    advanced_remote.toggle_power()
    advanced_remote.volume_up()
    advanced_remote.channel_up()
    advanced_remote.mute()
    advanced_remote.toggle_power()
    
if __name__ == "__main__":
    main()