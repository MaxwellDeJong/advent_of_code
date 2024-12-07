"""Utilities for initializing guard information."""

from typing import List, Optional

import heading as heading_module

_ORIENTATION_SYMBOLS = ['<', '^', '>', 'v']


class Guard:

    def __init__(self, map_strings: List[str]) -> None:
        self._map_strings = map_strings
        self._position: Optional[List[int]] = None
        self._heading: Optional[heading_module.Heading] = None

    def _initialize_guard(self) -> None:
        for row_idx, row in enumerate(self._map_strings):
            for symbol in _ORIENTATION_SYMBOLS:
                if symbol in row:
                    self._position = [row_idx, row.index(symbol)]
                    self._heading = heading_module.Heading(symbol)
                    return

    @property
    def position(self) -> List[int]:
        if self._position is None:
            self._initialize_guard()
            assert self._position is not None, (
                'Guard position failed to initialize')
        return self._position

    @position.setter
    def position(self, new_position: List[int]) -> None:
        self._position = [p for p in new_position]

    @property
    def heading(self) -> heading_module.Heading:
        if self._heading is None:
            self._initialize_guard()
            assert self.heading is not None, (
                'Guard heading failed to initialize')
        return self._heading

    @heading.setter
    def heading(self, new_heading: heading_module.Heading) -> None:
        self._heading = new_heading

    def turn(self) -> None:
        self._heading.turn()

    def get_next_position(self) -> List[int]:
        position_change = self._heading.get_position_change()
        return [self.position[0] + position_change[0],
                self.position[1] + position_change[1]]

