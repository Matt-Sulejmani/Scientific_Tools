import math
from Function import *

def expandBinomial(expr: str, power: int=1) -> str:
    ##* This splits the string input into sperate parts denoted by the x 
    ##? Currently a and b include the brackets
    ##! Could raise error if innapropriate input is provided
    a, b = expr.split("+")

    ##* Finding which term contains the x variable
    ##! Broken - Currently returns only a as being the xTerm even if both inputs contain x - issue
    if a.find("x") and not b.find("x"):
        xTerm = a
    elif a.find("x") and b.find("x"):
        xTerm = a + b
    else:
        xTerm = b

    a = a.replace("(", "")

    ##! Sigma function - Incomplete - Need to define function class
    sigma(0, power)

    print(a)

'''
    The sigma function takes a strat and end point as inputs giving it the range for which to iterate over
    The other input includes a function defined elsewhere in the code (Inputting a function is optional)
    It then returns the sum of the values of the function (sigma notation step)'''
def sigma(startIndex:int, endIndex:int, function=None) -> float:
    ##* Intialise a sum at 0
    summation = 0

    ##* The 'for loop' that iterates over the provided interval (starting and ending point)
    for n in range(startIndex, endIndex+1):
        ##* Checks to see if a function was provided and breaks the loop if it wasn't (doesn't check whether function is valid)
        if function:
            ##* Here the sigma function keeps track of the sum for each term of the provided function
            summation += function(n)

        else:
            break

    ## Returns the final sum or 0 if no function was inputted
    return summation

'''
    Binomial expansion formula

    Sigma from k=0 to n
    nCk * X **n * b** n-k

    This would return a string
    I could get a string input (expression) - A function class would be better
    Split the expression and get the required information

'''

func = Function("polynomial")
print(sigma(1, 10))