'''
This program will create a calculator object which will have basic operations such as
addition, subtraction, multiplication, division, square root, and squared
'''

class Calculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # make sure the second number is not a zero, otherwise return a string with error message
        if b != 0:
            return a / b
        else:
            return "You are funny, no division by 0!"

    def square(self, a):
        return a ** 2

    def squareRoot(self, a):
        # import the function sqrt from the math library
        # I am only importing sqrt because it is the only function I need
        from math import sqrt
        return sqrt(a)


test = Calculator()
print(test.add(45,5))