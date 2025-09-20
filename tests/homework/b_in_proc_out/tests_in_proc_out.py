
import unittest
from src.homework.b_in_proc_out.output import get_sales_tax_amount, get_tip_amount, TAX_RATE

class TestRestaurantBill(unittest.TestCase):
    def test_get_sales_tax_amount(self):
        self.assertAlmostEqual(get_sales_tax_amount(20), 20 * TAX_RATE, places=2)
        self.assertAlmostEqual(get_sales_tax_amount(0), 0.0, places=2)
        self.assertAlmostEqual(get_sales_tax_amount(100), 100 * TAX_RATE, places=2)

    def test_get_tip_amount(self):
        self.assertAlmostEqual(get_tip_amount(20, 0.15), 3.0, places=2)
        self.assertAlmostEqual(get_tip_amount(50, 0.20), 10.0, places=2)
        self.assertAlmostEqual(get_tip_amount(0, 0.10), 0.0, places=2)

