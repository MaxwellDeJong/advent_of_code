# Simple test for AoC day 1 part 1 solution.
from typing import Sequence
import unittest

import parameterized

import soln1


class TestSoln1(unittest.TestCase):

    @parameterized.parameterized.expand([
        ('zeros', [0, 0, 0], [0, 0, 0], 0),
        ('duplicates', [1, 1, 2, 2], [1, 1, 2, 2], 0),
        ('non-zero', [1, 2, 3], [2, 3, 4], 3),
        ('non-zero_r', [1, 2, 3], [4, 3, 2], 3),
        ('non-zero_tuple', (1, 2, 3), (2, 3, 4), 3),
        ('non-zero_mixed', [1, 2, 3], (2, 3, 4), 3),
        ('example', [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 11)])
    def test_compute_sorted_distance(
            self,
            name: str,
            seq1: Sequence[int],
            seq2: Sequence[int],
            distance: int) -> None:
        computed_distance = soln1.compute_sorted_distance(seq1, seq2)
        self.assertEqual(computed_distance, distance)


if __name__ == '__main__':
    unittest.main()
