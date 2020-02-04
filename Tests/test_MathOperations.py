import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(5, Addition.sum(1,4))

    def test_MathOperations_Subtraction(self):
        self.assertEqual(-3, Subtraction.subtract(1,4))

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3]

        self.assertEqual(6, Addition.sum(valueList))


if __name__ == '__main__':
    unittest.main()
