from sqlalchemy import ForeignKey, String, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.infrastructure.base_model import Base, TimestampMixin

# Проміжна таблиця зв'язку Many-to-Many
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
)

class Tag(Base, TimestampMixin):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)

    # Відносини
    posts: Mapped[list["Post"]] = relationship("Post", secondary=post_tags, back_populates="tags")

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, name={self.name})"

# Імпорти для типізації
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.features.posts.models import Post