"""Test for solution for day 3 part 2."""

import unittest

import soln2


class TestSoln2(unittest.TestCase):

    def test_add_valid_multiplications_conditional(self) -> None:
        memory_str = ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]"
                      "(mul(11,8)undo()?mul(8,5))")
        prod_sum = 48
        calculated_solution = soln2.add_valid_multiplications(memory_str)
        self.assertEqual(prod_sum, calculated_solution)

    def test_add_valid_multiplications_unconditional(self) -> None:
        memory_str = ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]"
                      "(mul(11,8)undo()?mul(8,5))")
        prod_sum = 161
        calculated_solution = soln2.add_valid_multiplications(
            memory_str, parse_conditionals=False)
        self.assertEqual(prod_sum, calculated_solution)


if __name__ == '__main__':
    unittest.main()
