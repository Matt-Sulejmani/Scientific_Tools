import numpy as np
import matplotlib.pyplot as plt
import json

import Function

with open('Constants.json', "r") as f:
    const = json.load(f)


def plotFunction(function, domain: float):
    ## Create x-axis values
    x = np.arange(-domain, domain, 0.01)

    ## Create an array the same size as x with entirely zeroes
    ## This ensures that x and y have the same number of elements
    y = np.zeros(len(x), dtype=np.float32)

    ## This loops fills the y array with the f(x) values by using the x value at each index
    for index, value in enumerate(x):
        y[index] = function(value)

    ## Plots the x and y arrays
    plt.plot(x, y)
    plt.show()


def expandBinomial(expr, power: int):
    '''
        Find a way to unpack the expression
        
    '''
    pass