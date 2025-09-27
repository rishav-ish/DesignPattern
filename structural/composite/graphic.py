from __future__ import annotations
from abc import ABC, abstractmethod

class Graphic(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass