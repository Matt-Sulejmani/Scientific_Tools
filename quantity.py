# System and standard library imports
from sys import getsizeof
import array

# Package imports

from exceptions import *


# Defining types
Vector = list[int | float]


class Quantity(object):
    def __init__(self, magnitude: int | float, units: str, 
                 direction: Vector=[0, 0,0], unitPow: int = 1, qType: str = ''):

        # Properties of a quantity
        self.magnitude = magnitude 
        self.direction = array.array('d', direction)
        self.unitPow = unitPow
        self.units = f'{units}{self.unitPow}'
        self.qType = qType
        self._memSize = getsizeof(self)

    # Arithmetic operation definitions/ behaviour
    def __repr__(self):
        return  f" Type: {self.qType}\n Memory size: {self._memSize} \
        \n Magnitude: {self.magnitude} \n Direction: {self.direction}\n"
    
    def _validate(self, other):
        return self.units == other.units
    
    # Methods that a recalled when operating with other quantities
    def __add__(self, other):
        try:
            if not self._validate(other):
                raise MismatchedUnits
            magResult = self.magnitude + other.magnitude
            directionResult = array.array('d', [(i + j) for i,j in self.direction and other.direction])

            return Quantity(magResult, self.units, directionResult)
        
        except MismatchedUnits:
            # log smth
            return "Invalid units"

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

test = Quantity(10, "J", [3, 4, 5])
test1 = Quantity(10, "J")

print(test + test1)