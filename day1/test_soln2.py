# Simple test for AoC day 1 part 2 solution.
from typing import Sequence
import unittest

import parameterized

import soln2


class TestSoln1(unittest.TestCase):

    @parameterized.parameterized.expand([
        ('empty_list1', [], [1], 0),
        ('empty_list2', [1], [], 0),
        ('single_element', [1], [1], 1),
        ('single_element_not_matching', [1], [0], 0),
        ('duplicate_list1', [1, 1], [1], 2),
        ('duplicate_list2', [1], [1, 1], 2),
        ('mixed_sequence', [1], (1, 1), 2),
        ('tuple', (1,), (1, 1), 2),
        ('extraneous_list1', [1, 4], [1, 1], 2),
        ('extraneous_list2', [1, 1], [1, 4], 2),
        ('example', [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 31)])
    def test_compute_sorted_distance(
            self,
            name: str,
            seq1: Sequence[int],
            seq2: Sequence[int],
            similarity: int) -> None:
        computed_similarity = soln2.compute_similarity(seq1, seq2)
        self.assertEqual(computed_similarity, similarity)


if __name__ == '__main__':
    unittest.main()
