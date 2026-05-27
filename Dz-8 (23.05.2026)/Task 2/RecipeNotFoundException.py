class RecipeNotFoundException(Exception):
    """Exception raised when a recipe is not found."""

    def __init__(self, recipe_id: int) -> None:
        self.recipe_id = recipe_id
        self.message = f"Recipes not found (ID {recipe_id})"
        super().__init__(self.message)