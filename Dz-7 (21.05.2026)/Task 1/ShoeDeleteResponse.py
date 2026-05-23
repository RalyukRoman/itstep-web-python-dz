from dataclasses import dataclass
from datetime import datetime

@dataclass
class ShoeDeleteResponse:
    id: int 
    timestamp: datetime