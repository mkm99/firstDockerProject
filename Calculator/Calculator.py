'''
This program will create a calculator object which will have basic operations such as
addition, subtraction, multiplication, division, square root, and squared
'''

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.squareRoot import SquareRoot
from MathOperations.logarithm import Logarithm

class Calculator:

    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Subtract(self, a, b):
        self.Result = Subtraction.subtract(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

    def Division(self, a, b):
        self.Result = Division.division(a, b)
        return self.Result

    def Exponentiation(self, a, b):
        self.Result = Exponentiation.exponentiation(a, b)
        return self.Result

    def SquareRoot(self, a):
        # import the function sqrt from the math library
        # I am only importing sqrt because it is the only function I need
        from math import sqrt
        self.Result = SquareRoot.squareRoot(a)
        return self.Result

    def Logarithm(self, a, b):
        self.Result = Logarithm.logarithm(a, b)
        return self.Result


#test = Calculator()
#print(test.divide(2,0))