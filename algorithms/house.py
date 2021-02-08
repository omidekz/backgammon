from models import House, Marble
from typing import Sequence

def concat(string: str, new_line: str, reverse: bool = False) -> str:
    if not reverse:
        return string + new_line
    return new_line + string

def join(seprator: str, joinlist: Sequence, endline: str = '\n', needendline: bool = True, nonevalue: str = '_', to_str: callable = str) -> str:
    return seprator.join([
        to_str(item or nonevalue) for item in joinlist
    ]) + (endline if needendline else '')

def has_host(house: House) -> bool:
    return house.has_host()

def pop(house: House) -> Marble:
    host = house.host()
    return house.pop(host)

def house_number_zfill(n: int = 2):
    def get_house(house: House):
        return str(house.house_number).zfill(n)
    return get_house

def house_collection_to_string(houses: Sequence[House], reverse=False, seprator='  ') -> str:
    string = ''
    while any(map(has_host, houses)):
        line = join(seprator + ' ', map(pop, houses))
        string = concat(string, line, reverse)
    house_numbers = join(seprator, map(house_number_zfill(), houses))
    string = concat(string, house_numbers, not reverse)
    return string
