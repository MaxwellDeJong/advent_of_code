"""Solution for day 12, part 1."""

import copy
from typing import Dict, List, Optional, Set, Tuple

_MAP_FILE = 'map.txt'


def read_map(map_file: str) -> List[str]:
    with open(map_file, 'r') as f:
        lines = [line.rstrip() for line in f]
    return lines

def valid_position(position: Tuple[int, int], plot: List[str], value: str) -> bool:
    x, y = position
    plot_size = len(plot)
    if x < 0 or y < 0:
        return False
    if x >= plot_size or y >= plot_size:
        return False
    return plot[x][y] == value

def get_neighbors(pos_x: int, pos_y: int) -> List[Tuple[int, int]]:
    return [
        (pos_x - 1, pos_y),
        (pos_x + 1, pos_y),
        (pos_x, pos_y - 1),
        (pos_x, pos_y + 1)]

def assign_region(
        initial_pos: Tuple[int, int],
        plot: List[str]) -> List[Tuple[int, int]]:
    positions = {initial_pos}
    position_value = plot[initial_pos[0]][initial_pos[1]]
    while True:
        new_positions = copy.deepcopy(positions)
        for pos_x, pos_y in positions:
            for neighbor in get_neighbors(pos_x, pos_y):
                if valid_position(neighbor, plot, position_value):
                    new_positions.add(neighbor)
        if len(positions) == len(new_positions):
            return positions
        positions = new_positions

def assign_all_regions(plot: List[str]) -> Dict[int, Set[Tuple[int, int]]]:
    size = len(plot)
    unassigned_positions = set()
    region_dict: Dict[int, Set[Tuple[int, int]]] = {}
    for pos_x in range(size):
        for pos_y in range(size):
            unassigned_positions.add((pos_x, pos_y))
    region_id = 0
    while len(unassigned_positions) > 0:
        initial_position = next(iter(unassigned_positions))
        region_positions = assign_region(initial_position, plot)
        region_dict[region_id] = region_positions
        unassigned_positions -= region_positions
        region_id += 1
    return region_dict

def calculate_perimeter(region: Set[Tuple[int, int]]) -> int:
    cum_perimeter = 0
    for position in region:
        pos_x, pos_y = position
        n_neighbors = sum(
            neighbor in region for neighbor in get_neighbors(pos_x, pos_y))
        cum_perimeter += 4 - n_neighbors
    return cum_perimeter

def calculate_cost(plot: List[str]) -> Dict[str, int]:
    region_dict = assign_all_regions(plot)
    return {
        region_id: len(region) * calculate_perimeter(region)
        for region_id, region in region_dict.items()}

def solve(map_file: Optional[str] = None) -> int:
    map_file = map_file or _MAP_FILE
    plot = read_map(map_file)
    cost_dict = calculate_cost(plot)
    cost = sum(cost_dict.values())
    print(f'Total cost: {cost}.')
    return cost


if __name__ == '__main__':
    solve()

