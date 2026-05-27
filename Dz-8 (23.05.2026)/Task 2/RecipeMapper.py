from dataclasses import replace
from RecipeEntity import RecipeEntity
from RecipeRequest import RecipeRequest
from RecipeResponse import RecipeResponse
from RecipeDTO import RecipeDTO

class RecipeMapper:
    """Maps between entities and data transfer objects."""

    @staticmethod
    def map_request_to_dto(recipe_request: RecipeRequest) -> RecipeDTO:
        """Converts a RecipeRequest object to a RecipeDTO object."""
        return RecipeDTO.model_validate(recipe_request)
    
    @staticmethod
    def map_dto_to_entity(recipe_dto: RecipeDTO) -> RecipeDTO:
        """Converts a RecipeDTO object to a RecipeEntity object."""
        return RecipeEntity.model_validate(recipe_dto)

    @staticmethod
    def map_entity_to_response(
        recipe_id: int, recipe_entity: RecipeEntity
    ) -> RecipeResponse:
        """Converts a domain RecipeEntity into an outgoing structured RecipeResponse."""
        recipe_data = recipe_entity.model_dump()
        recipe_data["id"] = recipe_id
        return RecipeResponse.model_validate(recipe_data)
    
    @staticmethod
    def map_entities_to_responses(
        recipe_entities_dict: dict[int, RecipeEntity]
    ) -> list[RecipeResponse]:
        """Transforms a collection of domain entities into a list of response."""
        return [
            RecipeMapper.map_entity_to_response(recipe_id, recipe_entity) 
            for recipe_id, recipe_entity in recipe_entities_dict.items()
        ]
    


