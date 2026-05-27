from dataclasses import dataclass
from RecipeEnums import RecipeType, NameOfCuisine
from pydantic import BaseModel, ConfigDict

@dataclass
class RecipeResponse(BaseModel):
    """
    Data object containing the full read-ready data of a recipe, 
    typically returned after successful operations.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine