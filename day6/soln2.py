"""Solution for day 6 part 2."""

from typing import List, Optional, Tuple

import guard
import heading as heading_module
import mapped_area as mapped_area_module

_INITIAL_MAP_FILE = 'initial_map.txt'


class CycleChecker:

    def __init__(
            self,
            mapped_area: mapped_area_module.MappedArea,
            original_guard: guard.Guard) -> None:
        self._mapped_area = mapped_area
        self._guard = original_guard
        self._direction_history = self._initialize_direction_history()

    def _initialize_direction_history(self) -> (
            List[List[List[heading_module.Direction]]]):
        mask = self._mapped_area.mask
        n_row = len(mask)
        n_col = len(mask[0])
        direction_history = [[[] for _ in range(n_row)] for _ in range(n_col)]
        for i in range(n_row):
            for j in range(n_col):
                if mask[i][j] == 1:
                    direction_history[i][j].append(
                        self._guard.heading.direction)
                    return direction_history
        raise ValueError(f'Unable to initialize direction history.')

    def _update_direction_history(self) -> bool:
        position = self._guard.position
        if self._guard.heading.direction in (
                self._direction_history[position[0]][position[1]]):
            return True
        self._direction_history[position[0]][position[1]].append(
                self._guard.heading.direction)
        return False

    def _loop(self) -> bool:
        next_position = self._guard.get_next_position()
        #print(f'Position: {self._guard.position}. Next position: {next_position}.')
        if not self._mapped_area.position_in_bounds(next_position):
            return True
        if self._mapped_area.mask[next_position[0]][next_position[1]] is None:
            self._guard.heading.turn()
        else:
            self._guard.position = next_position
        return False

    def produces_cycle(self, verbose: bool = False) -> bool:
        terminate = not self._mapped_area.position_in_bounds(
            self._guard.position)
        cycle = False
        while not terminate:
            terminate = self._loop()
            if not terminate:
                cycle = self._update_direction_history()
                if cycle:
                    if verbose:
                        self.print_history()
                    return cycle
        if verbose:
            self.print_history()
        return cycle

    def print_history(self) -> None:
        mask = self._mapped_area.mask
        n_row = len(mask)
        n_col = len(mask[0])
        for i in range(n_row):
            row_list = list(self._mapped_area.map_strings[i])
            for j in range(len(row_list)):
                if len(self._direction_history[i][j]) > 0:
                    last_direction = self._direction_history[i][j][-1]
                    if last_direction == heading_module.Direction.left:
                        char = '<'
                    elif last_direction == heading_module.Direction.right:
                        char = '>'
                    elif last_direction == heading_module.Direction.up:
                        char = '^'
                    elif last_direction == heading_module.Direction.down:
                        char = 'v'
                    else:
                        char = '?'
                    row_list[j] = char
            print(''.join(row_list))
        print()


def find_valid_obstacle_positions(mask: List[List[Optional[int]]]) -> List[Tuple[int, int]]:
    def _valid_obstacle_position(mask_value: Optional[int]) -> bool:
        return mask_value == 0
    n_row = len(mask)
    n_col = len(mask[0])
    positions: List[Tuple[int, int]] = []
    for i in range(n_row):
        for j in range(n_col):
            if _valid_obstacle_position(mask[i][j]):
                positions.append((i, j))
    return positions


def patch_match_strings(
        map_strings: List[str], obstacle_indices: Tuple[int, int]) -> List[str]:
    obstacle_i, obstacle_j = obstacle_indices
    n_row = len(map_strings)
    n_col = len(map_strings[0])
    patched_map: List[str] = []
    for i, row_string in enumerate(map_strings):
        if i != obstacle_i:
            patched_map.append(row_string)
        else:
            row_list = list(row_string)
            row_list[obstacle_j] = '#'
            patched_map.append(''.join(row_list))
    return patched_map


def brute_force_cycle_counter(initial_map_file) -> int:
    mapped_area = mapped_area_module.MappedArea(initial_map_file)
    new_obstacle_positions = find_valid_obstacle_positions(mapped_area.mask)
    original_map_strings = [s for s in mapped_area.map_strings]
    n_cycles = 0
    for iteration, (position_i, position_j) in enumerate(new_obstacle_positions):
        if not iteration % 100:
            print(f'Iteration: {iteration}/{len(new_obstacle_positions)}.')
        # Patch mask with new obstacle
        mapped_area.mask[position_i][position_j] = None
        map_strings = patch_match_strings(
            original_map_strings, (position_i, position_j))
        original_guard = guard.Guard(map_strings)
        cycle_checker = CycleChecker(mapped_area, original_guard)
        n_cycles += cycle_checker.produces_cycle()
        # Restore mask
        mapped_area.mask[position_i][position_j] = 0
    return n_cycles


def solve(initial_map_file: Optional[str] = None) -> int:
    initial_map_file = initial_map_file or _INITIAL_MAP_FILE
    n_obstacle_positions = brute_force_cycle_counter(initial_map_file)
    print(f'Valid obstacle locations to induce cycles: {n_obstacle_positions}.')
    return n_obstacle_positions


if __name__ == '__main__':
    solve()

