import json

with open('Constants.json', 'r') as f:
    const = json.load(f)

## Constant declarations
L = const['avogadrosConst']
molarVolume = const['molarGasVolume']


## Basic soticiometric conversions
def particleToMole(particle: float) -> float:
    return paricle / L


def moleToParticle(mol: float) -> float:
    return mol * L

##! NEEDS attention
def molarMassCalc(*args: str) -> float:
    for element in args:
        element.casefold()


def massToMol(mass: float, molarMass: float) -> float:
    return mass / molarMass


def molToMass(mol: float, molarMass: float) -> float:
    return molarMass * mol


def volumeToMol(volume: float, condition: int=0) -> float:
    return volume / molarVolume[condition]


def molToVolume(mol: float, consdition: int=0) -> float:
    return mol * molarVolume[0]


def limitingReagent(reaction: str, reactAmount1: float, reactAmount2: float, product: str) -> tuple:
    '''
        Function will return the limiting reagent (first result) and product amount.

        The inputs required for the fucntion:
        - Reaction
        - Mol ratios
        - Reactenet mass or amount
        - Desired product

        Determining limitign reagent: Firstly we find the amount in mol of reactant 1. We then find the amount of the second reactant need to react with the first reactant. We then determine which is in excess.
    '''

    '''
    To do:
    - Info from reaction
        - Get ratio from reaction
            - Separate reaction into parts *how?
        - Get compound/elements from reaction
            - Get the molar mass
            
    - Find limiting reagent
    '''
    pass
