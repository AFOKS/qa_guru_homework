import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("\nПодготовка теста")
        self.calc = Calculator()

    def tearDown(self):
        print("Завершение теста")

    def test_add(self):
        result = self.calc.add(5, 3)

        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)

        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calc.multiply(6, 7)

        self.assertEqual(result, 42)

    def test_divide(self):
        result = self.calc.divide(20, 5)

        self.assertEqual(result, 4)

    def test_divide_by_zero(self):

        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_positive_result(self):
        result = self.calc.add(2, 2)

        self.assertTrue(result > 0)