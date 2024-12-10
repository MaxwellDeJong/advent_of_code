"""Test for solution for day 9 part 1."""

import os
import shutil
import tempfile
import unittest

import soln1

_TEST_DISK_MAP_STR = '2333133121414131402'


class TestSoln1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        test_file = os.path.join(cls.test_dir, 'test_disk_map.txt')
        with open(test_file, 'w') as f:
            f.write(_TEST_DISK_MAP_STR)
        cls._test_file = test_file

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_solve(self) -> None:
        expected_checksum = 1928
        calculated_checksum = soln1.solve(self._test_file)
        self.assertEqual(expected_checksum, calculated_checksum)


if __name__ == '__main__':
    unittest.main()

