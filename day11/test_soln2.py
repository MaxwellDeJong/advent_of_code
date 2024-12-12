"""Test for solution for day 11 part 2."""

import os
import shutil
import tempfile
import unittest

import soln2

_TEST_STONES_STR = '125 17'


class TestSoln2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_stones.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_STONES_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_length = 65601038650482
        calculated_length = soln2.solve(self._test_file)
        self.assertEqual(expected_length, calculated_length)


if __name__ == '__main__':
    unittest.main()

