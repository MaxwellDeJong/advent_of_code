"""Test for level checker utility."""

from typing import Sequence
import unittest

import parameterized

import level_checker


class TestLevelChecker(unittest.TestCase):

    @parameterized.parameterized.expand([
        ('intermediate_diff', 2, 1, 3, True),
        ('min_diff', 2, 2, 3, True),
        ('max_diff', 3, 1, 3, True),
        ('small_diff', 0, 1, 3, False),
        ('large_diff', 8, 1, 3, False)])
    def test_is_valid_diff(
            self,
            name: str,
            diff: int,
            min_distance: int,
            max_distance: int,
            valid: bool) -> None:
        valid_diff = level_checker.is_valid_diff(
            diff, min_distance, max_distance)
        self.assertEqual(valid_diff, valid)

    @parameterized.parameterized.expand([
        ('positive_positive', 1, 1, True),
        ('positive_negative', 1, -1, False),
        ('negative_positive', -1, 1, False),
        ('negative_negative', -1, -1, True)])
    def test_get_valid_sign_fn(
            self,
            name: str,
            initial_diff: int,
            value: int,
            valid: bool) -> None:
        valid_sign_fn = level_checker.get_valid_sign_fn(initial_diff)
        valid_sign = valid_sign_fn(value)
        self.assertEqual(valid_sign, valid)

    def test_get_valid_sign_fn_exception(self) -> None:
        initial_diff = 0
        self.assertRaises(
            level_checker.AmbiguousSignException,
            level_checker.get_valid_sign_fn,
            initial_diff)


if __name__ == '__main__':
    unittest.main()

