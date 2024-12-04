"""Solution for day 3 part 1."""

import re
from typing import Optional

MEMORY_DUMP_FILENAME = 'memory_dump.txt'


def add_valid_multiplications(memory_str: str) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    str_matches = re.findall(pattern, memory_str)
    matches = [tuple(map(int, string_tuple)) for string_tuple in str_matches]
    products = map(
        lambda number_pair: number_pair[0] * number_pair[1], matches)
    return sum(products)


def solve(memory_dump_file: Optional[str] = None) -> int:
    memory_dump_file = memory_dump_file or MEMORY_DUMP_FILENAME
    with open(memory_dump_file, 'r') as f:
        memory_str = f.read()
    result = add_valid_multiplications(memory_str)
    print(f'Solution: {result}.')
    return result


if __name__ == '__main__':
    print(solve())
