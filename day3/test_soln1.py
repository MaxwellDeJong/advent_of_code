"""Test for solution for day 3 part 1."""

import unittest

import soln1


class TestSoln1(unittest.TestCase):

    def test_add_valid_multiplications(self) -> None:
        memory_str = ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then"
                      "(mul(11,8)mul(8,5))")
        prod_sum = 161
        calculated_solution = soln1.add_valid_multiplications(memory_str)
        self.assertEqual(prod_sum, calculated_solution)


if __name__ == '__main__':
    unittest.main()
