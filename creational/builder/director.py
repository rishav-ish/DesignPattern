from __future__ import annotations

from builder import Builder
from engine import DieselEngine, PetrolEngine
from trip_computer import AppleTripComputer, SonnyTripComputer
from gps import Navic, USAGPS

class Director:
    
    def makeSUV(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(4)
        builder.set_engine(DieselEngine())
        builder.set_trip_computer(AppleTripComputer())
        builder.set_gps(Navic())
        
    def makeSportsCar(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(2)
        builder.set_engine(PetrolEngine())
        builder.set_trip_computer(SonnyTripComputer())
        builder.set_gps(USAGPS())