from dataclasses import dataclass
from RecipeEnums import NameOfCuisine, RecipeType
from pydantic import BaseModel, ConfigDict

@dataclass
class RecipeEntity(BaseModel):
    """Domain model representing a recipe entity."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine
    