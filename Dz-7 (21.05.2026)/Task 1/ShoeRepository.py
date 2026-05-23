from ShoeEntity import ShoeEntity

class ShoeRepository:
    def __init__(self):
        self._db = []
        self._next_id = 1

    def get_all_shoes(
        self
    ) -> list[ShoeEntity]:
        return self._db

    def get_shoe(
        self, shoe_id: int
    ) -> ShoeEntity | None:
        return next((
            shoe for shoe in self._db 
                if shoe.id == shoe_id), 
            None)

    def create_shoe(
        self, shoe: ShoeEntity
    ) -> ShoeEntity:
        shoe.id = self._next_id
        self._next_id += 1
        self._db.append(shoe)
        return shoe
    
    def update_shoe(
        self, new_shoe: ShoeEntity
    ) -> ShoeEntity | bool:
        index = next((
            i for i, shoe in enumerate(self._db) 
                if shoe.id == new_shoe.id),
            None)
        if index is None:
            return False
        self._db[index] = new_shoe
        return new_shoe
    
    def delete_shoe(
        self, shoe_id: int
    ) -> bool:
        shoe = self.get_shoe(shoe_id)
        if shoe is None:
            return False
        self._db.remove(shoe)
        return True