import unittest
from src.homework.b_in_proc_out.output import multiply_numbers

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(multiply_numbers(7, 7), 49)
        self.assertEqual(multiply_numbers(5, 5), 25)

    def test_multiply_zero(self):
        self.assertEqual(multiply_numbers(0, 10), 0)
        self.assertEqual(multiply_numbers(0, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(multiply_numbers(-3, 3), -9)
        self.assertEqual(multiply_numbers(-4, -2), 8)

if __name__ == "__main__":
    unittest.main()