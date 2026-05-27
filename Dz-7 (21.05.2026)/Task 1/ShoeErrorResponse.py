from datetime import datetime
from dataclasses import dataclass

@dataclass
class ShoeErrorResponse:
    """Data object used to carry failure details back to the presentation layer."""

    id: int | None
    message: str
    timestamp: datetime