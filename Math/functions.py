import numpy as np
import matplotlib.pyplot as plt


def plotFunction(function, domain: float):
    
    x = np.arange(-domain, domain, 0.01)
    y = function(x)

    plt.plot(x, y)
    plt.show()


def expandBinomial(expr, power: int):
    '''
        Find a way to unpack the expression
        
    '''
    pass