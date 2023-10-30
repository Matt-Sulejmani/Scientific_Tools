## Library imports for the package
import math
import json
from quantities import Quantity

## Standard imports from the constants and units files
with open("Constants.json", "r") as f:
    const= json.load(f)

with open("units.json", "r") as f:
    units = json.load(f)

## Functions related to quantum physics
def photoelectric():
    pass

def electronEnergy(frequency:float) ->float:
    return const['planckConst'] * frequency

def einsteinPhotoelecticEq(workFunction: float, electronEnergy: float=0, frequency: float=0) -> float:
    if electronEnergy:
        return electronEnergy - workFunction
    
    return (frequency * const['planckConst']) - workFunction

def bohrOrbitEnergy(n: int) -> float:
    return (-13.6 / pow(n, 2))