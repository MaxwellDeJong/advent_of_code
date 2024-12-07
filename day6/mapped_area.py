"""Utilities for working with the mapped area."""

from typing import List, Optional

_ORIENTATION_SYMBOLS = ['<', '^', '>', 'v']
_BARRICADE_SYMBOLS = ['#']
_TRAVERSABLE_SYMBOLS = ['.']


class MappedArea:

    def __init__(self, map_file: str) -> None:
        self._map_file = map_file
        self._map_strings: Optional[List[str]] = None
        self._mask: Optional[List[List[Optional[int]]]] = None

    @property
    def map_strings(self) -> List[str]:
        if self._map_strings is None:
            with open(self._map_file, 'r') as f:
                self._map_strings = [line.rstrip() for line in f]
        return self._map_strings

    def _set_map_mask(self) -> List[List[Optional[int]]]:
        def _map_char(char: str) -> Optional[int]:
            if char in _ORIENTATION_SYMBOLS:
                return 1
            if char in _BARRICADE_SYMBOLS:
                return None
            if char in _TRAVERSABLE_SYMBOLS:
                return 0
            raise ValueError(f'Unrecognized character: {char}.')
        return [[_map_char(char) for char in row]
                for row in self.map_strings]

    @property
    def mask(self) -> List[List[Optional[int]]]:
        if self._mask is None:
            self._mask = self._set_map_mask()
        return self._mask

    def position_in_bounds(self, position: List[int]) -> bool:
        n_row = len(self._map_strings)
        n_col = len(self._map_strings[0])
        if position[0] < 0 or position[1] < 0:
            return False
        if position[0] >= n_row or position[1] >= n_col:
            return False
        return True

