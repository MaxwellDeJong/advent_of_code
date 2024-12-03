"""Test for solution for day 2 part 2."""

from typing import Sequence
import unittest

import parameterized

import soln2


class TestSoln2(unittest.TestCase):

    @parameterized.parameterized.expand([
        ('1', [7, 6, 4, 2, 1], True),
        ('2', [1, 2, 7, 8, 9], False),
        ('3', [9, 7, 6, 2, 1], False),
        ('4', [1, 3, 2, 4, 5], True),
        ('5', [8, 6, 4, 4, 1], True),
        ('6', [1, 3, 6, 7, 9], True)])
    def test_is_safe_examples(
            self, name: str, report: Sequence[int], safe: bool) -> None:
        safety_value = soln2.is_safe(report)
        self.assertEqual(safety_value, safe)

    @parameterized.parameterized.expand([
        ('1', [9, 10, 8, 7, 6], True),
        ('2', [10, 12, 8, 7, 6], True),
        ('3', [9, 10, 8, 7, 6], True),
        ('4', [6, 9, 6, 4], True)])
    def test_is_safe_wrong_initial_sign(
            self, name: str, report: Sequence[int], safe: bool) -> None:
        safety_value = soln2.is_safe(report)
        self.assertEqual(safety_value, safe)

    @parameterized.parameterized.expand([
        ('1', [7, 6, 4, 2, 1], True),
        ('2', [1, 2, 7, 8, 9], False),
        ('3', [9, 7, 6, 2, 1], False),
        ('4', [1, 3, 2, 4, 5], False),
        ('5', [8, 6, 4, 4, 1], False),
        ('6', [1, 3, 6, 7, 9], True)])
    def test_is_safe_strict_tolerance(
            self, name: str, report: Sequence[int], safe: bool) -> None:
        with unittest.mock.patch('soln2.BAD_LEVEL_TOLERANCE', 0):
            safety_value = soln2.is_safe(report, bad_level_tolerance=0)
        self.assertEqual(safety_value, safe)


if __name__ == '__main__':
    unittest.main()
