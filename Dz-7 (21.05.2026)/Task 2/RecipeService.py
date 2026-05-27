from RecipeRepository import RecipeRepository
from RecipeCreateRequest import RecipeCreateRequest
from RecipeUpdateRequest import RecipeUpdateRequest
from RecipeMapper import RecipeMapper
from RecipeResponse import RecipeResponse
from RecipeDeleteResponse import RecipeDeleteResponse
from RecipeErrorResponse import RecipeErrorResponse

class RecipeService:
    """Service class for recipe operations."""

    def __init__(self, recipe_repository: RecipeRepository):
        self._recipe_repository = recipe_repository

    def get_all_recipes(self) -> list[RecipeResponse]:
        """Retrieves all recipe entities from repository."""

        all_recipes_entity = self._recipe_repository.get_all_recipes()
        return RecipeMapper.map_entities_to_list_response(all_recipes_entity)

    def get_recipe(self, recipe_get_id: int) -> RecipeResponse | RecipeErrorResponse:
        """Searches for a specific recipe by its unique identifier."""

        recipe_entity = self._recipe_repository.get_recipe(recipe_get_id)
        return RecipeMapper.map_entity_to_response(recipe_entity)

    def create_recipe(
        self, recipe_create_request: RecipeCreateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        """Assigns auto-incremented ID to the new recipe entityand persists it."""

        create_recipe_entity = RecipeMapper.map_create_to_entity(recipe_create_request)
        recipe_entity = self._recipe_repository.create_recipe(create_recipe_entity)
        return RecipeMapper.map_entity_to_response(recipe_entity)
    
    def update_recipe(
        self, recipe_update_request: RecipeUpdateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        """Updates an existing recipe entity."""

        old_recipe_entity = self._recipe_repository.get_recipe(recipe_update_request.id)

        if (old_recipe_entity is None):
            return RecipeMapper.map_error_to_response(
                "Recipe not found", recipe_update_request.id
            )
        
        update_recipe_entity = RecipeMapper.map_update_to_entity(
            recipe_update_request, old_recipe_entity
        )
        
        recipe_entity = self._recipe_repository.update_recipe(update_recipe_entity)
        return RecipeMapper.map_entity_to_response(recipe_entity)
    
    def delete_recipe(
        self, recipe_delete_id: int
    ) -> RecipeDeleteResponse | RecipeErrorResponse:
        """Removes a recipe entity from the database using its ID."""

        is_deleted = self._recipe_repository.delete_recipe(recipe_delete_id)

        if (is_deleted):
            return RecipeMapper.map_delete_to_response(recipe_delete_id)
        else:
            return RecipeMapper.map_error_to_response(
                "Cannot delete. Recipe not found", recipe_delete_id
            )
