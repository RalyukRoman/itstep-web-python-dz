from datetime import datetime
from dataclasses import dataclass

@dataclass
class ShoeErrorResponse:
    id: int | None
    message: str
    timestamp: datetime