import math
import json

with open("Constants.json", "r") as f:
    const= json.load(f)

with open("units.json", "r") as f:
    units = json.load(f)

'''
    This function calculates the coulomb force given the two charges and the distance between them. The units are not yet included in the calculation. Finish explanations for each.
    Include units
'''
def coulombForce(q1: float, q2: float, r: float) -> float:
    return (q1 * q2 * const['coulombConst']) / pow(r, 2)

def findCoulombCharge(force: float, q: float, r: float) -> float:
    return (force * pow(r, 2)) / (q * const['coulombConst'])

def findCoulombDist(force: float, q1: float, q2: float) -> float:
    return math.sqrt( (const['coulombConst'] * q1 * q2) / force)

'''

'''
def electricField(q: float, r: float, force: float =None) -> float:
    if r:
        return (q * const['coulombConst']) / pow(r, 2)
    
    return (force / q)
    