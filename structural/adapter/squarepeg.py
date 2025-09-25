from __future__ import annotations

from roundpeg import RoundPeg

class SquarePeg:
    def __init__(self, width: int):
        self.width = width
        
    def get_width(self) -> int:
        return self.width