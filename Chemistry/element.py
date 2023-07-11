## Standard library imports
import math
import numpy as np
from dataclasses import dataclass, field


@dataclass(slots=True)
class Element:
    ##? Element identifiers
    symbol:str              #* The chemical symbol in the perioidc table
    name:str = ''           #* The full name of the element
    state:str = ''          #* Gas, liquid or solid
    type:str = ''           #* Gas or metal (Could also be based on group name)
    subscript: np.int8 = np.int8(0)

    ##? Element properties
    atomicNumber: np.int8 = np.int8(0)
    atomicMass: np.float32 = np.float32(0.0)
    charge: np.int8 = np.int8(0)

    electronegativity: np.float32 = np.float32(0.0)
    
    #? This function returns a compound class instance/ object of 2 reacting elements
    #! No security checks (ocet rule, if two metals or gasses are reacting)
    def react(self, element) -> object:
        ## If two metals react then there will be no reaction
        if self.type == element.type == "metal":        #? Two metals cannot react (unless alloy), security check
            return None

        lcm = math.lcm(self.charge, element.charge)     #* Find the lowest common multiple of the valence electron numbers
        self.subscript = abs(lcm // self.charge)        #* The balacing coefficient for the first element
        element.subscript = abs(lcm // element.charge)  #* The balancing coefficient for the second element
        
        return Compound(self, element)                  #? Returns a compound
    
    @classmethod
    def _standardize(cls) -> None:
        ##! This function will turn all the currently used class instances into the same units
        return NotImplementedError


@dataclass(slots=True)
class Compound:
    ## Compound identifyers
    name:str =""                           #* Name of the chemical compound
    formula:str = ""                       #* Chemical formula of the compound
    components: list[Element] = field(default_factory=list)                 #* List that contains the element objects that make up the compound

    ## Compound properties
    molarMass: float = 0.0
    bondEnthalpy: float = 0.0              #! This is based on the elements like the molar mass but the values are standard meaning it should be read from database

    def __post_init__(self, *args):
        self.components: list = list(args)        

        for element in self.components:
            molarMass += element.atomicMass                                #* Determine the moalr mass of the compound
            formula += f"{element.symbol + str(element.subscript)}"        #* Determine the formula from the consituent components

    def reactElement(self, element):
        ## If element charge is < 0 then it is a gas
        #? Don't think gases replace other gasses in a compound
        if element.charge < 0:
            # self.components[1] - element
            return None
        
        ## If the compound is raecting with a metal
        #! Add reactivity series check
        self.components[0] = element
        
        #! Currently the number are based on convention 
        #! Make sure to distinguish gasses from metals and save the compound in the correct order
    
    def reactCompound(self, compound):
        return NotImplementedError


'''
Element class functionallity:
- When created an element object will contain al the identifiers and properties implemented to the class.
  The object will be created with data that is stored in a database file within the program.

How do element objects react with each other?
- Create a method that takes another element object as input and write the functionality within this method.

How do elements react with each other in real life?
- They form bonds by sharing electrons. In order to bond elements I need to determine the number of valence electrons
  it is also important to keep restrictions in mind (octet rule, bonding domains/hybridization, hund's rule)

  if 3 valence electrons or less (val elec <= 3):
    element.donateElectron  and  element.recieveElectron
'''


'''
File description and logistics

Everything in chemistry revolves around elements and compounds.

The elements class:
1. Symbol
2. Atomic number
3. Particles
4. Isotopes

Q1. How to represent chemical reactions?
    1.1. What is included in a chemical reaction?
        - Reactants and products -> These are elements or compounds
        - Chemical kinetics
        - Equilibrium
    1.2. What mechanics should I simulate?/ How do chemical raections work?
    1.3. What are the conditions for chemical reactions to happen?

example oxidation:
metal (element object) + oxygen (element object) -> react (function) -> metal oxide (compound object)
1. The two elements combine (visually represented through the letters that form the compound)
2. The elements combine in ratios based on the number of valence electrons 
3. The compound that gets formed has new properties(mixed - some based on reactants and some new) and a new formula(based on the reactants)
'''

el1 = Element('Fe')
el1.charge = 3
el1.type = "metal"

el2 = Element('O')
el2.charge = -2
el2.type = "gas"

el3 = Element('Cu')
el3.charge = 2
el3.type = "metal"

el4 = Element('F')
el4.charge = -1
el4.type = "gas"

compound = el4.react(el2)

print(compound.components, compound.formula)
