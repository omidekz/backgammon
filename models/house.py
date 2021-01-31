from __future__ import annotations
from typing import Sequence, Optional, Dict, Tuple

from . import Marble

class House:
    MARBLES_HOUSE_NUMBERS = (
         1,  6,  8, 12,
        24, 19, 17, 13
    )
    MARBLES_HOUSE_TYPE = dict(zip(MARBLES_HOUSE_NUMBERS, [
        Marble.WHITE, Marble.BLACK, Marble.BLACK, Marble.WHITE,
        Marble.BLACK, Marble.WHITE, Marble.WHITE, Marble.BLACK
    ]))

    def __init__(self, marbles: Sequence[Marble] = []):
        self.marbles = marbles

    @staticmethod
    def create_house_detail(house_number: int) -> Tuple[Marble, int]:
        if house_number not in House.MARBLES_HOUSE_NUMBERS:
            return (None, 0)
        if house_number == 6 or 12 <= house_number <= 13 or house_number == 19:
            return (House.MARBLES_HOUSE_TYPE[house_number], 5)
        elif 8 <= house_number <= 17:
            return (House.MARBLES_HOUSE_TYPE[house_number], 3)
        return (House.MARBLES_HOUSE_TYPE[house_number], 2)
 
    @staticmethod
    def build(house_number: int) -> House:
        host, number = House.create_house_detail(house_number)
        return House([host] * number)

    def marble_counter(self, marble: Marble) -> int:
        return self.marbles.count(marble)

    def marbles_counter(self, marbles: Sequence[Marble] = [Marble.BLACK, Marble.WHITE]) -> Dict[Marble, int]:
        return list(map(self.marble_counter, marbles))

    def host_premitive(self) -> Optional[Marble]:
        blacks, whites = self.marbles_counter()
        return self.premitive_conditions(blacks, whites)

    def premitive_conditions(self, blacks: int = 0, whites: int = 0) -> Optional[Marble]:
        if blacks == 0 and whites == 0:
            return None
        elif whites > 0:
            return Marble.WHITE
        return Marble.BLACK

    def continual_conditions(self, blacks: int = 0, whites: int = 0) -> Optional[Marble]:
        if blacks < 2 and whites < 2:
            return None
        elif whites == 2:
            return Marble.WHITE
        return Marble.BLACK

    def host_continual(self) -> Optional[Marble]:
        blacks, whites = self.marbles_counter()
        return self.continual_conditions(blacks, whites)


    def host(self) -> Optional[Marble]:
        return self.host_continual() or self.host_premitive()

    def is_host(self, marble) -> bool:
        host = self.host()
        return host and host == marble

    def has_host(self):
        return bool(self.host())

    def is_continual_host(self, marble: Marble) -> bool:
        return marble == self.host_continual()

    def is_premitive_host(self, marble: Marble) -> bool:
        return marble == self.host_premitive()

    def can_conqure(self, marble: Marble) -> bool:
        has_continual_host = bool(self.host_continual())
        return not has_continual_host or has_continual_host == marble

    def can_add(self, marble: Marble) -> bool:
        return self.can_conqure(marble)

    def add(self, marble: Marble, number: int = 1) -> bool:
        if not self.can_add(marble):
            return False
        host = self.host()
        if host and host != marble:
            self.marbles.remove(host)
        self.marbles.extend([marble] * number)
        return True

    def pop(self, marble: Marble, number: int = 1) -> bool:
        can_pop = self.host() == marble and self.marbles.count(marble) <= number
        while can_add and number > 0:
            number -= 1
            self.marbles.pop(0)
        return can_pop

    def __str__(self):
        return str(self.marbles)
    
    def __repr__(self):
        return str(self)
