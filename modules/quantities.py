# Standard library imports (Python 3.12)
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List
from numbers import Real

# Dependencies
import numpy as np

# Custom module imports
from exceptions import IncompatibleUnits, InvalidVectorArithemtic
from units import *


# TODO - Vector class documentation (review)
# TODO - Vector dot, cross and scalar multiplication
# TODO - Review Quantity class and arithmetic operations
# TODO - Write tests
# TODO - Write automated logs/ custom exceptions



class Vector:
    """Vector Class"""
    def __init__(self, 
                 position: List[Real, Real, Real]=[0, 0, 0]) -> None:
        """

        Args:
            position (List[Real, Real, Real], optional): 
            The position arguments take in a list of x, y, z values in order to 
            represent the vector. 
            Defaults to [0, 0, 0].
        """
        self.position = np.array(position, np.float32)
        self.x, self.y, self.z = iter(position)                       
    
    @staticmethod
    def is_vector(arg: Any) -> None:
        """
        This function checks if the argument passed in is a vector or not.

        Args:
            argument (Any): The argument that gets type checked

        Raises:
            InvalidVectorArithemtic: The function raises an Invalid Vector 
            Arithmetic exception when the argument passed in is not an instance
            of a vector class

        Returns:
            None: If the argument is a vector then the function 
            returns None.
        """
        try:
            if not isinstance(arg, Vector):
                raise InvalidVectorArithemtic
            
        except InvalidVectorArithemtic:
            raise InvalidVectorArithemtic("Attempted arithmetic between vector and non-vector types")
        
        return None

    def __str__(self) -> str:
        """
        Returns:
            str: The value that gets printed when print is called on an intance
            of the class
        """
        return f'{self.position}'

    
    def __add__(self, other: Vector) -> Vector:
        """
        This function defines how two vector quantities are added to each other.

        Args:
            other (Vector): The second vector value that gets added

        Returns:
            Vector: The result of the vector addition
        """
        self.is_vector(other)
        return Vector(np.add(self.position, other.position))


    def __sub__(self, other: Vector) -> Vector:
        """
        This function defines how two vector quantities are subtracted from each 
        other.

        Args:
            other (Vector): The vector that gets subtracted from self

        Returns:
            Vector: The result of the vector subtraction
        """
        self.is_vector(other)
        return Vector(np.subtract(self.position, other.position))
    

    def __mul__(self, other: Vector) -> Vector:
        # Vector cross multiplication
        pass

    def __rmul__(self, other: Real) -> Real:
        # Vector dot multiplication
        pass



@dataclass(slots=True)
class Quantity:
    value: Real
    units: standard_unit|derived_unit                             
    direction: Vector = field(default=Vector())                     

    def __str__(self) -> str:
        """
        Returns:
            str: The value that gets used when an instance is printed 
        """
        return f"{self.value}{self.units}"
    
    
    def check_units(self, other: Any) -> None:
        """
        This function checks if the argument passed in is of the correct type 
        and has the correct units in order to perform the desired calculations

        Args:
            other (Any): The value whose type and units are being checked

        Raises:
            TypeError: If the argument is not of type (Quantity) then the 
            function raises a type error 
            IncompatibleUnits: If the argument is of type (Quantity) but does
            not have the same units as self then an Incompatible Units error is 
            raised

        Returns:
            None: If both the type and units of the argument are ok then the
            function returns None
        """
        try:
            if not isinstance(other, Quantity):
                raise TypeError
            
            if other.units != self.units:
                raise IncompatibleUnits
            
        except TypeError:
            return NotImplemented
        
        except IncompatibleUnits as error:
            raise error("Attempted additon of two quantities with incompatible units")

        return None

    
    ##? Dunder methods that get called when arithmetic operators are used
    def __add__(self, other: Vector) -> Vector:
        """
        The addtion function that gets called when a "+" operator is used. This 
        function defines the behaviour of the addition of 2 quantities and
        retuns the sum of the operation as a new quantity instance.

        For the in-place operation see self.__iadd__

        Args:
            other (Vector): The quantity to the right of the "+" operator

        Returns:
            Vector: The sum of the two Quantity instances
        """
        self.check_units(other)
        
        mag = self.magnitude + other.magnitude          #* Temporary variable to store the result of magnitude addition
        vec = self.direction + other.direction          #* Temporary variable to store the vector addition
        
        return Quantity(mag, self.units, vec)

    
    def __sub__(self, other: Vector) -> Vector:
        self.check_units(other)
        
        mag = self.magnitude - other.magnitude          #* Temporary variable to store the result of magnitude subtraction
        vec = self.direction - other.direction          #* Temporary variable to store the vector subtraction
        
        return Quantity(mag, self.units, vec)
        
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






vec1 = Vector([1,2,3])
vec2 = Vector([3,4,5])

print(vec1-vec2)
print(type(vec1+vec2))
print(vec1)
print()