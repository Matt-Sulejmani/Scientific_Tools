# Standard library imports
from dataclasses import dataclass, field
from typing import List, Tuple
import json

# Constants that will be set in the settings file when the module is run
unitsFile = b"C:\Users\sulej\Desktop\Projects\Science_Tools\units.json"

# Shorthands for commonly used types
type Numeric = int | float


@dataclass(slots=True)
class Unit:
    '''Unit is a dataclass or custom type that represent the units of a given 
    quantity. This dataclass is a subtype of "String". Basically separating each 
    part of a unit to make conversions easier.'''
    identifier: str
    prefix: str = ""
    power: int = 1

    def __repr__(self):
        '''Defines how a quantity is printed to the screen'''
        return f"{self.prefix}{self.identifier}{"^" + str(self.power) if self.power > 1 else ""}"


class Quantity:
    def __init__(self, magnitude: Numeric, unit: Unit, dimension: str,
                 sigFigs: int = 3, notation: str = "dec", errors: bool = False):
        # Attributes that are dependent on user input when creating a new quantity
        self.magnitude = magnitude
        self.unit = unit
        self.dimension = dimension

        # Default attributes that can be changed by the user later on
        self.sigFigs = sigFigs
        self.notation = notation
        self.errors = errors

    def __repr__(self):
        '''Print the qunatity in decimal and scientific notation with the given 
        number of significant figures.'''
        self.magnitude = round(self.magnitude, self.sigFigs)

        if self.notation == "sci":
            # ? This only prints the value in scientific notation the value itself
            # ? is still a float in computer memory
            return f"{self.magnitude:e}{self.unit}"

        return f"{self.magnitude}{self.unit}"

    def convert(self, target: Unit | str) -> None:
        '''This function allows for the conversion of magnitude prefixes within
        the same measurement dimension (length, time, temperature ...)'''

        with open(unitsFile, 'r') as file:
            multiples = json.load(file)["multiples"]

            # Conversion of magnitude based on the change in prefix
            # Eg, converting from km to m
            self.magnitude *= (multiples[self.unit.prefix] / multiples[target])
            self.unit.prefix = target

        return self

    def convertSys(self, targetSys: Unit):
        return NotImplementedError


@dataclass(slots=True)
class Table:
    '''This dataclass holds the (x, y) data points that are used during various
    calculations. It offers methods like adding and removing data points, printing
    the current stored values and grpahing the values in the table. \n 
    Furthermore it offers some functionallity that is related to statistical 
    analysis of the current data being stored.'''
    container: List[Tuple] = field(default_factory=List[Tuple])

    def addPair(self, varX: Numeric, varY: Numeric) -> None:
        self.container.append(tuple(varX, varY))

    def removePair(self, index: int) -> None:
        del self.container[index]

    def slope(self, *args: Tuple) -> Numeric:
        '''This method calculates the slope of the function relating variable x
        to variable y.'''
        return (args[-1][1] - args[0][1]) / (args[-1][0] - args[0][0])
    
    def intercept(self):
        pass


table = Table([(1, 2), (3, 4)])
print(table.slope((5, 6), (3, 4), (1, 2)))
