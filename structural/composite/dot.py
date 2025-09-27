from __future__ import annotations
from graphic import Graphic

class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def draw(self) -> None:
        print(f"Drawing a dot at ({self.x}, {self.y})")
        
        
class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius
        
    def draw(self) -> None:
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")
        
class Rectangle(Dot):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.width = width
        self.height = height
        
    def draw(self) -> None:
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")
        

class Square(Dot):
    def __init__(self, x: int, y: int, side: int):
        super().__init__(x, y)
        self.side = side
        
    def draw(self) -> None:
        print(f"Drawing a square at ({self.x}, {self.y}) with side {self.side}")
        