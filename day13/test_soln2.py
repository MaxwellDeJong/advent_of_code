"""Test for solution for day 13 part 2."""

import os
import shutil
import tempfile
import unittest

import soln2

_TEST_RULES_STR = (
    'Button A: X+94, Y+34\n'
    'Button B: X+22, Y+67\n'
    'Prize: X=8400, Y=5400\n'
    '\n'
    'Button A: X+26, Y+66\n'
    'Button B: X+67, Y+21\n'
    'Prize: X=12748, Y=12176\n'
    '\n'
    'Button A: X+17, Y+86\n'
    'Button B: X+84, Y+37\n'
    'Prize: X=7870, Y=6450\n'
    '\n'
    'Button A: X+69, Y+23\n'
    'Button B: X+27, Y+71\n'
    'Prize: X=18641, Y=10279')


class TestSoln2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_rules.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_RULES_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_token_cost = 875318608908
        calculated_token_cost = soln2.solve(self._test_file)
        self.assertEqual(expected_token_cost, calculated_token_cost)


if __name__ == '__main__':
    unittest.main()

