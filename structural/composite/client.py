from __future__ import annotations

from compound_graphic import CompoundGraphic
from dot import Dot, Circle, Rectangle, Square

class ImageEditor:
    def load(self):
        dot:Graphic = Dot(1, 2)
        circle:Graphic = Circle(3, 4, 5)
        rectangle:Graphic = Rectangle(6, 7, 8, 9)
        square:Graphic = Square(10, 11, 12)
        
        nested_graphic = CompoundGraphic()
        nested_graphic.add(dot)
        nested_graphic.add(circle)
        nested_graphic.add(rectangle)
        nested_graphic.add(square)
        
        compound_graphic = CompoundGraphic()
        compound_graphic.add(dot)
        compound_graphic.add(circle)
        compound_graphic.add(rectangle)
        compound_graphic.add(square)
        compound_graphic.add(nested_graphic)
        
        return compound_graphic
    
    def draw(self):
        compound_graphic:Graphic = self.load()
        compound_graphic.draw()
        
        
if __name__ == "__main__":
    image_editor = ImageEditor()
    image_editor.draw()