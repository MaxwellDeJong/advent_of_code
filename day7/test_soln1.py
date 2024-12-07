"""Test for solution for day 7 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

_TEST_NUMBERS_STR = (
    '190: 10 19\n'
    '3267: 81 40 27\n'
    '83: 17 5\n'
    '156: 15 6\n'
    '7290: 6 8 6 15\n'
    '161011: 16 10 13\n'
    '192: 17 8 14\n'
    '21037: 9 7 18 13\n'
    '292: 11 6 16 20')


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_numbers.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_NUMBERS_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_sum = 3749
        calculated_sum = soln1.solve(self._test_file)
        self.assertEqual(expected_sum, calculated_sum)


if __name__ == '__main__':
    unittest.main()

