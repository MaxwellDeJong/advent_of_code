"""Solution for day 12, part 2."""

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

def get_hlines(
        position: Tuple[int, int],
        region: Set[Tuple[int, int]]) -> Tuple[Optional[Tuple[int, int]],
                                               Optional[Tuple[int, int]]]:
    pos_x, pos_y = position
    top_neighbor = (pos_x - 1, pos_y)
    bottom_neighbor = (pos_x + 1, pos_y)
    top_line: Optional[Tuple[int, int]] = None
    bottom_line: Optional[Tuple[int, int]] = None
    if not top_neighbor in region:
        top_line = position
    if not bottom_neighbor in region:
        bottom_line = bottom_neighbor
    return top_line, bottom_line

def get_vlines(
        position: Tuple[int, int],
        region: Set[Tuple[int, int]]) -> Tuple[Optional[Tuple[int, int]],
                                               Optional[Tuple[int, int]]]:
    pos_x, pos_y = position
    left_neighbor = (pos_x, pos_y - 1)
    right_neighbor = (pos_x, pos_y + 1)
    left_line: Optional[Tuple[int, int]] = None
    right_line: Optional[Tuple[int, int]] = None
    if not left_neighbor in region:
        left_line = position
    if not right_neighbor in region:
        right_line = right_neighbor
    return left_line, right_line

def get_all_lines(region: Set[Tuple[int, int]]) -> (
        Tuple[List[Tuple[int, int]],
              List[Tuple[int, int]],
              List[Tuple[int, int]],
              List[Tuple[int, int]]]):
    top_lines: List[Tuple[int, int]] = []
    bottom_lines: List[Tuple[int, int]] = []
    left_lines: List[Tuple[int, int]] = []
    right_lines: List[Tuple[int, int]] = []
    for position in region:
        top_line, bottom_line = get_hlines(position, region)
        left_line, right_line = get_vlines(position, region)
        if top_line is not None:
            top_lines.append(top_line)
        if bottom_line is not None:
            bottom_lines.append(bottom_line)
        if left_line is not None:
            left_lines.append(left_line)
        if right_line is not None:
            right_lines.append(right_line)
    return top_lines, bottom_lines, left_lines, right_lines

def get_v_side_lines(
        line: Tuple[int, int],
        lines: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    candidate_lines = [
        (x, y) for x, y in lines if y == line[1] and x != line[0]]
    candidate_lines.sort()
    if not candidate_lines:
        return []
    side_lines: List[Tuple[int, int]] = []
    for i in range(1, len(candidate_lines) + 1):
        if (line[0] + i, line[1]) in candidate_lines:
            side_lines.append((line[0] + i, line[1]))
        else:
            break
    for i in range(1, len(candidate_lines) + 1):
        if (line[0] - i, line[1]) in candidate_lines:
            side_lines.append((line[0] - i, line[1]))
        else:
            return side_lines
    return side_lines

def get_h_side_lines(
        line: Tuple[int, int],
        lines: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    candidate_lines = [
        (x, y) for x, y in lines if (x == line[0]) and (y != line[1])]
    candidate_lines.sort()
    if not candidate_lines:
        return []
    side_lines: List[Tuple[int, int]] = []
    for i in range(1, len(candidate_lines) + 1):
        if (line[0], line[1] + i) in candidate_lines:
            side_lines.append((line[0], line[1] + i))
        else:
            break
    for i in range(1, len(candidate_lines) + 1):
        if (line[0], line[1] - i) in candidate_lines:
            side_lines.append((line[0], line[1] - i))
        else:
            return side_lines
    return side_lines

def calculate_sides(region: Set[Tuple[int, int]]) -> int:
    top_lines, bottom_lines, left_lines, right_lines = get_all_lines(region)
    for h_line in top_lines:
        for side_line in get_h_side_lines(h_line, top_lines):
            top_lines.remove(side_line)
    for h_line in bottom_lines:
        for side_line in get_h_side_lines(h_line, bottom_lines):
            bottom_lines.remove(side_line)
    for v_line in left_lines:
        for side_line in get_v_side_lines(v_line, left_lines):
            left_lines.remove(side_line)
    for v_line in right_lines:
        for side_line in get_v_side_lines(v_line, right_lines):
            right_lines.remove(side_line)
    return (len(top_lines) +
            len(bottom_lines) +
            len(left_lines) +
            len(right_lines))

def calculate_cost(plot: List[str]) -> Dict[str, int]:
    region_dict = assign_all_regions(plot)
    return {
        region_id: len(region) * calculate_sides(region)
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

