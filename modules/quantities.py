from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List
from numbers import Real

import numpy as np

from units import *



class InvalidVectorArithemtic(Exception): pass
class IncompatibleUnits(Exception): pass


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
    def is_vector(argument: Any) -> None:
        """
        This function checks if the argument passed in is a vector or not.

        Args:
            argument (Any): The argument that gets type checked

        Raises:
            TypeError: If the argument passed in was not of type (Vector)
            then the function raises a TypeError.

        Returns:
            None: If the argument is a vector then the function returns None.
        """
        if type(argument) != Vector:
            raise TypeError
        
        return None

    def __repr__(self) -> str:
        return f'{self.position}'

    
    def __add__(self, other: Vector) -> Vector:
        """
        This function defines how two vector quantities are added to each other.

        Args:
            other (Vector): The second vector value that gets added

        Raises:
            InvalidVectorArithemtic: This error is raised when an invalid 
            operation was attempted. 

        Returns:
            Vector: The result of the vector addition
        """
        try:
            self.is_vector(other)
            return Vector(np.add(self.position, other.position))

        except TypeError:
            return InvalidVectorArithemtic("Attempted arithmetic between vector and non-vector types")
        
        except:
            return InvalidVectorArithemtic("Invalid vector arithmetic was attempted")

    
    def __sub__(self, other: Vector) -> Vector:
        """
        This function defines how two vector quantities are subtracted from each 
        other.

        Args:
            other (Vector): The vector that gets subtracted from self

        Raises:
            InvalidVectorArithemtic: This error is raised when an invalid 
            operation was attempted. 

        Returns:
            Vector: The result of the vector subtraction
        """
        try:
            self.is_vector(other)
            return Vector(np.subtract(self.position, other.position))

        except TypeError:
            return InvalidVectorArithemtic("Attempted arithmetic between vector and non-vector types")
        
        except:
            return InvalidVectorArithemtic("Invalid vector arithmetic was attempted")
    
    def __mul__(self, other: Vector) -> Vector:

        pass

    def __rmul__(self, other: Real) -> Real:
        pass



@dataclass(slots=True)
class Quantity:
    
    value: Real
    units: standard_unit|derived_unit                             
    direction: Vector = field(default=Vector())                     

    def __str__(self) -> str:
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
        if type(other) != Quantity:
            raise TypeError
        
        if other.units != self.units:
            raise IncompatibleUnits

        return None

    
    ##? Dunder methods that get called when arithmetic operators are used
    def __add__(self, other):
        try:
            self.check_units(other)
            
            mag = self.magnitude + other.magnitude          #* Temporary variable to store the result of magnitude addition
            vec = self.direction + other.direction          #* Temporary variable to store the vector addition
            
            return Quantity(mag, self.units, direction=vec)
        
        except TypeError:
            raise 

        except IncompatibleUnits as error:
            raise error("Attempted additon of two quantities with incompatible units")
    
    def __sub__(self, other):
        try:
            self.check_units(other)
            
            mag = self.magnitude - other.magnitude          #* Temporary variable to store the result of magnitude subtraction
            vec = self.direction - other.direction          #* Temporary variable to store the vector subtraction
            
            return Quantity(mag, self.units, direction=vec)
        
        except TypeError:
            return NotImplemented
        
        except IncompatibleUnits as error:
            raise error("")
        
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
print(type(vec1-vec2))
print(vec1-5)
print()