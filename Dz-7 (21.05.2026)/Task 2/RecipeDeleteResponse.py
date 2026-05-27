from dataclasses import dataclass
from datetime import datetime

@dataclass
class RecipeDeleteResponse:
    """Data object that represents the successful confirmation of a recipe deletion."""

    id: int 
    timestamp: datetime