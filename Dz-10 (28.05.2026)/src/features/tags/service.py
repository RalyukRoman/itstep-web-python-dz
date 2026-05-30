from .repository import TagRepository
from .schemas import TagCreate
from .models import Tag
from src.features.posts.repository import PostRepository

class TagService:
    def __init__(
        self, 
        repository: TagRepository,
        post_repository: PostRepository
    ):
        self.repository = repository
        self.post_repository = post_repository

    async def add_tags_to_post(
        self, 
        post_id: int, 
        tags_in: TagCreate
    ) -> list[Tag]:
        post_data = await self.post_repository.get_post_by_id(post_id)
        _, post = post_data

        attached_tags = []
        
        for name in tags_in.names:
            cleaned_name = name.strip().lower()
            if not cleaned_name:
                continue
                
            # Шукаємо тег
            existing_tag = await self.repository.get_by_name(cleaned_name)
            if existing_tag:
                _, tag_entity = existing_tag
            else:
                # Якщо немає — створюємо новий
                _, tag_entity = await self.repository.create_tag(cleaned_name)
            
            attached_tags.append(tag_entity)
        
        # Додаємо теги до зв'язків поста (SQLAlchemy сама заповнить post_tags)
        post.tags.extend(attached_tags)
        await self.repository.db.commit()
        
        return attached_tags