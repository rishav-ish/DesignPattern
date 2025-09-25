from __future__ import annotations

from roundhole import RoundHole
from roundpeg import RoundPeg
from squarepeg import SquarePeg
from squarepeg_adapter import SquarePegAdapter

def main() -> None:
    hole = RoundHole(5)
    peg = RoundPeg(5)
    hole.fits(peg)
    
    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    
    # hole.fits(small_sqpeg) This will not work
    
    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    
    hole.fits(small_sqpeg_adapter)
    hole.fits(large_sqpeg_adapter)
    
if __name__ == "__main__":
    main()