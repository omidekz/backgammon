from __future__ import annotations
from models import Marble, House
from models.board import Board
from typing import Sequence, Union
from enum import Enum


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
    all_boards = set()
    for dice in dices:
        new_boards = set()
        for board in boards:
            bs = create_boards(board, dice, marble)
            [new_boards.add(b) for b in bs]
        next_dices = dices.copy()
        next_dices.pop(next_dices.index(dice))
        bs = create_all_boards(new_boards, next_dices, marble)
        [all_boards.add(b) for b in bs]
    return all_boards or boards
