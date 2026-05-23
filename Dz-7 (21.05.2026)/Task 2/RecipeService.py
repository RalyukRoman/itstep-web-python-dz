from RecipeRepository import RecipeRepository
from RecipeCreateRequest import RecipeCreateRequest
from RecipeUpdateRequest import RecipeUpdateRequest
from RecipeMapper import RecipeMapper
from RecipeResponse import RecipeResponse
from RecipeDeleteResponse import RecipeDeleteResponse
from RecipeErrorResponse import RecipeErrorResponse

class RecipeService:
    def __init__(
        self, recipe_repository: RecipeRepository
    ):
        self._recipe_repository = recipe_repository

    def get_all_recipes(
        self
    ) -> list[RecipeResponse]:
        all_recipes_entity = self._recipe_repository.get_all_recipes()
        all_recipes_response = RecipeMapper.map_entities_to_list_response(
            all_recipes_entity)
        return all_recipes_response

    def get_recipe(
        self, recipe_get_id: int
    ) -> RecipeResponse | RecipeErrorResponse:
        recipe_entity = self._recipe_repository.get_recipe(
            recipe_get_id)
        recipe_response = RecipeMapper.map_entity_to_response(
            recipe_entity)
        return recipe_response

    def create_recipe(
        self, recipe_create_request: RecipeCreateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        recipe_entity = self._recipe_repository.create_recipe(
            RecipeMapper.map_create_to_entity(
                recipe_create_request))
        recipe_response = RecipeMapper.map_entity_to_response(
            recipe_entity)
        return recipe_response
    
    def update_recipe(
        self, recipe_update_request: RecipeUpdateRequest
    ) -> RecipeResponse | RecipeErrorResponse:
        old_recipe_entity = self._recipe_repository.get_recipe(
            recipe_update_request.id)
        if (old_recipe_entity is None):
            return RecipeMapper.map_error_to_response(
                "Recipe not found", recipe_update_request.id)
        recipe_entity = self._recipe_repository.update_recipe(
            RecipeMapper.map_update_to_entity(
                recipe_update_request, old_recipe_entity))
        recipe_response = RecipeMapper.map_entity_to_response(
            recipe_entity)
        return recipe_response
    
    def delete_recipe(
        self, recipe_delete_id: int
    ) -> RecipeDeleteResponse | RecipeErrorResponse:
        is_deleted = self._recipe_repository.delete_recipe(
            recipe_delete_id)
        if (is_deleted):
            recipe_response = RecipeMapper.map_delete_to_response(
                recipe_delete_id)
        else:
            recipe_response = RecipeMapper.map_error_to_response(
                "Cannot delete. Recipe not found", recipe_delete_id)
        return recipe_response
