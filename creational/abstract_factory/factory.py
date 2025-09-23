from __future__ import annotations

from abc import ABC, abstractmethod
from button import Button
from checkbox import Checkbox
from button import WindowsButton, MacButton
from checkbox import WinCheckbox, MacCheckbox


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    
class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()
    
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()