from models import Board, Marble
from typing import Sequence

def create_boards(board: Board, dices: Sequence[int], marbl: Marble) -> Sequence[Board]:
    boards = list()
    for dice in dices:
        houses_index = board.marble_houses(marbl, indexes_seq=True)
        for index in houses_index:
            if board.can_move(index, marbl.get_destination(index, dice), marbl):
                board.move_by(index, marbl, dice)
                boards.append(
                    board.co
                )
    return boards
