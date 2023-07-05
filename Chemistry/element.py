## Standard library imports
import string
import math
import string


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
        self.charge: int = 0

        self.electronegativity:float = 0
    
    #? This function returns the compound formal of 2 reacting elements in string format
    # Currently only work if 2 simple elements are reacting
    #! No security checks (ocet rule, if two metals or gasses are reacting)
    def react(self, element) -> str:
        lcm = math.lcm(self.charge, element.charge)     #* Find the lowest common multiple of the valence electron numbers
        self.subscript = lcm // self.charge                       #* The balacing coefficient for the first element
        element.subscript = lcm // element.charge                 #* The balancing coefficient for the second element
        
        return Compound(self, element)                                      #? Returns a compound


class Compound(object):
    def __init__(self, *args:Element):
        ## Compound identifyers
        self.name:str =""                           #* Name of the chemical compound
        self.formula:str = f""                      #* Chemical formula of the compound
        # self.components:dict = {element.symbol: element.charge for element in args}       #* Elments/ Polyatomic ions that make up the compound and their valence electrons
        self.components: list = list(args)          #* List that contains the element objects that make up the compound

        ## Compound properties
        self.molarMass: float = 0.0

        for element in self.components:
            self.molarMass += element.atomicMass

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
        pass

    ## Find the number subscripts of each element in the case that the compound is given as input
    ## Private function
    def findElementNumbers(self) -> list:
        if self.formula:
            indexes = [index for index, character in enumerate(self.formula) if character in string.digits]
            
            return indexes

        return "Value not Found" #! Replace with error message
    
    def determineElements(self) -> dict:
        indexes = self.findElementNumbers()

        if len(indexes) == 2:
            element1 = self.formula[0:indexes[0]]
            element2 = self.formula[indexes[0] + 1: indexes[1]]

            ## Want to create 2 element instances based on the formula/ name of the elements form the compound
            ## Assign the corresponding propertties during the process
            ## Store in the list
            return element1, element2
    
    #? string input -> split into elements and subscripts -> identify elements and create new objects from the elemnt class -> store element objects alonside coefficients in the compound object
    ## "Fe_2+O_3"

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

def reactStructure(*args):
    reactantElements = {}           #* Dictionary that contains all the elements (even parts of compounds) and their valence electrons
    
    ## Loop over the reactants, pair element symbol and valence electrons for element object inputs and append the components dictionary for compound objects
    for reactant in args:
        if type(reactant) == Element:
            reactantElements[reactant.symbol] = reactant.charge
        
        else:
            reactantElements = reactantElements | reactant.components
    
    print(reactantElements)


def redox(*args: Element) -> list:
    return NotImplementedError


def neutralization(*args: Element)-> list:
    return NotImplementedError


def singleSub(*args: Element)-> list:
    return NotImplementedError


def doubleSub(*args: Element)-> list:
    return NotImplementedError


def decomposition(*args: Element)-> list:
    return NotImplementedError


el1 = Element('Fe')
el1.charge = 3

el2 = Element('O')
el2.charge = -2

el3 = Element('Cu')
el3.charge = 2

el4 = Element('F')
el4.charge = -1

compound = Compound(el3, el2)
