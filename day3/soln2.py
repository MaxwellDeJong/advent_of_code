"""Solution for day 3 part 2."""

import re
from typing import List, Optional, Tuple

MEMORY_DUMP_FILENAME = 'memory_dump.txt'


def _find_next_do_index(
        do_not_index: int, do_indices: List[int]) -> Tuple[int, int]:
    for i, do_idx in enumerate(do_indices):
        if do_idx > do_not_index:
            return (i, do_idx)
    return (i, -1)
    
def find_exclusion_ranges(memory_str: str) -> List[Tuple[int, int]]:
    do_pattern = r"do\(\)"
    do_not_pattern = r"don\'t\(\)"
    do_indices = [
        match.start() for match in re.finditer(do_pattern, memory_str)]
    do_not_indices = [
        match.start() for match in re.finditer(do_not_pattern, memory_str)]
    exclusion_ranges: List[Tuple[int, int]] = []
    for do_not_idx in do_not_indices:
        offset, do_idx = _find_next_do_index(do_not_idx, do_indices)
        # Avoid iterating over elements we already know are too small.
        do_indices = do_indices[offset:]
        exclusion_ranges.append((do_not_idx, do_idx))
    return exclusion_ranges

def truncate_memory_str(memory_str: str) -> str:
    exclusion_ranges = find_exclusion_ranges(memory_str)
    if not exclusion_ranges:
        return memory_str
    start_index = 0
    keep_str = ''
    for exclusion_start, exclusion_end in exclusion_ranges:
        sub_str = memory_str[start_index:exclusion_start]
        keep_str += memory_str[start_index:exclusion_start]
        start_index = exclusion_end
    keep_str += memory_str[exclusion_end:]
    return keep_str

def add_valid_multiplications(
        memory_str: str, parse_conditionals: bool = True) -> int:
    if parse_conditionals:
        memory_str = truncate_memory_str(memory_str)
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
    ex = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    exclusion_ranges = find_exclusion_ranges(ex)
    print(f'Exclusion ranges: {exclusion_ranges}.')
    print(f'Truncated string: {truncate_memory_str(ex)}.')
    print(add_valid_multiplications(ex))
    print(solve())
