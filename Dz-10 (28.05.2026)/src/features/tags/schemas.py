from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TagBase(BaseModel):
    name: str

class TagCreate(BaseModel):
    # Приймаємо список тегів списком строк, наприклад ["python", "fastapi"]
    names: list[str]

class TagRead(TagBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True
    )