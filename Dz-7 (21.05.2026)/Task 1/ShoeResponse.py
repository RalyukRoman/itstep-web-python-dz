from dataclasses import dataclass
from datetime import datetime
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeResponse:
    id: int
    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float
    timestamp: datetime