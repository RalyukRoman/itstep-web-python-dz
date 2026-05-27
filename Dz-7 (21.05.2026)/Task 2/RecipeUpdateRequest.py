from dataclasses import dataclass
from RecipeEnums import RecipeType, NameOfCuisine

@dataclass
class RecipeUpdateRequest:
    """A data object containing the data needed to update a new recipe record."""

    id: int
    name: str               | None = None
    author: str             | None = None
    type: RecipeType        | None = None
    description: str        | None = None
    link_video: str         | None = None
    ingredients: list[str]  | None = None
    cuisine: NameOfCuisine  | None = None