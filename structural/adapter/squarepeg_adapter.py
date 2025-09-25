from __future__ import annotations

import math

from squarepeg import SquarePeg
from roundhole import RoundHole
from roundpeg import RoundPeg

class SquarePegAdapter(RoundPeg):
    def __init__(self, squarepeg: SquarePeg):
        self.squarepeg = squarepeg
        
    def get_radius(self) -> int:
        return self.squarepeg.get_width() * math.sqrt(2) / 2
    
    def __str__(self) -> str:
        return f"SquarePeg(width={self.squarepeg.get_width()})"