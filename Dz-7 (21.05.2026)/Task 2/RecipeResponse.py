from dataclasses import dataclass
from datetime import datetime
from RecipeEnums import RecipeType, NameOfCuisine

@dataclass
class RecipeResponse:
    """
    Data object containing the full read-ready data of a recipe,
    typically returned after successful operations.
    """

    id: int
    name: str
    author: str
    type: RecipeType
    description: str
    link_video: str
    ingredients: list[str]
    cuisine: NameOfCuisine
    timestamp: datetime