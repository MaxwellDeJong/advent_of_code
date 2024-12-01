# Simple test for AoC day 1 solution.
import os
import shutil
import tempfile
from typing import List
import unittest

import parameterized

import extract_numbers


def _create_test_file(
        list1: List[int],
        list2: List[int],
        test_file: str,
        number_spaces: int = 4) -> str:
    if number_spaces:
        separator = ' ' * number_spaces
    else:
        separator = '\t'
    with open(test_file, 'w') as f:
        for loc_id1, loc_id2 in zip(list1, list2):
            line = f'{loc_id1}{separator}{loc_id2}'
            f.write(f'{loc_id1}{separator}{loc_id2}\n')


class TestExtractNumbers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    @parameterized.parameterized.expand([
        ('2_spaces', 2),
        ('4_spaces', 4),
        ('tab', 0)])
    def test_extract_numbers(self, name: str, number_spaces: int) -> None:
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        test_file = os.path.join(self.test_dir, f'{name}.txt')
        _create_test_file(list1, list2, test_file, number_spaces)
        extracted_list1, extracted_list2 = extract_numbers.extract_numbers(
            test_file)
        self.assertEqual(list1, extracted_list1)
        self.assertEqual(list2, extracted_list2)


if __name__ == '__main__':
    unittest.main()
