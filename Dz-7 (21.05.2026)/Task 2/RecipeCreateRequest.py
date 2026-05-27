from dataclasses import dataclass
from RecipeEnums import NameOfCuisine, RecipeType

@dataclass
class RecipeCreateRequest:
    """Data transfer object for recipes."""

    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine