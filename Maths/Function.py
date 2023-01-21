import numpy as np
import math
import json

with open("Constants.json", "r") as f:
    const = json.load(f)

class Function(object):
    def __init__(self, fType:str):
        self.type = fType.casefold()

        ## Assign a function type to the object
        self.setType(self.type)

    def __call__(self, exponent: float):

        ## This returns the function that will be called
        return self.exponential(exponent)

    def setType(self):
        if self.type == "polynomial":
            pass
        if self.type == "exponential":
            pass

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
    
    def exponential(self, exponent: float, base: float =const['e']):
        return math.pow(base, exponent)

def findOccurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]

