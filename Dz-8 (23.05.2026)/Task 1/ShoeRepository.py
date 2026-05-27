from ShoeEntity import ShoeEntity
from ShoeDTO import ShoeDTO
from ShoeMapper import ShoeMapper

class ShoeRepository:
    """A repository for shoes."""

    def __init__(self) -> None:
        self._db: dict[int, ShoeEntity] = {}
        self._next_id = 1

    def get_all_shoes(self) -> dict[int, ShoeEntity]:
        """Retrieves all currently stored shoe records."""
        return self._db

    def get_shoe(
        self, shoe_id: int
    ) -> tuple[int | None, ShoeEntity | None]:
        """Searches for a specific shoe by its unique identifier."""
        
        if shoe_id not in self._db:
            return None, None
        return shoe_id, self._db.get(shoe_id)

    def create_shoe(
        self, shoe_dto: ShoeDTO
    ) -> tuple[int, ShoeEntity]:
        """Assigns auto-incremented ID to the new shoe entityand persists it."""
        
        shoe_entity = ShoeMapper.map_dto_to_entity(shoe_dto)
        current_id = self._next_id

        self._db[current_id] = shoe_entity
        self._next_id += 1

        return current_id, shoe_entity
    
    def update_shoe(
        self, shoe_id: int, shoe_dto: ShoeDTO
    ) -> tuple[int | None, ShoeEntity | None]: 
        """Finds an existing shoe by its ID and replaces it with the updated entity."""
        
        if shoe_id not in self._db:
            return None, None
        
        shoe_entity = ShoeMapper.map_dto_to_entity(shoe_dto)
        self._db[shoe_id] = shoe_entity
        
        return shoe_id, shoe_entity
    
    def delete_shoe(
        self, shoe_id: int
    ) -> int | None:
        """Removes a shoe entity from the database using its ID."""

        if shoe_id not in self._db:
            return None
        
        del self._db[shoe_id]
        return shoe_id