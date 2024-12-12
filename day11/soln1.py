"""Solution for day 11, part 1."""

from typing import List, Optional, Tuple

_STONES_FILE = 'stones.txt'


def read_stones(stones_file: str) -> List[int]:
    with open(stones_file, 'r') as f:
        stones_str = f.read().rstrip()
    return list(map(int, stones_str.split()))

def split(str_number: str) -> Tuple[int, int]:
    split_idx = len(str_number) // 2
    return int(str_number[:split_idx]), int(str_number[split_idx:])

def evolve_stones(stones: List[int]) -> None:
    new_stones: List[Tuple[int, int]] = []
    for i, stone in enumerate(stones):
        stone_str = str(stone)
        if stone == 0:
            stones[i] = 1
        elif not len(stone_str) % 2:
            left_val, right_val = split(stone_str)
            stones[i] = left_val
            new_stones.append((i + 1, right_val))
        else:
            stones[i] *= 2024
    offset = 0
    for stone_idx, stone_value in new_stones:
        stones.insert(stone_idx + offset, stone_value)
        offset += 1

def solve(stones_file: Optional[str] = None, n_iterations: int = 25) -> int:
    stones_file = stones_file or _STONES_FILE
    stones = read_stones(stones_file)
    for _ in range(n_iterations):
        evolve_stones(stones)
    stones_len = len(stones)
    print(f'Length after {n_iterations} blinks: {stones_len}.')
    return stones_len


if __name__ == '__main__':
    solve()

