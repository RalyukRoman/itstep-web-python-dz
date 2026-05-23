from RecipeEntity import RecipeEntity

class RecipeRepository:
    def __init__(self):
        self._db = []
        self._next_id = 1

    def get_all_recipes(
        self
    ) -> list[RecipeEntity]:
        return self._db

    def get_recipe(
        self, recipe_id: int
    ) -> RecipeEntity | None:
        return next((
            recipe for recipe in self._db 
                if recipe.id == recipe_id), 
            None)

    def create_recipe(
        self, recipe: RecipeEntity
    ) -> RecipeEntity:
        recipe.id = self._next_id
        self._next_id += 1
        self._db.append(recipe)
        return recipe
    
    def update_recipe(
        self, new_recipe: RecipeEntity
    ) -> RecipeEntity | bool:
        index = next((
            i for i, recipe in enumerate(self._db) 
                if recipe.id == new_recipe.id),
            None)
        if index is None:
            return False
        self._db[index] = new_recipe
        return new_recipe
    
    def delete_recipe(
        self, recipe_id: int
    ) -> bool:
        recipe = self.get_recipe(recipe_id)
        if recipe is None:
            return False
        self._db.remove(recipe)
        return True