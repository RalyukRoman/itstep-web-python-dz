from dataclasses import replace
from ShoeEntity import ShoeEntity
from ShoeRequest import ShoeRequest
from ShoeResponse import ShoeResponse
from ShoeDTO import ShoeDTO

class ShoeMapper:
    """Maps between entities and data transfer objects."""

    @staticmethod
    def map_request_to_dto(shoe_request: ShoeRequest) -> ShoeDTO:
        """Converts a ShoeRequest object to a ShoeDTO object."""
        return ShoeDTO.model_validate(shoe_request)
    
    @staticmethod
    def map_dto_to_entity(shoe_dto: ShoeDTO) -> ShoeDTO:
        """Converts a ShoeDTO object to a ShoeEntity object."""
        return ShoeEntity.model_validate(shoe_dto)

    @staticmethod
    def map_entity_to_response(
        shoe_id: int, shoe_entity: ShoeEntity
    ) -> ShoeResponse:
        """Converts a domain ShoeEntity into an outgoing structured ShoeResponse."""
        shoe_data = shoe_entity.model_dump()
        shoe_data["id"] = shoe_id
        return ShoeResponse.model_validate(shoe_data)
    
    @staticmethod
    def map_entities_to_responses(
        shoe_entities_dict: dict[int, ShoeEntity]
    ) -> list[ShoeResponse]:
        """Transforms a collection of domain entities into a list of response."""
        return [
            ShoeMapper.map_entity_to_response(shoe_id, shoe_entity) 
            for shoe_id, shoe_entity in shoe_entities_dict.items()
        ]
    


