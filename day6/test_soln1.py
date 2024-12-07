"""Test for solution for day 6 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

_TEST_MAP_STR = (
    '....#.....\n'
    '.........#\n'
    '..........\n'
    '..#.......\n'
    '.......#..\n'
    '..........\n'
    '.#..^.....\n'
    '........#.\n'
    '#.........\n'
    '......#...')


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        map_file = os.path.join(cls.test_dir, 'test_map.txt')
        with open(map_file, 'w') as f:
            f.write(_TEST_MAP_STR)
        cls._map_file = map_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_squares_visited = 41
        squares_visited = soln1.solve(self._map_file)
        self.assertEqual(expected_squares_visited, squares_visited)


if __name__ == '__main__':
    unittest.main()

