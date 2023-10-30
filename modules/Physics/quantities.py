# Standard library imports
from dataclasses import dataclass, field
import numpy as np

#! Optime by using slots or dataclasses
class Vector:
    def __init__(self, position: np.ndarray=np.array([0, 0, 0], np.float32)):
        self.position = np.array(position, np.float32)
        # self.x, self.y, self.z = iter(position)                       #* Iterate over the position vector to store specific (x, y, z) values

    def __repr__(self) -> str:
        return f'{self.position}'                                       #* What gets printed when the class is passed in the print function
    
    def __add__(self, other):
        try:
            return Vector(np.add(self.position, other.position))        #* Returns a new vector with the coordinates from the vector addition

        except:
            return NotImplemented
    
    def __sub__(self, other):
        try:
            return Vector(np.subtract(self.position, other.position))   #* Returns a new vector with the coordinates from the vector subtraction

        except:
            return NotImplemented


@dataclass(slots=True)
class Quantity:
    ##? Qunatity attributes 
    magnitude: int|float
    units: str                      #* Units for given qunatity
    dimensions: int = field(default=np.int8(1), repr=False)       #* The power of the unit (m^2, m^3, s^-1)
    direction: Vector|list[int|float] = field(default=Vector())                     #* Direction vector of the class    #! Arguments passed in need to be Vector classes

    def convert(self, targetUnit: str):
        return NotImplementedError
    
    def __repr__(self):
        return NotImplementedError
    
    ##? Dunder methods that get called when arithmetic operators are used
    def __add__(self, other):
        try:
            ## If the units are incorrect the addition cannot happen -> Units should be converted
            if self.units != other.units:
                return "Incorrect units"
            
            mag = self.magnitude + other.magnitude          #* Temporary variable to store the result of magnitude addition
            vec = self.direction + other.direction          #* Temporary variable to store the vector addition
            
            return Quantity(mag, self.units, direction=vec)
        
        except:
            return NotImplemented
    
    def __sub__(self, other):
        try:
            ## If the units are incorrect the operation cannot happen -> Units should be converted
            if self.units != other.units:
                return "Incorrect units"
            
            mag = self.magnitude - other.magnitude          #* Temporary variable to store the result of magnitude subtraction
            vec = self.direction - other.direction          #* Temporary variable to store the vector subtraction
            
            return Quantity(mag, self.units, direction=vec)
        
        except:
            return NotImplemented
        
    def __radd__(self, other):
        try:
            return self.magnitude + other                  #* What gets called when a numeric quantity is adde with the quantity
            
        except:
            return NotImplemented
    
    def __rsub__(self, other):
        try:
            return other - self.magnitude
            
        except:
            return NotImplemented
        
    def __mul__(self, other):
        try:
            #! Missing direction
            self.magnitude *= other.magnitude
            self.unitsPow += other.unitsPow
            self.units = f'{self.units}^{self.unitsPow}'

            return ...
        
        except:
            return NotImplemented
    
    def __div__(self, other):
        return NotImplemented


def Add(*args: list[Quantity]) -> Quantity:
    myList = enumerate(args)
    print(myList)


def Subtract(*args: list[Quantity])-> Quantity:
    return NotImplementedError


def Multiply(*args: list[Quantity])-> Quantity:
    return NotImplementedError


def Divide(*args: list[Quantity])-> Quantity:
    return NotImplementedError


q = Quantity(10, 'J', direction=Vector([1, 2, 3]))
q1 = Quantity(20, 'J', direction=Vector([3, 2, 1]))
q2 = Quantity(30, 'J')

Add(q1, q, q2)

'''
Quantities:
- Mass
- Temperature
- Luminosity
- Distance
- Time
- Amount
- Current

Two scalar quantities can be added or subtracted (also multipled or divided if they are of the same type (mass, temp ...)

Two scalar quantities not of the same type can be multipled or divided to give new quantities (kg/ m s**2, N/ m**2)
'''