import unittest
from src.homework.b_in_proc_out.output import multiply_numbers, get_sales_tax_amount, get_tip_amount, TAX_RATE

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

class TestSalesTaxAndTip(unittest.TestCase):
    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(20), 20 * TAX_RATE, places=6)
        self.assertAlmostEqual(get_sales_tax_amount(0), 0.0, places=6)
        self.assertAlmostEqual(get_sales_tax_amount(100), 100 * TAX_RATE, places=6)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(20, 0.15), 3.0, places=6)
        self.assertAlmostEqual(get_tip_amount(50, 0.2), 10.0, places=6)
        self.assertAlmostEqual(get_tip_amount(0, 0.2), 0.0, places=6)

if __name__ == "__main__":
    unittest.main()