"""Solution for day 2 part 2."""

from typing import Callable, Optional, Sequence

import extract_reports
import level_checker


REPORT_FILENAME = 'report_data.txt'
BAD_LEVEL_TOLERANCE = 1
MIN_DISTANCE = 1
MAX_DISTANCE = 3


def is_valid_diff(diff: int) -> bool:
    return level_checker.is_valid_diff(diff, MIN_DISTANCE, MAX_DISTANCE)

def is_safe(
        report: Sequence[int],
        bad_level_tolerance: int = BAD_LEVEL_TOLERANCE) -> bool:
    if len(report) < 2:
        return True

    if bad_level_tolerance < 0:
        return False    

    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if i == 1:
            if level_checker.is_ambiguous_sign(diff):
                return is_safe(report[1:], bad_level_tolerance - 1)
            is_valid_sign = level_checker.get_valid_sign_fn(diff)
        if not is_valid_sign(diff) or not is_valid_diff(diff):
            # There are 3 ways to remove an element to produce subarrays when
            # there is an issue between elements i and i - 1:
            #   1. Remove element i - 1 
            #   2. Remove element i
            #   3. Remove the first element to reset the sign function
            sub_report1 = report[:i-1] + report[i:]
            sub_report2 = report[:i] + report[i+1:]
            sub_report3 = report[1:]
            return (is_safe(sub_report1, bad_level_tolerance - 1) or
                    is_safe(sub_report2, bad_level_tolerance - 1) or 
                    is_safe(sub_report3, bad_level_tolerance - 1))
    return True

def solve(report_filename: Optional[str] = None) -> int:
    report_filename = report_filename or REPORT_FILENAME
    report_list = extract_reports.extract(report_filename)
    number_safe = sum(is_safe(report) for report in report_list)
    print(f'Number of safe reports: {number_safe}/{len(report_list)}.')
    return number_safe


if __name__ == '__main__':
    solve()
