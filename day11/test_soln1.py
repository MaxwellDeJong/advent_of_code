"""Test for solution for day 11 part 1."""

import os
import shutil
import tempfile
import unittest

import parameterized

import soln1

_TEST_STONES_STR = '125 17'


class TestSoln1(unittest.TestCase):

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

    def test_evolve(self) -> None:
        stones = [125, 17]
        for _ in range(6):
            soln1.evolve_stones(stones)
        expected_stones = [
            2097446912,
            14168,
            4048,
            2,
            0,
            2,
            4,
            40,
            48,
            2024,
            40,
            48,
            80,
            96,
            2,
            8,
            6,
            7,
            6,
            0,
            3,
            2]
        self.assertEqual(expected_stones, stones)

    @parameterized.parameterized.expand([
        ('small', 6, 22),
        ('large', 25, 55312)])
    def test_solve(
            self, name: str, iterations: int, expected_length: int) -> None:
        calculated_length = soln1.solve(
            self._test_file, n_iterations=iterations)
        self.assertEqual(expected_length, calculated_length)


if __name__ == '__main__':
    unittest.main()

