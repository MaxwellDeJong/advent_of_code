from typing import List, Sequence, Tuple

import block as block_module


def read_map(map_file: str) -> List[List[str]]:
    with open(map_file, 'r') as f:
        return [list(line.rstrip()) for line in f]

def read_move_chars(move_file: str) -> str:
    move_chars = ''
    with open(move_file, 'r') as f:
        for line in f:
            move_chars += line.rstrip()
    return move_chars

def resize_map(raw_warehouse_map: List[List[str]]) -> List[List[str]]:
    change_dict = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.'}
    for i, row in enumerate(raw_warehouse_map):
        for j, char in enumerate(row):
            raw_warehouse_map[i][j] = change_dict[char]
    resized_map: List[List[str]] = []
    for row in raw_warehouse_map:
        resized_map.append(list(''.join(row)))
    return resized_map

def get_warehouse_mask(warehouse_map: List[List[str]]) -> List[List[str]]:
    mask: List[List[str]] = []
    for row in warehouse_map:
        row_chars: List[str] = []
        for char in row:
            if char == '#':
                row_chars.append('#')
            else:
                row_chars.append('.')
        mask.append(row_chars)
    return mask

def initialize_position(
        raw_warehouse_map: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(raw_warehouse_map):
        if '@' in row:
            return (i, row.index('@'))
    raise ValueError('No robot detected in map.')

def initialize_blocks(
        raw_warehouse_map: List[List[str]]) -> List[block_module.Block]:
    blocks: List[block_module.Block] = []
    for i, row in enumerate(raw_warehouse_map):
        for j, char in enumerate(row):
            if char == '[':
                blocks.append(block_module.Block((i, j), (i, j + 1)))
    return blocks

def initialize_map_information(map_file: str) -> (
        Tuple[Tuple[int, int], List[block_module.Block], List[List[str]]]):
    raw_warehouse_map = read_map(map_file)  
    resized_map = resize_map(raw_warehouse_map)
    position = initialize_position(resized_map)
    blocks = initialize_blocks(resized_map)
    mask = get_warehouse_mask(resized_map)
    return (position, blocks, mask)

def render_map(
        position: Tuple[int, int],
        blocks: Sequence[block_module.Block],
        warehouse_mask: List[List[str]]) -> List[List[str]]:
    rendered_map: List[List[str]] = []
    symbol_dict = {
        position: '@'}
    for block in blocks:
        symbol_dict[block.left] = '['
        symbol_dict[block.right] = ']'
    for i, row in enumerate(warehouse_mask):
        chars: List[str] = []
        for j, char in enumerate(row):
            chars.append(symbol_dict.get((i, j), char))
        rendered_map.append(chars)
    return rendered_map

def print_rendered_map(rendered_map: List[List[str]]) -> None:
    for row in rendered_map:
        print(''.join(row))
    print()

