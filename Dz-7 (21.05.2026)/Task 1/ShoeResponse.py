from dataclasses import dataclass
from datetime import datetime
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeResponse:
    """
    Data object containing the full read-ready data of a shoe, 
    typically returned after successful operations.
    """

    id: int
    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float
    timestamp: datetime