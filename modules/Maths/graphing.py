import numpy as np
import matplotlib.pyplot as plt
import json


def plot_function(func: function, domain: float) -> None:
    '''
    Initialise an array with all the x values representing the domain of the
    function that will be plotted. The 'scale" variable sets what the gap between
    values is for the ...
    '''
    scale = 0.01

    x = np.arange(-domain, domain, scale)
    y = np.array([func(val) for val in x])


    plt.plot(x, y)
    plt.show()


def interpret_function(func: str):
    operators = ["+", "-", "*", "/", "^"]

    for letter in func:
        if letter in operators:
            pass