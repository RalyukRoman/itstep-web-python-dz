from dataclasses import dataclass
from datetime import datetime

@dataclass
class RecipeDeleteResponse:
    id: int 
    timestamp: datetime