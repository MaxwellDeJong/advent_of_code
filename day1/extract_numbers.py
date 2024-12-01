# Solution for AoC day 1.
import re
from typing import List, Tuple


def extract_numbers(
        local_filename: str = None) -> Tuple[List[int], List[int]]:
    """Extract list of location IDs from local filename."""
    loc_ids1: List[int] = []
    loc_ids2: List[int] = []
    # Defensively handle malformed inputs.
    regex_pattern = re.compile(r'(\d+)\s+(\d+)')

    with open(local_filename) as f:
        for row in f:
            match = regex_pattern.match(row)
            if match:
                loc_ids1.append(int(match.group(1)))
                loc_ids2.append(int(match.group(2)))
    return loc_ids1, loc_ids2

