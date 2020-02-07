import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.squareRoot import SquareRoot
from MathOperations.logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(5, Addition.sum(1,4))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-3, Subtraction.subtract(1,4))

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3]
        self.assertEqual(6, Addition.sum(valueList))

    def test_MathOperations_Multiplication(self):
        self.assertEqual(24, Multiplication.multiplication(3,8))

    def test_MathOperations_Division(self):
        self.assertEqual(5, Division.division(35,7))

    def test_MathOperations_Exponentiation(self):
        self.assertEqual(27, Exponentiation.exponentiation(3,3))

    def test_MathOperations_SquareRoot(self):
        self.assertEqual(5, SquareRoot.squareRoot(25))

    def test_MathOperations_Logarithm(self):
        self.assertEqual(3, Logarithm.logarithm(729, 9))

if __name__ == '__main__':
    unittest.main()
