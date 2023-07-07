## Standard library imports
import math


class Element(object):
    def __init__(self, symbol:str):
        ##? Element identifiers
        self.symbol:str = symbol        #* The chemical symbol in the perioidc table
        self.name:str = ""              #* The full name of the element
        self.state:str = ""             #* Gas, liquid or solid
        self.type:str = ""              #* Gas or metal (Could also be based on group name)
        self.subscript: int = 0

        ##? Element properties
        self.atomicNumber:int = 0
        self.atomicMass:float = 0.0
        self.charge:int = 0

        self.electronegativity:float = 0
    
    #? This function returns the compound formal of 2 reacting elements in string format
    # Currently only work if 2 simple elements are reacting
    #! No security checks (ocet rule, if two metals or gasses are reacting)
    def react(self, element) -> object:
        ## If two metals react then there will be no reaction
        if self.type == element.type == "metal":        #? Two metals cannot react (unless alloy), security check
            return None

        lcm = math.lcm(self.charge, element.charge)     #* Find the lowest common multiple of the valence electron numbers
        self.subscript = abs(lcm // self.charge)        #* The balacing coefficient for the first element
        element.subscript = abs(lcm // element.charge)  #* The balancing coefficient for the second element
        
        return Compound(self, element)                  #? Returns a compound


class Compound(object):
    def __init__(self, *args:Element):
        ## Compound identifyers
        self.name:str =""                           #* Name of the chemical compound
        self.formula:str = ""                       #* Chemical formula of the compound
        self.components: list = list(args)          #* List that contains the element objects that make up the compound

        ## Compound properties
        self.molarMass: float = 0.0
        self.bondEnthalpy: float = 0.0              #! This is based on the elements like the molar mass but the values are standard meanign it should be read from database

        for element in self.components:
            self.molarMass += element.atomicMass                                #* Determine the moalr mass of the compound
            self.formula += f"{element.symbol + str(element.subscript)}"        #* Determine the formula from the consituent components

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
