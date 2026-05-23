from dataclasses import dataclass
from datetime import datetime
from RecipeEnums import RecipeType, NameOfCuisine

@dataclass
class RecipeResponse:
    id: int
    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine
    timestamp: datetime