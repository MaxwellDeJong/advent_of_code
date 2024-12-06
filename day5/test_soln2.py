"""Test for solution for day 5 part 2."""

import os
import shutil
import tempfile
from typing import List
import unittest

import parameterized

import soln2

_TEST_RULES_STR = (
    '47|53\n'
    '97|13\n'
    '97|61\n'
    '97|47\n'
    '75|29\n'
    '61|13\n'
    '75|53\n'
    '29|13\n'
    '97|29\n'
    '53|29\n'
    '61|53\n'
    '97|53\n'
    '61|29\n'
    '47|13\n'
    '75|47\n'
    '97|75\n'
    '47|61\n'
    '75|61\n'
    '47|29\n'
    '75|13\n'
    '53|13')

_TEST_UPDATES_STR = (
    '75,47,61,53,29\n'
    '97,61,53,29,13\n'
    '75,29,13\n'
    '75,97,47,61,53\n'
    '61,13,29\n'
    '97,13,75,29,47')


class TestSoln2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        rules_file = os.path.join(cls.test_dir, 'test_rules.txt')
        with open(rules_file, 'w') as f:
            f.write(_TEST_RULES_STR)
        cls._rules_file = rules_file

        updates_file = os.path.join(cls.test_dir, 'test_updates.txt')
        with open(updates_file, 'w') as f:
            f.write(_TEST_UPDATES_STR)
        cls._updates_file = updates_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_sum = 123
        calculated_sum = soln2.solve(self._rules_file, self._updates_file)
        self.assertEqual(expected_sum, calculated_sum)


if __name__ == '__main__':
    unittest.main()

