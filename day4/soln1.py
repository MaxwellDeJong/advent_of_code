"""Solution for day 4 part 1."""

from typing import List, Optional

PUZZLE_INPUT_FILE = 'puzzle_input.txt'
KEY = 'XMAS'


def read_puzzle_rows(puzzle_input_file: str) -> List[str]:
    with open(puzzle_input_file, 'r') as puzzle_file:
        return [line.rstrip() for line in puzzle_file]

def count_occurences(chars: str, key: str) -> int:
    count = 0
    key_len = len(key)
    key_r = key[::-1]
    for l_ptr in range(0, len(chars) - key_len + 1):
        if chars[l_ptr:l_ptr+key_len] == key:
            count += 1
        if chars[l_ptr:l_ptr+key_len] == key_r:
            count += 1
    return count

def get_columns(puzzle_rows: List[str]) -> List[str]:
    n_col = len(puzzle_rows[0])
    return [''.join([row[col] for row in puzzle_rows]) for col in range(n_col)]

def get_downward_right_diagonals(puzzle_rows: List[str], key: str) -> List[str]:
    n_row = len(puzzle_rows)
    n_col = len(puzzle_rows[0])
    key_len = len(key)

    top_indices = [[0, j] for j in range(n_col)]
    bottom_indices = [[n_row - 1, j] for j in range(n_col)]
    left_indices = [[i, 0] for i in range(1, n_row - 1)]
    right_indices = [[i, n_col - 1] for i in range(1, n_row - 1)]

    starting_indices = (
        [[i, 0] for i in range(0, n_row - key_len + 1)] +
        [[0, j] for j in range(1, n_col - key_len + 1)])
    diagonals: List[str] = []
    for starting_idx in starting_indices:
        max_k = min(n_row - starting_idx[0], n_col - starting_idx[1])
        if max_k >= key_len - 1:
            diagonal_chars = [
                puzzle_rows[starting_idx[0]+k][starting_idx[1]+k]
                for k in range(max_k)]
            diagonals.append(''.join(diagonal_chars))
    return diagonals

def get_upward_right_diagonals(puzzle_rows: List[str], key: str) -> List[str]:
    puzzle_rows_reversed = [row[::-1] for row in puzzle_rows]
    return get_downward_right_diagonals(puzzle_rows_reversed, key)

def form_all_lines(puzzle_rows: List[str], key: str) -> List[str]:
    return (puzzle_rows +
            get_columns(puzzle_rows) +
            get_downward_right_diagonals(puzzle_rows, key) +
            get_upward_right_diagonals(puzzle_rows, key))

def solve(
        puzzle_input_file: Optional[str] = None,
        key: Optional[str] = None) -> int:
    puzzle_input_file = puzzle_input_file or PUZZLE_INPUT_FILE
    key = key or KEY
    puzzle_rows = read_puzzle_rows(puzzle_input_file)
    all_lines = form_all_lines(puzzle_rows, key)
    n_matches = sum(count_occurences(line, key) for line in all_lines)
    print(f'Number of matches found: {n_matches}.')
    return n_matches


if __name__ == '__main__':
    solve()

