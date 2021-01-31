from __future__ import annotations
from enum import Enum
from typing import Union, Sequence

from . import House, Dice, Marble

class Board:

    def __init__(self):
        self.board = dict(
            zip(
                list(range(1, 25)),
                [House.build(house_number=i) for i in range(1, 25)]
            )
        )
        self.current_turn_toss = Dice.toss(2)

    def next(self, toss: Sequence[int]) -> None:
        self.current_turn_toss = toss or Dice.toss()

    def marble_house(self, marble: Marble, indexs_seq=False) -> Sequence[Union[int, House]]:
        result_sequence = []
        for house_number, house in self.board.items():
            if house.host() == marble:
                result_sequence.append(house_number if indexs_seq else house)
        return result_sequence

    def __getitem__(self, house_number: int) -> House:
        if not 1 <= house_number <= 24:
            raise ValueError("{} is not valid house number".format(house_number))
        return self.board[house_number]
