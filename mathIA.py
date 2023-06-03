'''
    Graphing and calculations for the mathematics IA
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy
import math


'''
    # Labellign digrams
'''

x = np.arange(-10, 10, 0.01, dtype=np.float32)

y = np.sign(np.cos(x))

plt.plot(x, y)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude/ f(t)")
plt.title("Square wave function")

plt.grid(True)

plt.show()