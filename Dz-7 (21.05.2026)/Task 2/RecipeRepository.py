from RecipeEntity import RecipeEntity

class RecipeRepository:
    """A repository for storing and retrieving recipe entities."""

    def __init__(self):
        self._db = []
        self._next_id = 1

    def get_all_recipes(self) -> list[RecipeEntity]:
        """Retrieves all currently stored recipe records."""
        return self._db

    def get_recipe(self, recipe_id: int) -> RecipeEntity | None:
        """Searches for a specific recipe by its unique identifier."""
        return next(
            (recipe for recipe in self._db if recipe.id == recipe_id), 
            None
        )

    def create_recipe(self, recipe: RecipeEntity) -> RecipeEntity:
        """Assigns auto-incremented ID to the new recipe entity and persists it."""

        recipe.id = self._next_id
        self._next_id += 1
        self._db.append(recipe)

        return recipe
    
    def update_recipe(self, new_recipe: RecipeEntity) -> RecipeEntity | bool:
        """Finds an existing recipe by its ID and replaces it with the updated entity."""

        index = next(
            (i for i, recipe in enumerate(self._db) if recipe.id == new_recipe.id),
            None
        )

        if index is None:
            return False
        
        self._db[index] = new_recipe
        return new_recipe
    
    def delete_recipe(self, recipe_id: int) -> bool:
        """Removes a recipe entity from the database using its ID."""

        recipe = self.get_recipe(recipe_id)

        if recipe is None:
            return False
        
        self._db.remove(recipe)
        return True