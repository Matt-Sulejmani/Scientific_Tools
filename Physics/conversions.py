''' This module contains all the unit conversions related to physics calculations '''

# Converts scientific notation to decimal
def sci_to_dec(val: str) -> float:
    return float(val)

# The 12 is the number of sig figs
def dec_to_sci(val: float) -> str:
    return "{:.12e}".format(val)

# Electromagnetism

#! Change to use constants
def J_to_eV(initVal: float) -> float:
    return initVal * 1.6e-19

def eV_to_J(initVal: float) -> float:
    return initVal / 1.6e-19