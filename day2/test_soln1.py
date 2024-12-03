"""Test for solution for day 2 part 1."""

from typing import Sequence
import unittest

import parameterized

import soln1


class TestSoln1(unittest.TestCase):

    @parameterized.parameterized.expand([
        ('1', [7, 6, 4, 2, 1], True),
        ('2', [1, 2, 7, 8, 9], False),
        ('3', [9, 7, 6, 2, 1], False),
        ('4', [1, 3, 2, 4, 5], False),
        ('5', [8, 6, 4, 4, 1], False),
        ('6', [1, 3, 6, 7, 9], True)])
    def test_is_safe(
            self, name: str, report: Sequence[int], safe: bool) -> None:
        safety_value = soln1.is_safe(report)
        self.assertEqual(safety_value, safe)


if __name__ == '__main__':
    unittest.main()
