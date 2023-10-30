import threading

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = [-1, 5]
y = [-1, 17]

fig, ax = plt.subplots()

ax.plot(x, y, color='green')


class Function(object):
    def __init__(self):
        self.domain = []
        self.fType = ''

    def graph(self):
        pass


class Polynomial(Function):
    def __init__(self, coefficients:list[int|float], degree:int):
        try:
            if coefficients.__len__ != degree:
                raise ValueError

            # Defining properties of a polynomial
            self.zeroes = []
            self.rZeroes = [y for y in self.zeroes if type(y) != complex]
            self.iZeroes = [y for y in self.zeroes if type(y) == complex]

            self.coefficients = coefficients
            self.degree = degree

        except ValueError:
            print()
    
    def __str__(self) -> str:
        return f"".join()
    

class Linear(Function):
    def __init__(self, gradient:int|float, yIntercept:int|float=0):
        self.gradient = gradient
        self.yIntercept = yIntercept