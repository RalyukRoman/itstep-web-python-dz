from ShoeRepository import ShoeRepository
from ShoeCreateRequest import ShoeCreateRequest
from ShoeUpdateRequest import ShoeUpdateRequest
from ShoeMapper import ShoeMapper
from ShoeResponse import ShoeResponse
from ShoeDeleteResponse import ShoeDeleteResponse
from ShoeErrorResponse import ShoeErrorResponse

class ShoeService:
    """
    Service layer class that implements business logic rules and bridges 
    communication between the Repository layer and the Controller layer.
    """

    def __init__(self, shoe_repository: ShoeRepository) -> None:
        self._shoe_repository = shoe_repository

    def get_all_shoes(self) -> list[ShoeResponse]:
        """Retrieves all shoe entities from repository."""

        all_shoes_entity = self._shoe_repository.get_all_shoes()
        return ShoeMapper.map_entities_to_list_response(all_shoes_entity)

    def get_shoe(
        self, shoe_get_id: int
    ) -> ShoeResponse | ShoeErrorResponse:
        """Retrieves a single shoe by ID"""
        
        shoe_entity = self._shoe_repository.get_shoe(shoe_get_id)

        if shoe_entity is None:
            return ShoeMapper.map_error_to_response(
                "Shoe not found", shoe_get_id
            )
        
        return ShoeMapper.map_entity_to_response(shoe_entity)

    def create_shoe(
        self, shoe_create_request: ShoeCreateRequest
    ) -> ShoeResponse | ShoeErrorResponse:
        """Creates a new shoe record based on the received data"""

        create_shoe_entity = ShoeMapper.map_create_to_entity(shoe_create_request)
        shoe_entity = self._shoe_repository.create_shoe(create_shoe_entity)
        return ShoeMapper.map_entity_to_response(shoe_entity)
    
    def update_shoe(
        self, shoe_update_request: ShoeUpdateRequest
    ) -> ShoeResponse | ShoeErrorResponse:
        """Applies partial updates to an existing shoe record."""

        old_shoe_entity = self._shoe_repository.get_shoe(shoe_update_request.id)
        
        if (old_shoe_entity is None):
            return ShoeMapper.map_error_to_response(
                "Shoe not found", shoe_update_request.id
            )
        
        update_shoe_entity = ShoeMapper.map_update_to_entity(
            shoe_update_request, old_shoe_entity
        )

        shoe_entity = self._shoe_repository.update_shoe(update_shoe_entity)
        return ShoeMapper.map_entity_to_response(shoe_entity)
    
    def delete_shoe(
        self, shoe_delete_id: int
    ) -> ShoeDeleteResponse | ShoeErrorResponse:
        """Deletes existing shoe record by ID."""

        is_deleted = self._shoe_repository.delete_shoe(shoe_delete_id)

        if (is_deleted):
            return ShoeMapper.map_delete_to_response(shoe_delete_id)
        else:
            return ShoeMapper.map_error_to_response(
                "Cannot delete. Shoe not found", shoe_delete_id
            )