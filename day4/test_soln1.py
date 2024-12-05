"""Test for solution for day 4 part 1."""

import os
import shutil
import tempfile
from typing import List
import unittest

import soln1

_TEST_STR = (
    'MMMSXXMASM\n'
    'MSAMXMSMSA\n'
    'AMXSXMAAMM\n'
    'MSAMASMSMX\n'
    'XMASAMXAMM\n'
    'XXAMMXXAMA\n'
    'SMSMSASXSS\n'
    'SAXAMASAAA\n'
    'MAMMMXMMMM\n'
    'MXMXAXMASX')


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()
        test_file = os.path.join(cls.test_dir, 'test_puzzle.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        matches_found = soln1.solve(puzzle_input_file=self._test_file)
        expected_matches = 18
        self.assertEqual(matches_found, expected_matches)


if __name__ == '__main__':
    unittest.main()

