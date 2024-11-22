import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_bmi_normal(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_bmi_overweight(self):
        self.assertAlmostEqual(calculate_bmi(85, 1.75), 27.76, places=2)

    def test_bmi_underweight(self):
        self.assertAlmostEqual(calculate_bmi(50, 1.75), 16.33, places=2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)

if __name__ == "__main__":
    unittest.main()