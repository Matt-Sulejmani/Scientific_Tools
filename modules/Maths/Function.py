# Standard library imports
from typing import Tuple

# Type aliases
type Number = int | float


class LinearFunc:
    def __init__(self, *args: Tuple[Number]):
        self.points = list(args)

    def addPoints(self, *args: Tuple[Number]) -> None:
        '''Enter the points you want the function to remember in the format (x, y).
        All the points should be entered according to this format and separated
        by a comma.'''
        self.points.extend(args)

    def removePoints(self, *args: int) -> None:
        '''Enter the index of the points you want to delete from the functions 
        memory.'''
        for index in args:
            del self.points[index]

    def __repr__(self) -> str:
        '''Prints the list of points the function is storing.'''
        return f"{self.points}"

    @property
    def slope(self) -> Number:
        '''Slope of the linear function, based on the list of data points provided 
        when creating the function itself.'''
        point1, point2 = self.points[0], self.points[-1]

        # Formula: a = (y2 - y1) / (x2 - x1)
        return (point2[1] - point1[1]) / (point2[0]-point1[0])

    @property
    def yIntercept(self) -> Number:
        '''The y-intercept of the linear function.'''
        point = self.points[0]

        # Fomula: c = y1 - ax1
        return point[1] - self.slope * point[0]


class Polynomial:
    def __init__(self, *args):
        self.points = list(args)

    @property
    def degree(self) -> int:
        return 0
