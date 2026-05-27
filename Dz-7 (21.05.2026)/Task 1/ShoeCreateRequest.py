from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeCreateRequest:
    """A data object containing the data needed to create a new shoe record."""

    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float