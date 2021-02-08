from __future__ import annotations
from typing import Sequence
from enum import Enum

class Section:
    ABOVE = 'above'
    DOWN  = 'down'

    class Detail:
        ABOVE_SECTION_START = 13
        ABOVE_SECTION_END = 24 + 1
        DOWN_SECTION_START = 12
        DOWN_SECTION_END = 1 - 1

        @staticmethod
        def get_range(section: Section) -> Sequence[int, int]:
            SD_AS = Section.Detail.ABOVE_SECTION_START
            SD_AE = Section.Detail.ABOVE_SECTION_END
            SD_DS = Section.Detail.DOWN_SECTION_START
            SD_DE = Section.Detail.DOWN_SECTION_END
            is_for_above = section == Section.ABOVE
            start = SD_AS if is_for_above else SD_DS
            end   = SD_AE if is_for_above else SD_DE
            return start, end

def get_board_section(section: Section, board) -> Sequence[House]:
    start, end = Section.Detail.get_range(section)
    return [board[house_number] for house_number in range(start, end)]
