"""Test for solution for day 8 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

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


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_antenna_map.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_ANTENNA_MAP_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_antinodes = 14
        calculated_antinodes = soln1.solve(self._test_file)
        self.assertEqual(expected_antinodes, calculated_antinodes)


if __name__ == '__main__':
    unittest.main()

