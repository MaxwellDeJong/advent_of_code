"""Solution for day 6 part 1."""

from typing import List, Optional

import guard
import mapped_area

_INITIAL_MAP_FILE = 'initial_map.txt'


class Game:

    def __init__(self, initial_map_file: str) -> None:
        self._mapped_area = mapped_area.MappedArea(initial_map_file)
        self._guard = guard.Guard(self._mapped_area.map_strings)
        self._terminated = False

    def _loop(self) -> bool:
        next_position = self._guard.get_next_position()
        #print(f'Position: {self._guard.position}. Next position: {next_position}.')
        terminate = False
        if not self._mapped_area.position_in_bounds(next_position):
            terminate = True
            return terminate
        if self._mapped_area.mask[next_position[0]][next_position[1]] is None:
            self._guard.heading.turn()
        else:
            self._guard.position = next_position
            self._mapped_area.mask[next_position[0]][next_position[1]] = 1
        return terminate

    def evolve(self) -> None:
        terminate = not self._mapped_area.position_in_bounds(
            self._guard.position)
        while not terminate:
            terminate = self._loop()
        self._terminated = True

    def count_visited_squares(self) -> int:
        if not self._terminated:
            self.evolve()
        cum_sum = 0
        for row in self._mapped_area.mask:
            cum_sum += sum(elem for elem in row if elem)
        return cum_sum


def solve(initial_map_file: Optional[str] = None) -> int:
    initial_map_file = initial_map_file or _INITIAL_MAP_FILE
    game = Game(initial_map_file)
    visited_squares = game.count_visited_squares()
    print(f'Visited a total of {visited_squares} unique squares.')
    return visited_squares


if __name__ == '__main__':
    solve()

