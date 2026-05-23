from ShoeRepository import ShoeRepository
from ShoeCreateRequest import ShoeCreateRequest
from ShoeUpdateRequest import ShoeUpdateRequest
from ShoeMapper import ShoeMapper
from ShoeResponse import ShoeResponse
from ShoeDeleteResponse import ShoeDeleteResponse
from ShoeErrorResponse import ShoeErrorResponse

class ShoeService:
    def __init__(
        self, shoe_repository: ShoeRepository
    ):
        self._shoe_repository = shoe_repository

    def get_all_shoes(
        self
    ) -> list[ShoeResponse]:
        all_shoes_entity = self._shoe_repository.get_all_shoes()
        all_shoes_response = ShoeMapper.map_entities_to_list_response(
            all_shoes_entity)
        return all_shoes_response

    def get_shoe(
        self, shoe_get_id: int
    ) -> ShoeResponse | ShoeErrorResponse:
        shoe_entity = self._shoe_repository.get_shoe(
            shoe_get_id)
        shoe_response = ShoeMapper.map_entity_to_response(
            shoe_entity)
        return shoe_response

    def create_shoe(
        self, shoe_create_request: ShoeCreateRequest
    ) -> ShoeResponse | ShoeErrorResponse:
        shoe_entity = self._shoe_repository.create_shoe(
            ShoeMapper.map_create_to_entity(
                shoe_create_request))
        shoe_response = ShoeMapper.map_entity_to_response(
            shoe_entity)
        return shoe_response
    
    def update_shoe(
        self, shoe_update_request: ShoeUpdateRequest
    ) -> ShoeResponse | ShoeErrorResponse:
        old_shoe_entity = self._shoe_repository.get_shoe(
            shoe_update_request.id)
        if (old_shoe_entity is None):
            return ShoeMapper.map_error_to_response(
                "Shoe not found", shoe_update_request.id)
        shoe_entity = self._shoe_repository.update_shoe(
            ShoeMapper.map_update_to_entity(
                shoe_update_request, old_shoe_entity))
        shoe_response = ShoeMapper.map_entity_to_response(
            shoe_entity)
        return shoe_response
    
    def delete_shoe(
        self, shoe_delete_id: int
    ) -> ShoeDeleteResponse | ShoeErrorResponse:
        is_deleted = self._shoe_repository.delete_shoe(
            shoe_delete_id)
        if (is_deleted):
            shoe_response = ShoeMapper.map_delete_to_response(
                shoe_delete_id)
        else:
            shoe_response = ShoeMapper.map_error_to_response(
                "Cannot delete. Shoe not found", shoe_delete_id)
        return shoe_response
