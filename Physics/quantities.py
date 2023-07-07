class Quantity(object):
    def __init__(self):
        self.magnitude: float = 0.0         #* The magnitude component
        self.direction: list = [0, 0, 0]    #* Direction vector for the qunatity
        self.units: str = ''                #* The units related to the quantity
    
    def interact(self, quantity) -> object:
        ## If the quantities don't have the same units they can't interact
        if self.units != quantity.units:
            return None



'''
Quantities:
- Mass
- Temperature
- Luminosity
- Distance
- Time
- Amount
- Current

Two quantities can interact to form a new quantity according to a formula.

Two quantities of the same type can be added or subtracted. 
'''