"""Utilities for handling orientation associated with entities."""

import enum
from typing import Dict, List, Tuple


class Direction(enum.Enum):
    left = 0
    up = 1
    right = 2
    down = 3


def get_position_change(direction: Direction) -> Tuple[int]:
    position_change_dict = {
        Direction.left: (0, -1),
        Direction.up: (-1, 0),
        Direction.right: (0, 1),
        Direction.down: (1, 0)}
    return position_change_dict[direction]


class Heading:

    def __init__(self, initial_symbol: str) -> None:
        self._direction = self._set_initial_direction(initial_symbol)

    @property
    def _ordered_symbols(self) -> List[str]:
        return ['<', '^', '>', 'v']

    @property
    def _symbol_to_direction_dict(self) -> Dict[str, Direction]:
        ordered_symbols = ['<', '^', '>', 'v']
        return {symbol: direction for symbol, direction in zip(
            ordered_symbols, Direction)}

    def _set_initial_direction(self, initial_symbol: str) -> Direction:
        if initial_symbol in self._symbol_to_direction_dict:
            return self._symbol_to_direction_dict[initial_symbol]
        raise ValueError(f'Invalid symbol {initial_symbol}.')

    @property
    def direction(self) -> Direction:
        return self._direction

    def turn(self) -> None:
        direction_idx = list(Direction).index(self._direction)
        new_direction_idx = (direction_idx + 1) % len(Direction)
        self._direction = Direction(new_direction_idx)

    def get_position_change(self) -> Tuple[int]:
        return get_position_change(self._direction)

