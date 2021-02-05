import random
from typing import Sequence, ClassVar
from pydantic import BaseModel


class Dice(BaseModel):
    MIN_NUMBER: ClassVar[int] = 1
    MAX_NUMBER: ClassVar[int] = 6

    @staticmethod
    def toss(number: int = 2) -> Sequence[int]:
        tosses = []
        for _ in range(number):
            random_number = Dice.random_number()
            tosses.append(random_number)
        return tosses
    
    @staticmethod
    def random_number():
        _min = Dice.MIN_NUMBER
        _max = Dice.MAX_NUMBER
        return random.randint(_min, _max)
