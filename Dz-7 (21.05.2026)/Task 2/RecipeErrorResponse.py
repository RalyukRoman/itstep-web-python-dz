from datetime import datetime
from dataclasses import dataclass

@dataclass
class RecipeErrorResponse:
    """Data object used to carry failure details back to the UI layer."""

    id: int | None
    message: str
    timestamp: datetime