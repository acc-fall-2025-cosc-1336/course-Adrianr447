import unittest
from src.homework.e_functions.value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):
    def test_gross_pay(self):
        self.assertAlmostEqual(get_gross_pay(40, 10), 400)
        self.assertAlmostEqual(get_gross_pay(45, 10), 475)
        self.assertAlmostEqual(get_gross_pay(30, 10), 300)
    def test_fica_tax(self):
        self.assertAlmostEqual(get_fica_tax(400), 30.6, places=2)
        self.assertAlmostEqual(get_fica_tax(475), 36.34, places=2)
        self.assertAlmostEqual(get_fica_tax(300), 22.95, places=2)
    def test_federal_tax(self):
        self.assertAlmostEqual(get_federal_tax(400), 32, places=2)
        self.assertAlmostEqual(get_federal_tax(475), 38, places=2)
        self.assertAlmostEqual(get_federal_tax(300), 24, places=2)

if __name__ == "__main__":
    unittest.main()