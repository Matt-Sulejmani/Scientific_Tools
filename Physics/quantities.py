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


@dataclass(slots=True)
class Quantity:
    ##? Qunatity attributes 
    magnitude: float
    units: str                      #* Units for given qunatity
    unitsPow: int = 1               #* The power of the unit (m^2, m^3, s^-1)
    direction: Vector = field(default_factory=Vector)       #* Direction vector of the class
    
    ##? Dunder methods that get called when arithmetic operators are used
    def __add__(self, other) -> float:
        try:
            ## If the units are incorrect the addition cannot happen -> Units should be converted
            if self.units != other.units:
                return "Incorrect units"

            mag = self.magnitude + other.magnitude          #* Temporary variable to store the result of magnitude addition
            vec = self.direction + other.direction          #* Temporary variable to store the vector addition
            
            return Quantity(mag, self.units, direction=vec)
        
        except:
            return NotImplemented
    
    def __radd__(self, other) -> float:
        try:
            return self.magnitude + other
            
        except:
            return NotImplemented
    
    def __sub__(self, other) -> float:
        try:
            return self.magnitude - other.magnitude 
        
        except:
            return NotImplemented
    
    def __rsub__(self, other) -> float:
        try:
            return other - self.magnitude
            
        except:
            return NotImplemented
        
    def __mul__(self, other) -> float:
        try:
            #! Missing direction
            self.magnitude *= other.magnitude
            self.unitsPow += other.unitsPow
            self.units = f'{self.units}^{self.unitsPow}'

            return ...
        
        except:
            return NotImplemented
        


q = Quantity(10, 'J', direction=Vector([1, 2, 3]))
q1 = Quantity(20, 'J', direction=Vector([2, 3, 4]))
q2 = Quantity(30, 'J')

print(q + q1)

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