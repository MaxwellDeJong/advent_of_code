"""Test for solution for day 14 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

_TEST_RULES_STR = (
    'p=0,4 v=3,-3\n'
    'p=6,3 v=-1,-3\n'
    'p=10,3 v=-1,2\n'
    'p=2,0 v=2,-1\n'
    'p=0,0 v=1,3\n'
    'p=3,0 v=-2,-2\n'
    'p=7,6 v=-1,-3\n'
    'p=3,0 v=-1,-2\n'
    'p=9,3 v=2,3\n'
    'p=7,3 v=-1,2\n'
    'p=2,4 v=2,-3\n'
    'p=9,5 v=-3,-3')


class TestSoln1(unittest.TestCase):

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
        expected_safety_factor = 12
        calculated_safety_factor = soln1.solve(
            self._test_file, 11, 7)
        self.assertEqual(expected_safety_factor, calculated_safety_factor)


if __name__ == '__main__':
    unittest.main()

