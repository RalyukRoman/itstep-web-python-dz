from RecipeRepository import RecipeRepository
from RecipeRequest import RecipeRequest
from RecipeMapper import RecipeMapper
from RecipeResponse import RecipeResponse
from RecipeNotFoundException import RecipeNotFoundException

class RecipeService:
    """Service layer for recipe operations."""

    def __init__(self, recipe_repository: RecipeRepository) -> None:
        self._recipe_repository = recipe_repository

    def get_all_recipes(self) -> list[RecipeResponse]:
        """Retrieves all recipe entities from repository."""

        list_recipes_entity = self._recipe_repository.get_all_recipes()
        return RecipeMapper.map_entities_to_responses(list_recipes_entity)

    def get_recipe(self, recipe_id: int) -> RecipeResponse:
        """Retrieves a single recipe by ID."""

        _, recipe_entity = self._recipe_repository.get_recipe(recipe_id)
        if recipe_entity is None:
            raise RecipeNotFoundException(recipe_id)
        return RecipeMapper.map_entity_to_response(recipe_id, recipe_entity)

    def create_recipe(self, recipe_request: RecipeRequest) -> RecipeResponse:
        """Creates a new recipe entity."""

        recipe_dto = RecipeMapper.map_request_to_dto(recipe_request)
        recipe_id, recipe_entity = self._recipe_repository.create_recipe(recipe_dto)
        return RecipeMapper.map_entity_to_response(recipe_id, recipe_entity)
    
    def update_recipe(self, recipe_id: int, recipe_request: RecipeRequest) -> RecipeResponse:
        """Updates an existing recipe entity."""

        old_recipe_entity = self._recipe_repository.get_recipe(recipe_id)
        if old_recipe_entity is None:
            raise RecipeNotFoundException(recipe_id)
        
        recipe_dto = RecipeMapper.map_request_to_dto(recipe_request)
        _, recipe_entity = self._recipe_repository.update_recipe(recipe_id, recipe_dto)
        return RecipeMapper.map_entity_to_response(recipe_id, recipe_entity)
    
    def delete_recipe(self, recipe_id: int) -> int:
        """Deletes a recipe entity by ID."""
        
        deleted_recipe_id = self._recipe_repository.delete_recipe(recipe_id)
        if not deleted_recipe_id:
            raise RecipeNotFoundException(recipe_id)
        return deleted_recipe_id
