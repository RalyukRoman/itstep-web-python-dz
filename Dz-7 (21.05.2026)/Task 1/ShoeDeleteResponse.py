from dataclasses import dataclass
from datetime import datetime

@dataclass
class ShoeDeleteResponse:
    """Data object that represents the successful confirmation of a shoe deletion."""

    id: int 
    timestamp: datetime