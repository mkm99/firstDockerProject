import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calculator_return_Sum(self):
        calculator = Calculator()
        result = calculator.Sum(2, 2)
        self.assertEqual(4, result)

    def test_calculator_return_Subtract(self):
        calculator = Calculator()
        result = calculator.Subtract(10, 5)
        self.assertEqual(5, result)

    def test_calculator_access_addition_result(self):
        calculator = Calculator()
        calculator.Sum(5, 5)
        self.assertEqual(10, calculator.Result)

    def test_calculator_access_subtract_result(self):
        calculator = Calculator()
        calculator.Subtract(10, 5)
        self.assertEqual(5, calculator.Result)

    def test_calculator_multiplication(self):
        calculator = Calculator()
        result = calculator.Multiplication(2, 3)
        self.assertEqual(6, result)

    def test_calculator_access_multiplication_result(self):
        calculator = Calculator()
        calculator.Multiplication(2, 4)
        self.assertEqual(8, calculator.Result)

    '''    
    def test_calculator_divisionByZero(self):
        calculator = Calculator()
        result = calculator.divide(10, 0)
        self.assertEqual("E", result)

    def test_calculator_access_divison_by_0(self):
        calculator = Calculator()
        calculator.Division(5, 0)
        self.assertEqual("E", calculator.Result)
    '''

    def test_calculator_division(self):
        calculator = Calculator()
        result = calculator.Division(10, 2)
        self.assertEqual(5, result)

    def test_calculator_access_division(self):
        calculator = Calculator()
        calculator.Division(14, 7)
        self.assertEqual(2, calculator.Result)

    def test_calculator_exponentiation(self):
        calculator = Calculator()
        result = calculator.Exponentiation(3, 2)
        self.assertEqual(9, result)

    def test_calculator_access_exponentiation(self):
        calculator = Calculator()
        calculator.Exponentiation(2, 3)
        self.assertEqual(8, calculator.Result)

    def test_calculator_sqRoot(self):
        calculator = Calculator()
        result = calculator.SquareRoot(16)
        self.assertEqual(4, result)

    def test_calculator_access_sqRoot(self):
        calculator = Calculator()
        calculator.SquareRoot(9)
        self.assertEqual(3, calculator.Result)


if __name__ == '__main__':
    unittest.main()