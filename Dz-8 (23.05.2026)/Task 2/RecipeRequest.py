from dataclasses import dataclass
from RecipeEnums import RecipeType, NameOfCuisine
from pydantic import BaseModel, ConfigDict

@dataclass
class RecipeRequest(BaseModel):
    """Data transfer object for recipes."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine