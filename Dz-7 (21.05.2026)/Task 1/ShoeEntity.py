from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeEntity:
    """Domain model representing a shoe entity."""

    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float
    id: int | None = None
    