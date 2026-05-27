from RecipeRepository import RecipeRepository
from RecipeCreateRequest import RecipeCreateRequest
from RecipeUpdateRequest import RecipeUpdateRequest
from RecipeMapper import RecipeMapper
from RecipeResponse import RecipeResponse
from RecipeDeleteResponse import RecipeDeleteResponse
from RecipeErrorResponse import RecipeErrorResponse

class RecipeService:
    """
    Service layer class that implements business logic rules and bridges 
    communication between the Repository layer and the Controller layer.
    """

    def __init__(self, recipe_repository: RecipeRepository):
        self._recipe_repository = recipe_repository

    def get_all_recipes(self) -> list[RecipeResponse]:
        """Retrieves all recipe entities from repository."""

        all_recipes_entity = self._recipe_repository.get_all_recipes()
        return RecipeMapper.map_entities_to_list_response(all_recipes_entity)

    def get_recipe(self, recipe_get_id: int) -> RecipeResponse | RecipeErrorResponse:
        """Retrieves a single recipe by ID"""

        recipe_entity = self._recipe_repository.get_recipe(recipe_get_id)
        return RecipeMapper.map_entity_to_response(recipe_entity)

    def create_recipe(
        self, recipe_create_request: RecipeCreateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        """Creates a new shoe record based on the received data"""

        create_recipe_entity = RecipeMapper.map_create_to_entity(recipe_create_request)
        recipe_entity = self._recipe_repository.create_recipe(create_recipe_entity)
        return RecipeMapper.map_entity_to_response(recipe_entity)
    
    def update_recipe(
        self, recipe_update_request: RecipeUpdateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        """Applies partial updates to an existing recipe record."""

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
        """Deletes existing shoe record by ID."""

        is_deleted = self._recipe_repository.delete_recipe(recipe_delete_id)

        if (is_deleted):
            return RecipeMapper.map_delete_to_response(recipe_delete_id)
        else:
            return RecipeMapper.map_error_to_response(
                "Cannot delete. Recipe not found", recipe_delete_id
            )
