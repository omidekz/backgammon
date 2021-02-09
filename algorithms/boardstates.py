from __future__ import annotations
from models import Marble, House
from models.board import Board
from typing import Sequence, Union
from enum import Enum

class CustomSet(set):
    def extend(self, itemslist: Sequence):
        for item in itemslist:
            self.add(item)


def create_boards(board: Board, moves: int, marble: Marble) -> Sequence[Board]:
    boards = set()
    houses_index = board.marble_houses(marble, indexes_seq=True)
    for index in houses_index:
        if board.can_move(index, marble.get_destination(index, moves), marble):
            new_board = board.copy()
            new_board.move_by(index, marble, moves)
            boards.add(new_board)
    return boards

def create_all_boards(
    boards: Sequence[Board],
    dices: Sequence[int],
    marble: Marble
) -> Sequence[Board]:
    all_boards = CustomSet()
    for dice in dices:
        new_boards = CustomSet()
        for board in boards:
            new_boards.extend(create_boards(board, dice, marble))
        next_dices = dices.copy()
        next_dices.pop(next_dices.index(dice))
        all_boards.extend(create_all_boards(new_boards, next_dices, marble))
    return all_boards or boards
