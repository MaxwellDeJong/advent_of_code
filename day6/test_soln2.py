"""Test for solution for day 6 part 2."""

import os
import shutil
import tempfile
import unittest

import soln2

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


class TestSoln2(unittest.TestCase):

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
        expected_valid_obstacle_positions = 6
        valid_obstacle_positions = soln2.solve(self._map_file)
        self.assertEqual(
            expected_valid_obstacle_positions, valid_obstacle_positions)


if __name__ == '__main__':
    unittest.main()

