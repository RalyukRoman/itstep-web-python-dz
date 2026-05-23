from datetime import datetime
from dataclasses import replace
from ShoeEntity import ShoeEntity
from ShoeCreateRequest import ShoeCreateRequest
from ShoeUpdateRequest import ShoeUpdateRequest
from ShoeResponse import ShoeResponse
from ShoeDeleteResponse import ShoeDeleteResponse
from ShoeErrorResponse import ShoeErrorResponse

class ShoeMapper:
    @staticmethod
    def map_create_to_entity(
        shoe_create_request: ShoeCreateRequest
    ) -> ShoeEntity:
        return ShoeEntity(
            gender_type = shoe_create_request.gender_type,
            shoe_type = shoe_create_request.shoe_type,
            color = shoe_create_request.color,
            price = shoe_create_request.price,
            manufacturer = shoe_create_request.manufacturer,
            size = shoe_create_request.size
        )
    
    @staticmethod
    def map_update_to_entity(
        shoe_update_request: ShoeUpdateRequest,
        old_shoe: ShoeEntity
    ) -> ShoeEntity:
        update_data = {
            k: v for k, v in shoe_update_request.__dict__.items() 
            if v is not None
        }
        return replace(old_shoe, **update_data)

    @staticmethod
    def map_entity_to_response(
        shoe_entity: ShoeEntity
    ) -> ShoeResponse:
        return ShoeResponse(
            id = shoe_entity.id,
            gender_type = shoe_entity.gender_type,
            shoe_type = shoe_entity.shoe_type,
            color = shoe_entity.color,
            price = shoe_entity.price,
            manufacturer = shoe_entity.manufacturer,
            size = shoe_entity.size,
            timestamp = datetime.now()
        )
    
    @staticmethod
    def map_entities_to_list_response(
        shoe_entities: list[ShoeEntity]
    ) -> list[ShoeResponse]:
        return [
            ShoeMapper.map_entity_to_response(shoe) 
            for shoe in shoe_entities
        ]
    
    @staticmethod
    def map_delete_to_response(
        shoe_id: int
    ) -> ShoeDeleteResponse:
        return ShoeDeleteResponse(
            id = shoe_id,
            timestamp = datetime.now()
        )
    
    @staticmethod
    def map_error_to_response(
        message: str, 
        shoe_id: int | None = None
    ) -> ShoeErrorResponse:
        return ShoeErrorResponse(
            id = shoe_id,
            message = message,
            timestamp = datetime.now()
        )

