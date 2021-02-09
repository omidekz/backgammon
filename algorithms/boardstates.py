from __future__ import annotations
from models import Marble, House
from models.board import Board
from typing import Sequence, Union, Tuple
from enum import Enum

class CustomSet(set):
    def extend(self, itemslist: Sequence):
        for item in itemslist:
            self.add(item)

    @staticmethod
    def extract_and_create(list_in_list: Sequence[Sequence]):
        items = []
        for list in list_in_list:
            if isinstance(list, Sequence):
                list = [list]
            items.extend(*list)
        return CustomSet(iter(items))


def create_boards(board: Board, moves: int, marble: Marble) -> Sequence[Board]:
    boards = set()
    houses_index = board.marble_houses(marble, indexes_seq=True)
    for index in houses_index:
        if board.can_move(index, marble.get_destination(index, moves), marble):
            new_board = board.copy()
            new_board.move_by(index, marble, moves)
            boards.add(new_board)
    return list(boards)

def create_possible_boards_from_boards_by_dice(boards: Sequence[Board], moves: int, marble: Marble) -> Sequence[Board]:
    new_boards = CustomSet()
    for board in boards:
        all_unique_boards_by_current_dice = create_boards(
            board, moves, marble
        )
        new_boards.extend(all_unique_boards_by_current_dice)
    return new_boards

def pop_dice(dices: Sequence[int], index: int) -> Tuple[int, Sequence[int]]:
    tmp_dices = dices.copy()
    return tmp_dices.pop(index), tmp_dices

def create_all_boards(
    boards: Sequence[Board],
    dices: Sequence[int],
    marble: Marble
) -> Sequence[Board]:
    all_boards = CustomSet()
    for dice_index in range(len(dices)):
        dice, rest_of_dices = pop_dice(dices, dice_index)
        all_unique_boards_by_current_dice = create_possible_boards_from_boards_by_dice(
            boards, dice, marble
        )
        all_unique_boards = create_all_boards(
            all_unique_boards_by_current_dice,
            rest_of_dices,
            marble
        )
        all_boards.extend(all_unique_boards)
    return all_boards or boards
