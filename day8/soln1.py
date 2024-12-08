"""Solution for day 8 part 1."""

from typing import Dict, List, Optional, Sequence, Set, Tuple

_EXCLUDED_CHARS = ['.']
_ANTENNA_MAP_FILE = 'antenna_map.txt'


def read_map(antenna_map_path: str) -> List[str]:
    with open(antenna_map_path, 'r') as f:
        return [line.rstrip() for line in f]

def index_map(antenna_map: List[str]) -> Dict[str, Tuple[int, int]]:
    n_row = len(antenna_map)
    n_col = len(antenna_map[0])
    antenna_index: Dict[str, Tuple[int, int]] = {}
    for i, row in enumerate(antenna_map):
        for j in range(n_col):
            char = antenna_map[i][j]
            if not char in _EXCLUDED_CHARS:
                antenna_index[char] = antenna_index.get(char, []) + [(i, j)]
    return antenna_index

def form_valid_antinodes(
        initial_loc: Tuple[int, int],
        second_loc: Tuple[int, int],
        n_row: int,
        n_col: int) -> List[Tuple[int, int]]:
    valid_antinode = (lambda loc: (
        loc[0] >= 0 and loc[0] < n_row and loc[1] >= 0 and loc[1] < n_col))
    row_diff = second_loc[0] - initial_loc[0]
    col_diff = second_loc[1] - initial_loc[1]
    antinode_locs = [
        (initial_loc[0] - row_diff, initial_loc[1] - col_diff),
        (second_loc[0] + row_diff, second_loc[1] + col_diff)]
    return [loc for loc in antinode_locs if valid_antinode(loc)]

def update_antinodes(
        locations: Sequence[Tuple[int, int]],
        n_row: int,
        n_col: int,
        antinode_locations: Set[Tuple[int, int]]) -> None:
    for i, initial_loc in enumerate(locations):
        for second_loc in locations[i+1:]:
            row_diff = second_loc[0] - initial_loc[0]
            col_diff = second_loc[1] - initial_loc[1]
            for antinode in form_valid_antinodes(
                    initial_loc, second_loc, n_row, n_col):
                antinode_locations.add(antinode)

def find_antinodes(antenna_map: List[str]) -> int:
    antenna_index = index_map(antenna_map)
    n_row = len(antenna_map)
    n_col = len(antenna_map[0])
    antinode_locations: Set[Tuple[int, int]] = set()
    for indices in antenna_index.values():
        update_antinodes(indices, n_row, n_col, antinode_locations)
    return len(antinode_locations)

def solve(antenna_map_path: Optional[str] = None) -> int:
    antenna_map_path = antenna_map_path or _ANTENNA_MAP_FILE
    antenna_map = read_map(antenna_map_path)
    n_antinodes = find_antinodes(antenna_map)
    print(f'Found {n_antinodes} unique antinode locations.')
    return n_antinodes


if __name__ == '__main__':
    solve()

