from __future__ import annotations

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass 
    
    @abstractmethod
    def create_button(self) -> Button:
        pass

class WindowsButton(Button):
    def render(self) -> None:
        print("Windows Button Rendered")
    
    def create_button(self) -> Button:
        return WindowsButton()

class MacButton(Button):
    def render(self) -> None:
        print("Mac Button Rendered")
        
    def create_button(self) -> Button:
        return MacButton()