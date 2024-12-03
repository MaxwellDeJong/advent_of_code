"""Check individual level values."""

from typing import Callable


class AmbiguousSignException(Exception):
    pass


def is_ambiguous_sign(diff: int) -> bool:
    return diff == 0

def get_valid_sign_fn(initial_diff: int) -> Callable[[int], bool]:
    if initial_diff > 0:
        return lambda value: value > 0
    if initial_diff < 0:
        return lambda value: value < 0
    raise AmbiguousSignException('Ambiguous sign when difference is zero.')

def is_valid_diff(diff: int, min_distance: int, max_distance: int) -> bool:
    abs_diff = abs(diff)
    if (abs_diff < min_distance) or (abs_diff > max_distance):
        return False
    return True

