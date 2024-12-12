"""Solution for day 11, part 2."""

import collections
from typing import Dict, List, Optional, Tuple

_STONES_FILE = 'stones.txt'


def read_stones(stones_file: str) -> List[int]:
    with open(stones_file, 'r') as f:
        stones_str = f.read().rstrip()
    return list(map(int, stones_str.split()))

def initialize_stone_counts(stones_list: List[int]) -> Dict[int, int]:
    stone_counter = collections.Counter(stones_list)
    return {
        stone_value: stone_count
        for stone_value, stone_count in stone_counter.items()}

def update_dict(stone_dict: Dict[int, int]) -> Dict[int, int]:
    updated_dict: Dict[int, int] = {}
    for value, count in stone_dict.items():
        for new_value, new_count in evolve_stone(value, count):
            updated_dict[new_value] = (
                updated_dict.get(new_value, 0) + new_count)
    return updated_dict

def split(str_number: str) -> Tuple[int, int]:
    split_idx = len(str_number) // 2
    return int(str_number[:split_idx]), int(str_number[split_idx:])

def evolve_stone(value: int, count: int) -> List[int]:
    if value == 0:
        values = [1]
        counts = [count]
    else:
        stone_str = str(value)
        if not len(stone_str) % 2:
            left_val, right_val = split(stone_str)
            if left_val == right_val:
                values = [left_val]
                counts = [2 * count]
            else:
                values = [left_val, right_val]
                counts = [count, count]
        else:
            values = [value * 2024]
            counts = [count]
    return [(value, count) for value, count in zip(values, counts)]

def solve(stones_file: Optional[str] = None, n_iterations: int = 75) -> int:
    stones_file = stones_file or _STONES_FILE
    stones_list = read_stones(stones_file)
    stones_dict = initialize_stone_counts(stones_list)
    for _ in range(n_iterations):
        stones_dict = update_dict(stones_dict)
    stones_len = sum(stones_dict.values())
    print(f'Length after {n_iterations} blinks: {stones_len}.')
    return stones_len


if __name__ == '__main__':
    solve()

