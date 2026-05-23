from datetime import datetime
from dataclasses import dataclass

@dataclass
class RecipeErrorResponse:
    id: int | None
    message: str
    timestamp: datetime