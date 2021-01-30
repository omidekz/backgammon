from __future__ import annotations
from enum import Enum
from typing import Union

from . import House

class Board:

    def __init__(self):
        self.board = dict(
            zip(
                list(range(1, 25)),
                [House.build(house_number=i) for i in range(1, 25)]
            )
        )

    def __getitem__(self, house_number):
        if not 1 <= house_number <= 24:
            raise ValueError("{} is not valid house number".format(house_number))
        return self.board[house_number]
