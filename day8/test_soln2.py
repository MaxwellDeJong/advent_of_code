"""Test for solution for day 8 part 2."""

import os
import shutil
import tempfile
import unittest

import soln2

_SIMPLE_ANTENNA_MAP_STR = (
    'T.........\n'
    '...T......\n'
    '.T........\n'
    '..........\n'
    '..........\n'
    '..........\n'
    '..........\n'
    '..........\n'
    '..........\n'
    '..........')

_TEST_ANTENNA_MAP_STR = (
    '............\n'
    '........0...\n'
    '.....0......\n'
    '.......0....\n'
    '....0.......\n'
    '......A.....\n'
    '............\n'
    '............\n'
    '........A...\n'
    '.........A..\n'
    '............\n'
    '............')


class TestSoln2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        simple_file = os.path.join(cls.test_dir, 'simple_antenna_map.txt')
        with open(simple_file, 'w') as f:
            f.write(_SIMPLE_ANTENNA_MAP_STR)
        cls._simple_file = simple_file

        test_file = os.path.join(cls.test_dir, 'test_antenna_map.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_ANTENNA_MAP_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve_simple(self) -> None:
        expected_antinodes = 9
        calculated_antinodes = soln2.solve(self._simple_file)
        self.assertEqual(expected_antinodes, calculated_antinodes)

    def test_solve(self) -> None:
        expected_antinodes = 34
        calculated_antinodes = soln2.solve(self._test_file)
        self.assertEqual(expected_antinodes, calculated_antinodes)


if __name__ == '__main__':
    unittest.main()

