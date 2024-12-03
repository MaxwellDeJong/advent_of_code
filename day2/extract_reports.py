"""Helper utility to extract reports from file."""

from typing import List


def extract(local_filename: str) -> List[List[int]]:
    report_list: List[List[int]] = []
    with open(local_filename) as f:
        for row in f:
            report = list(map(int, row.split()))
            report_list.append(report)
    return report_list

