'''
    Energetics functions and topics
    - Enthalpy changes
    - Entropy
    - Temperature
    - Gibbs free energy
    - Energy cycles 
'''
from dataclasses import dataclass, field
from numbers import Real
from ..quantities import Quantity


class Enthalpy(object):
    def __init__(self):
        pass

    def bondEnthalpy(self):
        pass

    def hydrationEnthalpy(self):
        pass

    def latticeEnthalpy(self):
        pass

    def atomizationEnthalpy(self):
        pass

    def ionizationEnergy(self):
        pass





class KineticEnergy(Quantity):
    def __init__(self, value: Real, ):
        pass
    

    def get_value(self, m: Real, u: Real):
        """
        The function that sets the value of the instance when passed in a mass
        and 

        Args:
            m (float): _description_
            u (float): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        try:
            return 0.5 * m * u**2

        except:
            raise ValueError()


class PotentialEnergy(Quantity):
    def __init__(self):
        pass
        
