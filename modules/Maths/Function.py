# Standard library imports
from __future__ import annotations
from numbers import Rational, Real
from typing import  Any, Dict, List, Tuple, override


# Custom type aliases

type Point = Tuple[Real, Real]

# Custom exceptions
class RepeatedXValue(Exception): pass
class NumberTypeError(Exception): pass


# Base function class
class _Function:
    def __init__(self, *args: Point, func: function = None) -> None:
        self.points:    Dict[Real, Real] = {}
        self.domain:    List[Real] = []
        self.range:     List[Real] = []
        self.function:  function = func
        self.fType:     str = ''

        try:
            for x, y in iter(args):
                if x in self.points and self.points[x] != y:
                    raise RepeatedXValue
                
                self.points[x] = y
                self.domain.append(x)
                self.range.append(y)

        except RepeatedXValue:
            raise RepeatedXValue(f"x={x} is being related to multiple y values")


    def __call__(self, *args: Real) -> List[Real]:
        return [self.func(x) for x in args]
    
    @staticmethod
    def isReal(arg: Any) -> None:
        """
        Checks if the argument passed in is an instance of a Real number (int or
        float). If not then the function raises an exception.

        Args:
            arg (Any): The argument which gets type checked

        Raises:
            NumberTypeError: The exception raised when the argument is not a 
            float or int. Additionally, it displays the type of the argument
            that was passed in
            e: General exception
        """
        try:
            if not isinstance(arg, Real):
                raise TypeError
    
        except TypeError:
            raise NumberTypeError(f"Detected invalid argument type: {type(arg)}. Argument type must be int or float.")
        
        except Exception as e:
            raise e

    def graph(self):
        pass





class LinearFunc(_Function):
    """ A class representing a linear function - f(x) = mx + c """
    @override
    def __init__(self, *args: Point) -> None:
        super().__init__(*args, func=None)
        self.fType = "Linear"

        self._slope: Real = 0 
        self._yIntercept: Real = 0


    def add_points(self, *args: Point) -> None:
        '''Enter the points you want the function to remember in the format (x, y).
        All the points should be entered according to this format and separated
        by a comma.'''
        self.points.extend(args)


    def __str__(self) -> str:
        """
        Returns:
            str: Formatted string representation of the function formula
        """
        return f"f(x) = {self.slope}x {"+ " + str(self.yIntercept) if self.yIntercept >= 0 else self.yIntercept}"
    

    @property
    def slope(self) -> float:
        """
        Slope of the linear function, based on the list of data points provided 
        when creating the function itself. \n
        
        Formula: m = (y2 - y1) / (x2 - x1)

        Returns:
            float: Returns the slope as a float value
        """
        if self._slope:
            # Returns the existing slope value if there is one 
            return self._slope
    
        x1, x2 = self.domain[0], self.domain[-1]
        y1, y2 = self.points[x1], self.points[x2]
        self._slope =  (y2 - y1) / (x2 - x1)

        return self._slope

    @slope.setter
    def slope(self, slope_value: Real) -> None:
        """
        Set the value of the slope for the function instance manually.

        Args:
            slope_value (Real): The desired slope value as an int or float
        """
        self.isReal(slope_value)
        
        self._slope = slope_value 

    @property
    def yIntercept(self) -> Real:
        """
        Fomula: c = y1 - m * x1

        Returns:
            int|float: Returns the y-intercept (c)
        """
        if self._yIntercept:
            return self._yIntercept
        
        x = self.domain[0]
        y = self.points[x]
        
        return y - self.slope * x
    
    @yIntercept.setter
    def yIntercept(self, y_intercept: Real) -> None:
        """
        Set the value of the y-intercept for the function instance manually.

        Args:
            slope_value (Real): The desired y-intercept value as an int or float
        """
        self.isReal(y_intercept)
        
        self._yIntercept = y_intercept


    def calculate(self) -> None:
        self.range = [self._slope * x + self._yIntercept for x in self.domain]


    @override
    def __call__(self) -> None:
        pass





class Polynomial(_Function):
    """ A class representing a polynomial function - f(x) = ax^n + bx^(n-1) + ... """
    @override
    def __init__(self, *args: Point) -> None:
        super().__init__(*args)
        self.fType = "Polynomial"


    @property
    def degree(self) -> int:
        return 0
    


class PowerFunction(_Function):
    @override
    def __init__(self, power: int | Rational, *args: Point) -> None:
        super().__init__(*args)
        self.fType = "Power Fuction"

        self.power = power

    def __str__(self) -> str:
        return f"x^{self.power}"
    

    def __call__(self) -> Real:
        pass


lin1 = LinearFunc((1,2), (2,4), (3,6), (4,8))

print(lin1.points)

print(lin1.slope)

print(lin1.yIntercept)






print(PowerFunction(4))


