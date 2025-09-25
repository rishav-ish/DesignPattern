from __future__ import annotations


class RoundPeg:
    def __init__(self, radius: int):
        self.radius = radius
        
    def get_radius(self) -> int:
        return self.radius
    
    def __str__(self) -> str:
        return f"RoundPeg(radius={self.radius})"