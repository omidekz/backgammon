try: 
    from . import Board, Dice, User, House, Marble
except:
    from user import User
    from board import Board
    from dice import Dice
    from house import House
    from marble import Marble

from pydantic import BaseModel
from typing import Sequence, Union

class Game(BaseModel):

    wplayer: User = User(name='white player')
    bplayer: User = User(name='black player')
    board: Board  = Board()
    black_turn: bool = True 

    def next(self, toss: Sequence[int] = [], number: int = 2) -> None:
        self.board.next(toss, number)
        self.black_turn = not self.black_turn

    @property
    def is_black_turn(self):
        return self.black_turn

    def current_player(self):
        return self.bplayer if self.black_turn else self.wplayer

    def player_marble(self, player: User) -> Marble:
        return Marble.WHITE if self.wplayer == player else Marble.BLACK

    def marble_houses(self, player: User = self.current_player, index: bool = True) -> Sequence[Union[int, House]]:
        marble = self.player_marble(player)
        return self.board.marble_houses(marble, index)

    def player_movements(self, player: User = self.current_player) -> Sequence[Board]:
        marbles_index = self.marbles_houses_index(player)
        marble = self.player_marble(player)
        movements = self.board.marble_houses(marble, indexs_seq=True)
        

