from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database import get_db
from src.features.auth.dependencies import get_current_user
from src.features.auth.models import User
from .schemas import TagCreate, TagRead
from .repository import TagRepository
from .service import TagService
from src.features.posts.repository import PostRepository

router = APIRouter(prefix="/tags", tags=["Social - Tags"])

async def get_tag_service(
    db: AsyncSession = Depends(get_db)
) -> TagService:
    repository = TagRepository(db)
    post_repository = PostRepository(db)
    return TagService(repository, post_repository)

@router.post(
    "/{post_id}", 
    response_model=list[TagRead], 
    status_code=status.HTTP_201_CREATED
)
async def add_tags_to_post(
    post_id: int,
    tags_in: TagCreate,
    current_user: User = Depends(get_current_user),
    service: TagService = Depends(get_tag_service),
    db: AsyncSession = Depends(get_db)
):
    # Перевіримо чи існує пост
    post_repo = PostRepository(db)
    post = await post_repo.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        
    return await service.add_tags_to_post(post_id, tags_in)