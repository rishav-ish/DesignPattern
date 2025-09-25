from __future__ import annotations

from builder import CarBuilder
from director import Director

def main() -> None:
    director = Director()
    car_builder = CarBuilder()
    director.makeSUV(car_builder)
    car = car_builder.get_result()
    car.start()
    car.stop()
    
if __name__ == "__main__":
    main()