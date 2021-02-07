from models import Board, Marble
from typing import Sequence

def create_boards(board: Board, moves: int, marble: Marble) -> Sequence[Board]:
    boards = list()
    houses_index = board.marble_houses(marble, indexes_seq=True)
    for index in houses_index:
        if board.can_move(index, marble.get_destination(index, moves), marble):
            new_board = board.copy()
            new_board.move_by(index, marble, moves)
            boards.append(
                new_board
            )
    return boards
