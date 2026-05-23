from dataclasses import dataclass
from RecipeEnums import RecipeType, NameOfCuisine

@dataclass
class RecipeEntity:
    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine
    id: int | None = None
    