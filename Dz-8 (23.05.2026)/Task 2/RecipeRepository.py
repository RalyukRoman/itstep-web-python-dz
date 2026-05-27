from RecipeEntity import RecipeEntity
from RecipeDTO import RecipeDTO
from RecipeMapper import RecipeMapper

class RecipeRepository:
    """A repository for recipes."""

    def __init__(self) -> None:
        self._db: dict[int, RecipeEntity] = {}
        self._next_id = 1

    def get_all_recipes(self) -> dict[int, RecipeEntity]:
        """Retrieves all currently stored recipe records."""
        return self._db

    def get_recipe(
        self, recipe_id: int
    ) -> tuple[int | None, RecipeEntity | None]:
        """Searches for a specific recipe by its unique identifier."""
        
        if recipe_id not in self._db:
            return None, None
        return recipe_id, self._db.get(recipe_id)

    def create_recipe(
        self, recipe_dto: RecipeDTO
    ) -> tuple[int, RecipeEntity]:
        """Assigns auto-incremented ID to the new recipe entityand persists it."""
        
        recipe_entity = RecipeMapper.map_dto_to_entity(recipe_dto)
        current_id = self._next_id

        self._db[current_id] = recipe_entity
        self._next_id += 1

        return current_id, recipe_entity
    
    def update_recipe(
        self, recipe_id: int, recipe_dto: RecipeDTO
    ) -> tuple[int | None, RecipeEntity | None]: 
        """Finds an existing recipe by its ID and replaces it with the updated entity."""
        
        if recipe_id not in self._db:
            return None, None
        
        recipe_entity = RecipeMapper.map_dto_to_entity(recipe_dto)
        self._db[recipe_id] = recipe_entity
        
        return recipe_id, recipe_entity
    
    def delete_recipe(
        self, recipe_id: int
    ) -> int | None:
        """Removes a recipe entity from the database using its ID."""

        if recipe_id not in self._db:
            return None
        
        del self._db[recipe_id]
        return recipe_id