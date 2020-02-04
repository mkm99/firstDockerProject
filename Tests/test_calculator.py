import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()

        self.assertIsInstance(calculator, Calculator)

    def test_calculator_add(self):
        calculator = Calculator()
        result = calculator.add(5, 5)
        self.assertEqual(10, result)

    def test_calculator_minus(self):
        calculator = Calculator()
        result = calculator.subtract(10 , 5)
        self.assertEqual(5, result)

    def test_calculator_times(self):
        calculator = Calculator()
        result = calculator.multiply(2, 3)
        self.assertEqual(6, result)

    def test_calculator_divisionByZero(self):
        calculator = Calculator()
        result = calculator.divide(10, 0)
        self.assertEqual("You are funny, no division by 0!", result)

    def test_calculator_division2(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        self.assertEqual(5, result)

    def test_calculator_square(self):
        calculator = Calculator()
        result = calculator.square(3)
        self.assertEqual(9, result)

    def test_calculator_sqRoot(self):
        calculator = Calculator()
        result = calculator.squareRoot(16)
        self.assertEqual(4, result)



if __name__ == '__main__':
    unittest.main()
