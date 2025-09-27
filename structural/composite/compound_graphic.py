from __future__ import annotations

from graphic import Graphic

class CompoundGraphic(Graphic):
    def __init__(self):
        self.children: list[Graphic] = []
    
    def draw(self) -> None:
        for child in self.children:
            child.draw()
            
    def add(self, graphic: Graphic) -> None:
        self.children.append(graphic)
        
    def remove(self, graphic: Graphic) -> None:
        self.children.remove(graphic)