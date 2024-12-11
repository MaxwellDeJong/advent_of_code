"""Solution for day 10 part 1."""

from typing import List, Optional, Set, Tuple

_TRAIL_MAP_FILE = 'trailmap.txt'


def load_trailmap(trail_map_file: str) -> List[List[int]]:
    with open(trail_map_file, 'r') as f:
        return [list(map(int, line.rstrip())) for line in f]

def find_trailheads(trail_map: List[List[int]]) -> List[Tuple[int, int]]:
    trailheads: List[Tuple[int, int]] = []
    for i, row in enumerate(trail_map):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.append((i, j))
    return trailheads

def valid_location(
        candidate_loc: Tuple[int, int],
        prev_height: int,
        trail_map: List[List[int]]) -> bool:
    n_row = len(trail_map)
    n_col = len(trail_map[0])
    candidate_x, candidate_y = candidate_loc
    if candidate_x < 0 or candidate_y < 0:
        return False
    if candidate_x >= n_row or candidate_y >= n_col:
        return False
    return trail_map[candidate_x][candidate_y] == prev_height + 1

def valid_trailhead(
        trail_map: List[List[int]],
        current_location: Tuple[int, int],
        terminal_locations: Set[Tuple[int, int]]) -> None:
    loc_x, loc_y = current_location
    height = trail_map[loc_x][loc_y]
    if height == 9:
        terminal_locations.add(current_location)
        return 1
    candidate_locs = [
        (loc_x - 1, loc_y),
        (loc_x + 1, loc_y),
        (loc_x, loc_y - 1),
        (loc_x, loc_y + 1)]
    valid_locs = [
        candidate_loc for candidate_loc in candidate_locs
        if valid_location(candidate_loc, height, trail_map)]
    for valid_loc in valid_locs:
        valid_trailhead(trail_map, valid_loc, terminal_locations)

def solve(trail_map_file: Optional[str] = None) -> int:
    trail_map_file = trail_map_file or _TRAIL_MAP_FILE
    trail_map = load_trailmap(trail_map_file)
    trailheads = find_trailheads(trail_map)
    score = 0
    for trailhead in trailheads:
        terminal_locations = set()
        valid_trailhead(trail_map, trailhead, terminal_locations)
        score += len(terminal_locations)
    print(f'Score: {score}.')
    return score


if __name__ == '__main__':
    solve()

