''' This module contains all unit conversions for each respective library '''
import json

with open('Constants.json', 'r') as f:
    const = json.load(f)

## Converts scientific notation to decimal
def sciToDec(val: str) -> float:
    return float(val)

## The 12 is the number of sig figs
def decToSci(val: float) -> str:
    return "{:.12e}".format(val)



# Electromagnetism

def J_to_eV(initVal: float) -> float:
    return initVal * const['electronCharge']

def eV_to_J(initVal: float) -> float:
    return initVal / const['electronCharge']