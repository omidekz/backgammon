from __future__ import annotations
from typing import Union, Sequence, Dict, ItemsView
from pydantic import BaseModel

try:
    from . import House, Dice, Marble
except ImportError:
    from house import House
    from dice import Dice
    from marble import Marble


class Board(BaseModel):
    board: Dict[int, House] = dict(
        zip(
            list(range(1, 25)),
            [House.build(house_number=i) for i in range(1, 25)]
        )
    )
    current_turn_toss: Sequence[int] = Dice.toss()

    @property
    def toss(self):
        return self.current_turn_toss

    def next(self, toss: Sequence[int] = None, number: int = 2) -> None:
        self.current_turn_toss = toss or Dice.toss(number)
        if self.current_turn_toss[0] == self.current_turn_toss[1]:
            self.current_turn_toss *= 2

    def board_items(self) -> ItemsView[int, House]:
        return self.board.items()

    def marble_houses(
        self,
        marble: Marble,
        indexes_seq: bool = False
    ) -> Sequence[Union[int, House]]:
        result_sequence = []
        for house_number, house in self.board_items():
            if house.is_host(marble):
                result_sequence.append(house_number if indexes_seq else house)
        return result_sequence

    def get_house(self, house: Union[House, int]) -> House:
        return self[house]

    def can_move(
        self,
        src: Union[House, int],
        dst: Union[House, int],
        marble: Marble,
        number: int = 1
    ):
        src, dst = self.get_house(src), self.get_house(dst)
        return bool(
            src.is_host(marble)
            and src.marble_counter(marble) >= number
            and marble.has_progressive_movements(int(src), int(dst))
            and dst.can_add(marble)
        )

    def move_marble(
        self,
        src: Union[House, int],
        dst: Union[House, int],
        marble: Marble,
        number: int = 1
    ) -> bool:
        if not self.can_move(src, dst, marble, number):
            return False
        self.get_house(src).pop(marble, number)
        self.get_house(dst).add(marble, number)

    def move_by(
        self,
        src: Union[House, int],
        marble: Marble,
        movements: int,
        number: int = 1
    ) -> bool:
        return self.move_marble(src, src + movements, marble, number)

    def __getitem__(self, house: Union[int, House]) -> House:
        if isinstance(house, House):
            return house
        if not 1 <= house <= 24:
            raise ValueError("{} is not valid house number".format(house))
        return self.board[house]

    def __eq__(self, other: Board):
        return self.board == other.board


if __name__ == '__main__':
    board = Board()

    # houses test    
    black_houses = board.marble_houses(Marble.BLACK, indexes_seq=True)
    white_houses = board.marble_houses(Marble.WHITE, indexes_seq=True)
    assert black_houses == [6, 8, 13, 24]
    assert white_houses == [1, 12, 17, 19]

    assert board.can_move(1, 2, Marble.WHITE) is False
    assert board.can_move(6, 7, Marble.BLACK) is True

    assert board.can_move(1, 2, Marble.BLACK) is False # house 1's host is not BLACK
    assert board.can_move(1, 6, Marble.WHITE) is False # house 6's continual host is not WHITE
    assert board.can_move(1, 6, Marble.BLACK) is False # house 1's host is not BLACK

    # when house's host is None
    assert board.can_move(2, 3, Marble.BLACK) is False
    assert board.can_move(2, 3, Marble.BLACK) is False
