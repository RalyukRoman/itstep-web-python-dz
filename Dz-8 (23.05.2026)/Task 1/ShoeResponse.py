from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind
from pydantic import BaseModel, ConfigDict

@dataclass
class ShoeResponse(BaseModel):
    """
    Data object containing the full read-ready data of a shoe, 
    typically returned after successful operations.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float