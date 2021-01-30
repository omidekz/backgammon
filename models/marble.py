from __future__ import annotations
from enum import Enum

class Marble(str, Enum):
    BLACK = 'b'
    WHITE = 'w'

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)
