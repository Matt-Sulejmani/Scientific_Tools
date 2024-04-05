'''
File Documentation:
    Purpose:
    - The purpose of this module is to contain common stoichiometric calculation
    functions. 

    Functions:
    1. Mass, Molar Mass, Mol conversions
    2. 

'''

import json
from typing import Dict, List
from element import Element
from dataclasses import dataclass, field


def formula_from_mass(**kwargs: Dict[Element, float]) -> str:
    '''
    Input:
    - List of keyword: value pairs (Dict) (Element: mass)

    Procedure:
    - Divide the the given mass by the element's molar mass
    - Find ratio between elements
    - Standardize ratio

    Output:'''
    ratios: List = []

    # Step 1: Figure out mol of each element
    for element, mass in kwargs:
        ratios.append(mass / element.molar_mass)

    # Step 2: Divide by smallest value

    ratios = [value / ratios.min() for value in ratios]


# Imports


# Load Json file with constants
with open('Constants.json', 'r') as f:
    const = json.load(f)

# Constant declarations and value assign
L = const['avogadrosConst']
molarVolume = const['molarGasVolume']


class Converter(object):
    """
    Converter class that container common conversions.
    """

    # Different conversions concerning mols
    # Coversions with number of particles, mass, volume and moles

    @staticmethod
    def particle_to_mol(particle: float) -> float:
        """
        Converts the input from particles to moles through division of the input
        with Avogadro's constant (6.022e23)


        Args:
            particle (float): Number of paricles as a floating point number

        Returns:
            float: Number of moles as a float
        """
        return particle / L

    @staticmethod
    def mol_to_particle(mol: float) -> float:
        """
        Convert the number of moles into the number of particles of a substance 
        through multiplication of the input with Avogadro's constant (6.022e23)

        Args:
            mol (float): Number of moles

        Returns:
            float: Number of particles
        """
        return mol * L

    @staticmethod
    def mass_to_mol(mass: float, molar_mass: float) -> float:
        """
        Convert the mass of a substance to moles of that substance by diving the
        mass with the molar mass. Note that both the mass and molar should be in
        the same units (g and g/mol respectively)

        Args:
            mass (float): Mass in grams (g)
            molar_mass (float): Molar mass of the element/compound in g/mol

        Returns:
            float: Number of moles 
        """
        return mass / molar_mass

    @staticmethod
    def mol_to_mass(mol: float, molar_mass: float) -> float:
        """_summary_

        Args:
            mol (float): _description_
            molar_mass (float): _description_

        Returns:
            float: _description_
        """
        return molar_mass * mol

    @staticmethod
    def volume_to_mol_gas(volume: float, condition: int = 0) -> float:
        """_summary_

        Args:
            volume (float): _description_
            condition (int, optional): _description_. Defaults to 0.

        Returns:
            float: _description_
        """
        return volume / molarVolume[condition]

    @staticmethod
    def mol_to_volume_gas(mol: float, condition: int = 0) -> float:
        """_summary_

        Args:
            mol (float): _description_
            condition (int, optional): _description_. Defaults to 0.

        Returns:
            float: _description_
        """
        return mol * molarVolume[condition]

    #! More conversions to add


@dataclass
class Reactant:
    coefficient: int
    mol: float


def limitingReagent(reactants: Dict[Element, int], products: Dict[Element, int]) -> tuple:
    """_summary_

    Args:
        reactants (Dict[Element, int]): _description_
        products (Dict[Element, int]): _description_

    Returns:
        tuple: _description_
    """
    '''
        Function will return the limiting reagent (first result) and product amount.

        The inputs required for the fucntion:
        - Reaction
        - Mol ratios
        - Reactenet mass or amount
        - Desired product

        Determining limitign reagent: Firstly we find the amount in mol of reactant 1. We then find the amount of the second reactant need to react with the first reactant. We then determine which is in excess.
    '''


    return NotImplementedError
