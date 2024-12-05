"""Solution for day 4, part 2."""

from typing import List, Optional, Tuple

PUZZLE_INPUT_FILE = 'puzzle_input.txt'
KEY = 'MAS'


def read_puzzle_rows(puzzle_input_file: str) -> List[str]:
    with open(puzzle_input_file, 'r') as puzzle_file:
        return [line.rstrip() for line in puzzle_file]

def find_key_center_indices(puzzle_rows: List[str], key: str) -> List[List[int]]:
    if not len(key) % 2:
        raise ValueError(f'Undetermined center with even-length key: {key}.')
    center_char = key[len(key) // 2]
    key_radius = (len(key) - 1) // 2

    n_row = len(puzzle_rows)
    n_col = len(puzzle_rows[0])
    key_len = len(key)

    if (key_len > n_row) or (key_len > n_col):
        return [[]]

    indices: List[List[int]] = []
    for row_idx in range(key_radius, n_row - key_radius):
        for col_idx in range(key_radius, n_col - key_radius):
            if puzzle_rows[row_idx][col_idx] == center_char:
                indices.append([row_idx, col_idx])
    return indices

def check_indices_match(indices: List[Tuple[int]], puzzle_rows: List[str], key: str) -> bool:
    chars = ''.join([puzzle_rows[i][j] for i, j in indices])
    return chars == key or chars == key[::-1]

def check_key_match(
        key_center_index: List[int], puzzle_rows: List[str], key: str) -> bool:
    key_radius = (len(key) - 1) // 2
    downward_right_indices = [(key_center_index[0] + k, key_center_index[1] + k) for k in range(-key_radius, key_radius + 1)]
    upward_right_indices = [(key_center_index[0] - k, key_center_index[1] + k) for k in range(-key_radius, key_radius + 1)]
    downward_right_match = check_indices_match(downward_right_indices, puzzle_rows, key)
    upward_right_match = check_indices_match(upward_right_indices, puzzle_rows, key)
    return downward_right_match and upward_right_match

def solve(
        puzzle_input_file: Optional[str] = None,
        key: Optional[str] = None) -> int:
    puzzle_input_file = puzzle_input_file or PUZZLE_INPUT_FILE
    key = key or KEY
    puzzle_rows = read_puzzle_rows(puzzle_input_file)
    key_center_indices = find_key_center_indices(puzzle_rows, key)
    n_matches = sum(check_key_match(key_center_idx, puzzle_rows, key) for key_center_idx in key_center_indices)
    print(f'Number of matches found: {n_matches}.')
    return n_matches


if __name__ == '__main__':
    #solve('test_puzzle.txt')
    solve()


