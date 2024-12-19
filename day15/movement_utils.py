from typing import List, Tuple

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

