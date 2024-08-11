from dataclasses import dataclass

# TODO - Look into using units as a meta class in quantities

type meter      = standard_unit
type second     = standard_unit
type candela    = standard_unit
type ampere     = standard_unit
type kelvin     = standard_unit
type mole       = standard_unit
type kilogram   = standard_unit


@dataclass(slots=True)
class standard_unit:
    """
    The base class for all standard units. Units in this case 

    Attributes:

    """
    prefix: str
    dimension: str


@dataclass(slots=True)
class derived_unit:
    pass
