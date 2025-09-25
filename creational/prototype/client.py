from __future__ import annotations

from shape import Shape, Rectangle, Circle, Square
from typing import cast

def main() -> None:
    rectangle = Rectangle(10, 20)
    circle = Circle(10)
    square = Square(10)
    
    rectangle_clone = cast(Rectangle, rectangle.clone())
    circle_clone = cast(Circle, circle.clone())
    square_clone = cast(Square, square.clone())
    
    rectangle_clone.draw()
    circle_clone.draw()
    square_clone.draw()
    
if __name__ == "__main__":
    main()