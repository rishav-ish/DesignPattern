from __future__ import annotations

from abc import ABC, abstractmethod
from prototype import Prototype

class Shape(Prototype):
    @abstractmethod
    def draw(self) -> None:
        pass
    
class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    def draw(self) -> None:
        print(f"Drawing Rectangle with width {self.width} and height {self.height}")
        
    def clone(self) -> Prototype:
        return Rectangle(self.width, self.height)
    
class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius
        
    def draw(self) -> None:
        print(f"Drawing Circle with radius {self.radius}")
        
    def clone(self) -> Prototype:
        return Circle(self.radius)
    
class Square(Shape):
    def __init__(self, side: int):
        self.side = side
        
    def draw(self) -> None:
        print(f"Drawing Square with side {self.side}")
        
    def clone(self) -> Prototype:
        return Square(self.side)
        
        