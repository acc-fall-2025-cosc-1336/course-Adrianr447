import unittest
import os
import sys

# Ensure this folder is on sys.path so tests can import output.py directly
sys.path.insert(0, os.path.dirname(__file__))

from output import get_sales_tax_amount, get_tip_amount, TAX_RATE, multiply_numbers

class TestOutput(unittest.TestCase):
    def test_sales_tax(self):
        self.assertAlmostEqual(get_sales_tax_amount(100.0), 100.0 * TAX_RATE)

    def test_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(50.0, 0.2), 10.0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)

    def test_zero_values(self):
        self.assertAlmostEqual(get_sales_tax_amount(0.0), 0.0)
        self.assertAlmostEqual(get_tip_amount(0.0, 0.15), 0.0)

if __name__ == "__main__":
    unittest.main()