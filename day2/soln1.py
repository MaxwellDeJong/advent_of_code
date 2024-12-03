"""Solution for day 2 part 1."""

from typing import Callable, Sequence, Optional

import extract_reports
import level_checker


REPORT_FILENAME = 'report_data.txt'
MIN_DISTANCE = 1
MAX_DISTANCE = 3


def is_valid_diff(diff: int) -> bool:
    return level_checker.is_valid_diff(diff, MIN_DISTANCE, MAX_DISTANCE)

def is_safe(report: Sequence[int]) -> bool:
    if len(report) < 2:
        return True

    initial_diff = report[1] - report[0]
    if abs(initial_diff) < MIN_DISTANCE:
        return False
    is_valid_sign = level_checker.get_valid_sign_fn(initial_diff)

    diff_generator = (xf - xi for xi, xf in zip(report[:-1], report[1:]))
    for diff in diff_generator:
        if not is_valid_sign(diff) or not is_valid_diff(diff):
            return False
    return True

def solve(report_filename: Optional[str] = None) -> int:
    report_filename = report_filename or REPORT_FILENAME
    report_list = extract_reports.extract(report_filename)
    number_safe = sum(is_safe(report) for report in report_list)
    print(f'Number of safe reports: {number_safe}/{len(report_list)}.')
    return number_safe


if __name__ == '__main__':
    solve()
