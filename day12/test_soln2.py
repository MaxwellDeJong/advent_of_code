"""Test for solution for day 12 part 2."""

import os
import shutil
import tempfile
import unittest

import parameterized

import soln2

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
    'EEEEE\n'
    'EXXXX\n'
    'EEEEE\n'
    'EXXXX\n'
    'EEEEE')

_TEST_MAP4_STR = (
    'AAAAAA\n'
    'AAABBA\n'
    'AAABBA\n'
    'ABBAAA\n'
    'ABBAAA\n'
    'AAAAAA')

_TEST_MAP5_STR = (
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


class TestSoln2(unittest.TestCase):

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
        test_file4 = os.path.join(cls.test_dir, 'test_map4.txt')
        with open(test_file4, 'w') as f:
            f.write(_TEST_MAP4_STR)
        test_file5 = os.path.join(cls.test_dir, 'test_map5.txt')
        with open(test_file5, 'w') as f:
            f.write(_TEST_MAP5_STR)

        cls._test_file_dict = {
            1: test_file1,
            2: test_file2,
            3: test_file3,
            4: test_file4,
            5: test_file5}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    @parameterized.parameterized.expand([
        ('small', 1, 80),
        ('medium', 2, 436),
        ('E-shape', 3, 236),
        ('touching', 4, 368),
        ('large', 5, 1206)])
    def test_solve(
            self, name: str, file_key: int, expected_cost: int) -> None:
        test_file = self._test_file_dict[file_key]
        calculated_cost = soln2.solve(test_file)
        self.assertEqual(expected_cost, calculated_cost)


if __name__ == '__main__':
    unittest.main()

