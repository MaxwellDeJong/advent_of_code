"""Test for solution for day 12 part 1."""

import os
import shutil
import tempfile
import unittest

import parameterized

import soln1

_TEST_MAP1_STR = (
    'AAAA\n'
    'BBCD\n'
    'BBCC\n'
    'EEEC')

_TEST_MAP2_STR = (
    'OOOOO\n'
    'OXOXO\n'
    'OOOOO\n'
    'OXOXO\n'
    'OOOOO')

_TEST_MAP3_STR = (
    'RRRRIICCFF\n'
    'RRRRIICCCF\n'
    'VVRRRCCFFF\n'
    'VVRCCCJFFF\n'
    'VVVVCJJCFE\n'
    'VVIVCCJJEE\n'
    'VVIIICJJEE\n'
    'MIIIIIJJEE\n'
    'MIIISIJEEE\n'
    'MMMISSJEEE')


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()
        test_file1 = os.path.join(cls.test_dir, 'test_map1.txt')
        with open(test_file1, 'w') as f:
            f.write(_TEST_MAP1_STR)
        test_file2 = os.path.join(cls.test_dir, 'test_map2.txt')
        with open(test_file2, 'w') as f:
            f.write(_TEST_MAP2_STR)
        test_file3 = os.path.join(cls.test_dir, 'test_map3.txt')
        with open(test_file3, 'w') as f:
            f.write(_TEST_MAP3_STR)

        cls._test_file_dict = {
            1: test_file1,
            2: test_file2,
            3: test_file3}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    @parameterized.parameterized.expand([
        ('small', 1, 140),
        ('medium', 2, 772),
        ('large', 3, 1930)])
    def test_solve(
            self, name: str, file_key: int, expected_cost: int) -> None:
        test_file = self._test_file_dict[file_key]
        calculated_cost = soln1.solve(test_file)
        self.assertEqual(expected_cost, calculated_cost)


if __name__ == '__main__':
    unittest.main()

