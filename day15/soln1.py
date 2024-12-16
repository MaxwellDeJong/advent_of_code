from typing import List, Optional, Tuple

_MAP_FILE = 'map.txt'
_MOVES_FILE = 'moves.txt'


def read_map(map_file: str) -> List[List[str]]:
    with open(map_file, 'r') as f:
        return [list(line.rstrip()) for line in f]

def read_move_chars(move_file: str) -> str:
    move_chars = ''
    with open(move_file, 'r') as f:
        for line in f:
            move_chars += line.rstrip()
    return move_chars

def initialize_position(
        raw_warehouse_map: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(raw_warehouse_map):
        if '@' in row:
            return (i, row.index('@'))
    raise ValueError('No robot detected in map.')

def get_next_position(
        position: Tuple[int, int], move_char: str) -> Tuple[int, int]:
    if move_char == '<':
        return (position[0], position[1] - 1)
    if move_char == '>':
        return (position[0], position[1] + 1)
    if move_char == '^':
        return (position[0] - 1, position[1])
    if move_char == 'v':
        return (position[0] + 1, position[1])
    raise ValueError(f'Unknown character: {move_char}.')

def get_all_next_positions(
        position: Tuple[int, int],
        move_char: str,
        warehouse_map: List[List[str]]) -> List[Tuple[int, int]]:
    x, y = position
    height = len(warehouse_map)
    width = len(warehouse_map[0])
    if move_char == '<':
        return [(x, i) for i in range(y-1)][::-1]
    if move_char == '>':
        return [(x, i) for i in range(y+1, width)]
    if move_char == '^':
        return [(i, y) for i in range(0, x)][::-1]
    if move_char == 'v':
        return [(i, y) for i in range(x+1, height)]
    raise ValueError(f'Unknown character: {move_char}.')

def valid_move(
        position: Tuple[int, int],
        move_char: str,
        warehouse_map: List[List[str]]) -> bool:
    next_x, next_y = get_next_position(position, move_char)
    if warehouse_map[next_x][next_y] == '.':
        return True
    if warehouse_map[next_x][next_y] == '#':
        return False
    return movable_box(position, move_char, warehouse_map)

def movable_box(
        next_char_indices: List[Tuple[int, int]],
        warehouse_map: List[List[str]]) -> bool:
    next_chars = [warehouse_map[x][y] for x, y in next_char_indices]
    for char in next_chars:
        if char == '.':
            return True
        if char == '#':
            return False
    return False

def update_boxes(
        position: Tuple[int, int],
        next_position_indices: List[Tuple[int, int]],
        warehouse_map: List[List[str]]) -> None:
    for next_x, next_y in next_position_indices:
        old_char = warehouse_map[next_x][next_y]
        warehouse_map[next_x][next_y] = 'O'
        if old_char == '.':
            return

def update_map(
        position: Tuple[int, int],
        move_char: str,
        warehouse_map: List[List[str]]) -> bool:
    next_position = get_next_position(position, move_char)
    next_x, next_y = next_position
    if warehouse_map[next_x][next_y] == '.':
        return next_position
    if warehouse_map[next_x][next_y] == '#':
        return position
    next_char_indices = get_all_next_positions(
        position, move_char, warehouse_map)
    if not movable_box(next_char_indices, warehouse_map):
        return position
    update_boxes(position, next_char_indices, warehouse_map)
    warehouse_map[next_x][next_y] = '.'
    return next_position

def evolve_map(
        move_chars: str, raw_warehouse_map: List[List[str]]) -> None:
    position = initialize_position(raw_warehouse_map)
    raw_warehouse_map[position[0]][position[1]] = '.'
    for move_char in move_chars:
        position = update_map(position, move_char, raw_warehouse_map)

def calculate_gps_sum(warehouse_map: List[List[str]]) -> int:
    cum_sum = 0
    for i, row in enumerate(warehouse_map):
        for j, char in enumerate(row):
            if char == 'O':
                cum_sum += 100 * i + j
    return cum_sum


if __name__ == '__main__':
    move_chars = read_move_chars(_MOVES_FILE)
    raw_warehouse_map = read_map(_MAP_FILE)
    evolve_map(move_chars, raw_warehouse_map)
    print(calculate_gps_sum(raw_warehouse_map))

