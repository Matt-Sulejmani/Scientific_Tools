## Standard library imports
import string

class Element(object):
    def __init__(self, symbol:str):
        ## Element specific
        self.symbol:str = symbol
        self.name:str = ""
        self.type:str = ""

        ## Element properties
        self.atomicMass:float = 0.0
        self.atomicNumber: int = 0
        self.valenceElectrons: int = 0

        self.electronegativity:float = 0
    
    def selfIdentify(self):
        self.symbol = ""
        return NotImplementedError


class Compound(object):
    def __init__(self, *args:Element):
        ## Compound identifyers
        self.name:str =""
        self.elements:list = [element for element in args]
        self.formula:str = ""

        ## Compound properties
        self.molarMass:float
        

    ## Assumes that the compound is passed as an input in the form of a string
    ## Determines what elements are in the compound
    def determineCompound(self, *args) -> str:
        return NotImplementedError
    
    def balanceCompound(self):
        
        return NotImplementedError

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
    
    #! string input -> split into elements and subscripts -> identify elements and create new objects from the elemnt class -> store element objects alonside coefficients in the compound object
    ## "Fe_2+O_3"

'''
el1 = Element()
el2 = Element()

el1.symbol = "Fe"
el2.symbol = "O"
compound = Compound(el1, el2)

compound.formula = "Fe1OH2"
print(compound.determineElements())

'''