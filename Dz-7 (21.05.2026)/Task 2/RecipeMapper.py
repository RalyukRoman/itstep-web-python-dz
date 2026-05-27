from datetime import datetime
from dataclasses import replace
from RecipeEntity import RecipeEntity
from RecipeCreateRequest import RecipeCreateRequest
from RecipeUpdateRequest import RecipeUpdateRequest
from RecipeResponse import RecipeResponse
from RecipeDeleteResponse import RecipeDeleteResponse
from RecipeErrorResponse import RecipeErrorResponse

class RecipeMapper:
    """Utility class to convert between domain entities and data transfer objects."""

    @staticmethod
    def map_create_to_entity(
        recipe_create_request: RecipeCreateRequest
    ) -> RecipeEntity:
        """Converts a RecipeCreateRequest object to a RecipeEntity object."""

        return RecipeEntity(
            name = recipe_create_request.name,
            author = recipe_create_request.author,
            type = recipe_create_request.type,
            description = recipe_create_request.description,
            link_video = recipe_create_request.link_video,
            ingredients = recipe_create_request.ingredients,
            cuisine = recipe_create_request.cuisine
        )
    
    @staticmethod
    def map_update_to_entity(
        recipe_update_request: RecipeUpdateRequest,
        old_recipe: RecipeEntity
    ) -> RecipeEntity:
        """Merges an update request into an existing domain entity."""

        update_data = {
            k: v for k, v in recipe_update_request.__dict__.items() 
            if v is not None
        }
        return replace(old_recipe, **update_data)

    @staticmethod
    def map_entity_to_response(
        recipe_entity: RecipeEntity
    ) -> RecipeResponse:
        """Converts a domain RecipeEntity into an outgoing structured RecipeResponse."""

        return RecipeResponse(
            id = recipe_entity.id,
            name = recipe_entity.name,
            author = recipe_entity.author,
            type = recipe_entity.type,
            description = recipe_entity.description,
            link_video = recipe_entity.link_video,
            ingredients = recipe_entity.ingredients,
            cuisine = recipe_entity.cuisine,
            timestamp = datetime.now()
        )
    
    @staticmethod
    def map_entities_to_list_response(
        recipe_entities: list[RecipeEntity]
    ) -> list[RecipeResponse]:
        """Transforms a collection of domain entities into a list of response."""
        return [
            RecipeMapper.map_entity_to_response(recipe) 
            for recipe in recipe_entities
        ]
    
    @staticmethod
    def map_delete_to_response(
        recipe_id: int
    ) -> RecipeDeleteResponse:
        """Constructs a deletion response confirmation for a given resource ID."""
        return RecipeDeleteResponse(
            id = recipe_id,
            timestamp = datetime.now()
        )
    
    @staticmethod
    def map_error_to_response(
        message: str, 
        recipe_id: int | None = None
    ) -> RecipeErrorResponse:
        """Wraps an error message and context ID into a standardized error response."""
        return RecipeErrorResponse(
            id = recipe_id,
            message = message,
            timestamp = datetime.now()
        )

