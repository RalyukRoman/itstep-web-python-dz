from dataclasses import dataclass
from ShoeEnums import GenderType, ShoeKind
from pydantic import BaseModel, ConfigDict

@dataclass
class ShoeRequest(BaseModel):
    """Data transfer object for shoes."""

    model_config = ConfigDict(from_attributes=True)

    gender_type: GenderType
    shoe_type: ShoeKind
    color: str
    price: float
    manufacturer: str
    size: int | float