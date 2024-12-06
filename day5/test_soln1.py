"""Test for solution for day 5 part 1."""

import os
import shutil
import tempfile
from typing import List
import unittest

import parameterized

import soln1

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


class TestSoln1(unittest.TestCase):

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

    @parameterized.parameterized.expand([
        ('valid_1', [75, 47, 61, 53, 29]),
        ('valid_2', [97, 61, 53, 29, 13]),
        ('valid_3', [75, 29, 13]),
        ('invalid_1', [75, 97, 47, 61, 53]),
        ('invalid_2', [61, 13, 29]),
        ('invalid_3', [97, 13, 75, 29, 47])])
    def test_validate_update(self, name: str, update: List[int]) -> None:
        invalid = 'invalid' in name
        order_rules = soln1.read_order_rules(self._rules_file)
        before_dict, after_dict = soln1.parse_order_rules(order_rules)
        validated = soln1.validate_update(update, before_dict, after_dict)
        self.assertNotEqual(invalid, validated)

    def test_solve(self) -> None:
        expected_sum = 143
        calculated_sum = soln1.solve(self._rules_file, self._updates_file)
        self.assertEqual(expected_sum, calculated_sum)


if __name__ == '__main__':
    unittest.main()

