# Solution for AoC day 1 part 2.
import collections
from typing import Optional, Sequence

import extract_numbers


LOCAL_FILENAME = 'locations.txt'


def compute_similarity(
        loc_ids1: Sequence[int], loc_ids2: [Sequence[int]]) -> int:
    id1_counter = collections.Counter(loc_ids1)
    id2_counter = collections.Counter(loc_ids2)

    similarity = 0
    for id1, count1 in id1_counter.items():
        count2 = id2_counter.get(id1, 0)
        similarity += count1 * id1 * count2
    return similarity


def solve(local_filename: Optional[str] = None) -> int:
    local_filename = local_filename or LOCAL_FILENAME
    loc_ids1, loc_ids2 = extract_numbers.extract_numbers(local_filename)
    similarity = compute_similarity(loc_ids1, loc_ids2)
    print(f'Similarity: {similarity}.')
    return similarity


if __name__ == '__main__':
    solve()
