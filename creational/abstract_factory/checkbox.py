from __future__ import annotations

from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    
class WinCheckbox(Checkbox):
    def render(self) -> None:
        print("Windows Checkbox Rendered")
        
    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()
    
class MacCheckbox(Checkbox):
    def render(self) -> None:
        print("Mac Checkbox Rendered")
        
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()