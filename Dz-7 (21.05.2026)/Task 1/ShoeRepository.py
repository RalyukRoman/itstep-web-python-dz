from ShoeEntity import ShoeEntity

class ShoeRepository:
    """A repository for storing and retrieving shoe entities."""

    def __init__(self) -> None:
        self._db = []
        self._next_id = 1

    def get_all_shoes(self) -> list[ShoeEntity]:
        """Retrieves all currently stored shoe records."""
        return self._db

    def get_shoe(self, shoe_id: int) -> ShoeEntity | None:
        """Searches for a specific shoe by its unique identifier."""
        return next(
            (shoe for shoe in self._db if shoe.id == shoe_id), 
            None
        )

    def create_shoe(self, shoe: ShoeEntity) -> ShoeEntity:
        """Assigns auto-incremented ID to the new shoe entityand persists it."""

        shoe.id = self._next_id
        self._next_id += 1
        self._db.append(shoe)

        return shoe
    
    def update_shoe(self, new_shoe: ShoeEntity) -> ShoeEntity | bool:
        """Finds an existing shoe by its ID and replaces it with the updated entity."""

        index = next(
            (i for i, shoe in enumerate(self._db) if shoe.id == new_shoe.id),
            None
        )

        if index is None:
            return False
        
        self._db[index] = new_shoe
        return new_shoe
    
    def delete_shoe(self, shoe_id: int) -> bool:
        """Removes a shoe entity from the database using its ID."""
        
        shoe = self.get_shoe(shoe_id)

        if shoe is None:
            return False
        
        self._db.remove(shoe)
        return True