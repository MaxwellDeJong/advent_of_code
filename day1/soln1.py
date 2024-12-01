# Solution for AoC day 1 part 1.
from typing import Optional, Sequence

import extract_numbers


LOCAL_FILENAME = 'locations.txt'


def compute_sorted_distance(
        loc_ids1: Sequence[int], loc_ids2: [Sequence[int]]) -> int:
    loc_ids1_list = [loc_id for loc_id in loc_ids1]
    loc_ids2_list = [loc_id for loc_id in loc_ids2]
    loc_ids1_list.sort()
    loc_ids2_list.sort()

    cum_sum = sum(abs(loc1 - loc2) for loc1, loc2 in zip(
        loc_ids1_list, loc_ids2_list))
    return cum_sum


def solve(local_filename: Optional[str] = None) -> int:
    local_filename = local_filename or LOCAL_FILENAME
    loc_ids1, loc_ids2 = extract_numbers.extract_numbers(local_filename)
    sorted_distance = compute_sorted_distance(loc_ids1, loc_ids2)
    print(f'Sorted distance: {sorted_distance}.')
    return sorted_distance


if __name__ == '__main__':
    solve()
