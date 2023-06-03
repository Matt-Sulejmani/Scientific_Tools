import numpy as np
import math
import json

with open("Constants.json", "r") as f:
    const = json.load(f)

class Function(object):
    def polynomial(self, power:int, coefficients: list) -> str:
        if power == len(coefficients):
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
        
        ## Fail case - error handling
        return "Invalid - The number of polynomial coefficients did not match the inputted power"


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
    def __init__(self, degree: int =1, coefficient:list =[]):
        self.degree = degree

    def __call__(self):
        pass



def findOccurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]



exponent = Exponential()
print(exponent())