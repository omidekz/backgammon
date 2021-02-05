try: 
    from . import Board, Dice, User, House, Marble
except ImportError as e:
    from user import User
    from board import Board
    from dice import Dice
    from house import House
    from marble import Marble

from pydantic import BaseModel
from typing import Sequence, Union, List


class Game(BaseModel):

    white_player:       User    = User(name='white player')
    black_player:       User    = User(name='black player')
    board:              Board   = Board()
    black_turn:         bool    = True

    def next(self, dice: Sequence[int] = (), number: int = 2) -> None:
        self.board.next(dice, number)
        self.black_turn = not self.black_turn

    @property
    def is_black_turn(self):
        return self.black_turn

    def current_player(self):
        return self.black_player if self.black_turn else self.white_player

    def player_marble(self, player: User = None) -> Marble:
        player = player or self.current_player()
        return Marble.WHITE if self.white_player == player else Marble.BLACK

    def marble_houses(self, player: User = None, index: bool = True) -> Sequence[Union[int, House]]:
        player = player or self.current_player()
        marble = self.player_marble(player)
        return self.board.marble_houses(marble, index)

    def get_all_movements(self, marble: Marble, dices: Sequence[int], boards: Sequence[Board]) -> Sequence[Board]:
        pass

    def player_movements(self, player: User = None) -> Sequence[Board]:
        player = player or self.current_player()
        marbles_index = self.marble_houses(player)
        marble = self.player_marble(player)
        return self.get_all_movements(
            marble,
            marbles_index,
            [self.board.copy()]
        )
