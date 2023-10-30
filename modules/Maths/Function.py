import numpy as np
import math
from fractions import Fraction
import json

with open("Constants.json", "r") as f:
    const = json.load(f)


class Function(object):
    def polynomial(self, power:int, coefficients: list) -> str:
        if power != len(coefficients):
            ## Fail case - error handling
            return "Invalid - The number of polynomial coefficients did not match the inputted power"
        
        polynomial = ""

        ## Redefines the input list as a numpy array
        coefficients = np.array(coefficients)

        ## Cycles through the coefficients
        for coefficient in coefficients:
            ## If the coefficient is non-zero it saves it
            if coefficient:
                polynomial += f"{coefficient}x^{power} +"
            
            ## Lowers the power of the x term by 1
            power -= 1
        
        return polynomial.removesuffix(" +")


'''
    An object made using the Exponential class contains the following information:
    - The base (acessed through object.base)
    - The exponent (acessed through object.exponent)
    - The numerical value (acessed through object())
'''

class Exponential(object):
    ## What happens when the variable is declared/ created
    def __init__(self, base: float =const['e'], exponent:float =1):
        self.base = base
        self.exponent = exponent

    ## What happens when varibale is called (baisically makes it like a function)
    def __call__(self):
        ## When the object is called it will return the numerical value 
        return math.pow(self.base, self.exponent)

    def derivative(self, order:int =1):
        pass


class Logarithmic(object):
    def __init__(self, base:float =const['e'], value:float =1):
        self.base = base
        self.value = value

    def __call__(self):
        pass


class Polynomial(object):
    def __init__(self, formula: str):
        self.formula: list = formula.replace(' ', '').split('+')         #* Standardise the input
        self.constTerm: float = 0.0

        for element in self.formula:
            if 'x' in element:
                pass

            self.constTerm += float(element)




def findOccurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]


'''
Types of functions:
- Polynomial
- Logarithmic
- Exponential
- Trogonometric

Polynomials:
- They are sums of different powers of x (a collection of exponential terms of x). They have:
1.Terms consisting of variables
2.A power ascoitated to each term

powers can be stored on a list.
To obtain a numerical value (in graphing) you could substitue the variable and raise it to the given powers
How to save expression? (string format)
'''

'''
A function or expression is:
f(x) = x**2 + x + 1
y - 1 = x**2 + x

'''
#! Problem 1 - Standardize expressions

print('x**2 + x + 1 + 5 + 3'.replace(' ', '').split('+'))

