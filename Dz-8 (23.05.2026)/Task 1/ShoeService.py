from ShoeRepository import ShoeRepository
from ShoeRequest import ShoeRequest
from ShoeMapper import ShoeMapper
from ShoeResponse import ShoeResponse
from ShoeNotFoundException import ShoeNotFoundException

class ShoeService:
    """Service layer for shoe operations."""

    def __init__(self, shoe_repository: ShoeRepository) -> None:
        self._shoe_repository = shoe_repository

    def get_all_shoes(self) -> list[ShoeResponse]:
        """Retrieves all shoe entities from repository."""

        list_shoes_entity = self._shoe_repository.get_all_shoes()
        return ShoeMapper.map_entities_to_responses(list_shoes_entity)

    def get_shoe(self, shoe_id: int) -> ShoeResponse:
        """Retrieves a single shoe by ID."""

        _, shoe_entity = self._shoe_repository.get_shoe(shoe_id)
        if shoe_entity is None:
            raise ShoeNotFoundException(shoe_id)
        return ShoeMapper.map_entity_to_response(shoe_id, shoe_entity)

    def create_shoe(self, shoe_request: ShoeRequest) -> ShoeResponse:
        """Creates a new shoe entity."""

        shoe_dto = ShoeMapper.map_request_to_dto(shoe_request)
        shoe_id, shoe_entity = self._shoe_repository.create_shoe(shoe_dto)
        return ShoeMapper.map_entity_to_response(shoe_id, shoe_entity)
    
    def update_shoe(self, shoe_id: int, shoe_request: ShoeRequest) -> ShoeResponse:
        """Updates an existing shoe entity."""

        old_shoe_entity = self._shoe_repository.get_shoe(shoe_id)
        if old_shoe_entity is None:
            raise ShoeNotFoundException(shoe_id)
        
        shoe_dto = ShoeMapper.map_request_to_dto(shoe_request)
        _, shoe_entity = self._shoe_repository.update_shoe(shoe_id, shoe_dto)
        return ShoeMapper.map_entity_to_response(shoe_id, shoe_entity)
    
    def delete_shoe(self, shoe_id: int) -> int:
        """Deletes a shoe entity by ID."""
        
        deleted_shoe_id = self._shoe_repository.delete_shoe(shoe_id)
        if not deleted_shoe_id:
            raise ShoeNotFoundException(shoe_id)
        return deleted_shoe_id
