class Quantity(object):
    def __init__(self):
        ## Fundamental identifiers for a quantity
        self.magnitude: float = 0.0
        self.units: str = ''

    def convert(self):
        return NotImplementedError


class vQuantity(Quantity):
    def __init__(self, directionVec: list = [0, 0, 0], argument: float = 0.0):
        self.directionVec = directionVec   ## This is the direction vector of the quantity represented in [x, y, z] coords
        self.argument = argument           ## This is the alternate way of giving a direction to the force by giving an angle in rad
