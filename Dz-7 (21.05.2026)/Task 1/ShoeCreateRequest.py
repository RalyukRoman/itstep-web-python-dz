from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeCreateRequest:
    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float