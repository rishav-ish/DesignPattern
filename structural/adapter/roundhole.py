from __future__ import annotations

from roundpeg import RoundPeg

class RoundHole:
    def __init__(self, radius: int):
        self.radius = radius
        
    def get_radius(self) -> int:
        return self.radius
    
    def fits(self, peg: RoundPeg) -> bool:
        res =  self.get_radius() >= peg.get_radius()
        print(f"RoundHole fits {peg} -> {res}")
        return res