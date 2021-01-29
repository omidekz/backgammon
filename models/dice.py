import random
from typing import Sequence

class Dice:
    MIN_NUMBER = 1
    MAX_NUMBER = 6

    @staticmethod
    def toss(number: int = 1) -> Sequence[int]:
        tosses = []
        for _ in range(number):
            random_number = Dice.random_number()
            tosses.append(random_number)
        return tosses
    
    @staticmethod
    def random_number():
        _min = Dice.MIN_NUMBER
        _max = Dice.MAX_NUMBER + 1
        return random.randint(_min, _max)
