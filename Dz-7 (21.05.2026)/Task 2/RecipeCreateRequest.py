from dataclasses import dataclass
from RecipeEnums import NameOfCuisine, RecipeType

@dataclass
class RecipeCreateRequest:
    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine