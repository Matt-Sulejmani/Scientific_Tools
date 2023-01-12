import numpy as np

class Function(object):
    def __init__(self, fType:str):
        self.type = fType.casefold()

    def setType(self):
        if self.type == "polynomial":
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
    
    def exponential(self, base, exponent):
        pass

def findOccurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]

func = Function("polynomial").polynomial(7, [0, 1, 2, 0, 0, 5, 6])
x = 5
print()

