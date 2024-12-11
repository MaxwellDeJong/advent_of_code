"""Test for solution for day 10 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

_TEST_TRAILHEAD_MAP_STR = (
    '89010123\n'
    '78121874\n'
    '87430965\n'
    '96549874\n'
    '45678903\n'
    '32019012\n'
    '01329801\n'
    '10456732')


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_trail_map.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_TRAILHEAD_MAP_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_score = 36
        calculated_score = soln1.solve(self._test_file)
        self.assertEqual(expected_score, calculated_score)


if __name__ == '__main__':
    unittest.main()

