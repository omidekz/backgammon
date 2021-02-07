from __future__ import annotations
from enum import Enum
from pydantic import BaseModel

class Marble(str, Enum):
    BLACK = 'b'
    WHITE = 'w'

    def has_progressive_movements(self, src, dst) -> bool:
        distance = dst - src
        return self == Marble.BLACK and distance > 0 \
                or self == Marble.WHITE and distance < 0

    def __bool__(self):
        return True

    def get_destination(self, src: int, moves: int) -> int:
        if self == Marble.BLACK:
            moves *= -1
        return src + moves

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)
