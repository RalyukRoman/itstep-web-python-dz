from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional, Tuple
from .models import Tag

class TagRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_name(self, name: str) -> Optional[Tuple[int, Tag]]:
        query = select(Tag).where(Tag.name == name)
        result = await self.db.execute(query)
        tag = result.scalar_one_or_none()
        if tag:
            return tag.id, tag
        return None

    async def create_tag(self, name: str) -> Tuple[int, Tag]:
        tag = Tag(name=name)
        self.db.add(tag)
        await self.db.flush()
        return tag.id, tag