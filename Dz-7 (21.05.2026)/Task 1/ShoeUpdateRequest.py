from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind

@dataclass
class ShoeUpdateRequest:
    """A data object containing the data needed to update a new shoe record."""

    id: int
    gender_type: GenderType | None = None
    shoe_type: ShoeKind     | None = None
    color: str              | None = None
    price: float            | None = None
    manufacturer: str       | None = None
    size: int | float       | None = None