from typing import Dict, List, Optional, Sequence, Tuple

import block as block_module
import map_utils
import movement_utils

_MAP_FILE = 'map.txt'
_MOVES_FILE = 'moves.txt'


def movable_horizontal_box(
        next_char_indices: List[Tuple[int, int]],
        warehouse_map: List[List[str]]) -> bool:
    next_chars = [warehouse_map[x][y] for x, y in next_char_indices]
    for char in next_chars:
        if char == '.':
            return True
        if char == '#':
            return False
    return False

def movable_vertical_boxes(
        all_next_char_indices: Dict[Tuple[int, int], List[Tuple[int, int]]],
        warehouse_map: List[List[str]]) -> bool:
    for next_char_indices in all_next_char_indices.values():
        next_chars = [warehouse_map[x][y] for x, y in next_char_indices]
        for char in next_chars:
            if char == '#':
                return False
            if char == '.':
                break
    return True

def valid_horizontal_move(
        position: Tuple[int, int],
        move_char: str,
        warehouse_map: List[List[str]]) -> bool:
    next_x, next_y = movement_utils.get_next_position(position, move_char)
    if warehouse_map[next_x][next_y] == '.':
        return True
    if warehouse_map[next_x][next_y] == '#':
        return False
    return movable_horizontal_box(position, move_char, warehouse_map)

def get_neighboring_blocks(
        next_position: Tuple[int, int],
        move_char: str,
        warehouse_map: List[List[str]]) -> List[block_module.Block]:
    next_x, next_y = next_position
    if warehouse_map[next_x][next_y] == '[':
        blocks = [block_module.Block(next_position, (next_x, next_y + 1))]
    elif warehouse_map[next_x][next_y] == ']':
        blocks = [block_module.Block((next_x, next_y - 1), next_position)]
    else:
        raise ValueError(f'Invalid character at next position: '
                         f'{warehouse_map[next_x][next_y]}.')
    n_prev_blocks = len(blocks)
    while True:
        for block in blocks:
            x_left, y_left = block.left
            x_right, y_right = block.right
            if move_char == '^':
                x_offset = -1
            elif move_char == 'v':
                x_offset = 1
            else:
                raise ValueError(f'Invalid move character: {move_char}.')
            possible_lefts = [
                (x_left + x_offset, y_left),
                (x_left + x_offset, y_left - 1),
                (x_left + x_offset, y_left + 1)]
            possible_rights = [
                (x_right + x_offset, y_right),
                (x_right + x_offset, y_right - 1),
                (x_right + x_offset, y_right + 1)]
            for possible_left_x, possible_left_y in possible_lefts:
                char = warehouse_map[possible_left_x][possible_left_y]
                if char == '[':
                    new_block = block_module.Block(
                        (possible_left_x, possible_left_y),
                        (possible_left_x, possible_left_y + 1))
                    if new_block not in blocks:
                        blocks.append(new_block)
            for possible_right_x, possible_right_y in possible_rights:
                char = warehouse_map[possible_right_x][possible_right_y]
                if char == ']':
                    new_block = block_module.Block(
                        (possible_right_x, possible_right_y - 1),
                        (possible_right_x, possible_right_y))
                    if new_block not in blocks:
                        blocks.append(new_block)
        if len(blocks) == n_prev_blocks:
            return blocks
        n_prev_blocks = len(blocks)

def update_horizontal_boxes(
        blocks: Sequence[block_module.Block],
        move_char: str,
        next_position_indices: List[Tuple[int, int]],
        warehouse_map: List[List[str]]) -> None:
    blocks_to_update: List[block_module.Block] = []
    for next_position in next_position_indices:
        for block in blocks:
            if block.left == next_position:
                blocks_to_update.append(block)
                break
        if warehouse_map[next_position[0]][next_position[1]] == '.':
            break
    for block in blocks_to_update:
        block.update(move_char)

def form_next_char_dict(
        neighboring_blocks: List[block_module.Block],
        move_char: str,
        warehouse_map: List[List[str]]) -> (
            Dict[Tuple[int, int], List[Tuple[int, int]]]):
    all_next_char_indices: Dict[
        Tuple[int, int], List[Tuple[int, int]]] = {}
    for block in neighboring_blocks:
        left_block_position = block.left
        right_block_position = block.right
        next_left_char_indices = movement_utils.get_all_next_positions(
            left_block_position, move_char, warehouse_map)
        next_right_char_indices = movement_utils.get_all_next_positions(
            right_block_position, move_char, warehouse_map)
        all_next_char_indices[left_block_position] = (
            movement_utils.get_all_next_positions(
                left_block_position, move_char, warehouse_map))
        all_next_char_indices[right_block_position] = (
            movement_utils.get_all_next_positions(
                right_block_position, move_char, warehouse_map))
    return all_next_char_indices

def update_map(
        position: Tuple[int, int],
        blocks: List[block_module.Block],
        move_char: str,
        warehouse_mask: List[List[str]]) -> Tuple[int, int]:
    next_position = movement_utils.get_next_position(position, move_char)
    next_x, next_y = next_position
    warehouse_map = map_utils.render_map(position, blocks, warehouse_mask)
    if warehouse_map[next_x][next_y] == '.':
        return next_position
    if warehouse_map[next_x][next_y] == '#':
        return position
    if move_char == '<' or move_char == '>':
        next_char_indices = movement_utils.get_all_next_positions(
            position, move_char, warehouse_map)
        if not movable_horizontal_box(next_char_indices, warehouse_map):
            return position
        update_horizontal_boxes(
            blocks, move_char, next_char_indices, warehouse_map)
    else:
        neighboring_blocks = get_neighboring_blocks(
            next_position, move_char, warehouse_map)
        all_next_char_indices = form_next_char_dict(
            neighboring_blocks, move_char, warehouse_map)
        if not movable_vertical_boxes(
                all_next_char_indices, warehouse_map):
            return position
        for block in neighboring_blocks:
            global_index = blocks.index(block)
            blocks[global_index].update(move_char)
    return next_position

def solve(
        map_file: Optional[str] = None,
        moves_file: Optional[str] = None) -> None:
    map_file = map_file or _MAP_FILE
    moves_file = moves_file or _MOVES_FILE
    position, blocks, warehouse_mask = map_utils.initialize_map_information(
        map_file)
    move_chars = map_utils.read_move_chars(moves_file)
    for move_char in move_chars:
        position = update_map(position, blocks, move_char, warehouse_mask)
    print('FINAL MAP...')
    warehouse_map = map_utils.render_map(position, blocks, warehouse_mask)
    map_utils.print_rendered_map(warehouse_map)
    return sum(block.gps_score() for block in blocks)


if __name__ == '__main__':
    print(solve())

