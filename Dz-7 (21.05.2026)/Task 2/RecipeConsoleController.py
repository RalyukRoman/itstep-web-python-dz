from RecipeService import RecipeService
from RecipeConsoleView import RecipeConsoleView
from RecipeErrorResponse import RecipeErrorResponse

class RecipeConsoleController:
    def __init__(
        self, 
        recipe_service: RecipeService,
        recipe_view: RecipeConsoleView
    ):
        self._recipe_service = recipe_service
        self._recipe_view = recipe_view

    def get_and_display_recipe(
        self
    ) -> None:
        try:
            recipe_id = self._recipe_view.get_recipe_id_input()
            recipe_response = self._recipe_service.get_recipe(
                recipe_id)

            if isinstance(recipe_response, RecipeErrorResponse):
                self._recipe_view.display_error(
                    recipe_response.message)
            else:
                self._recipe_view.display_recipe(recipe_response)

        except Exception as e:
            self._recipe_view.display_error_message(
                f"Error during get: {e}")

    def create_recipe_interactive(
        self
    ) -> None:
        try:
            create_request = self._recipe_view.get_recipe_create_input()
            recipe_response = self._recipe_service.create_recipe(
                create_request)

            if isinstance(recipe_response, RecipeErrorResponse):
                self._recipe_view.display_error(
                    recipe_response.message)
            else:
                self._recipe_view.display_success(
                    "The product has been successfully added to the warehouse!")
                self._recipe_view.display_recipe(recipe_response)

        except Exception as e:
            self._recipe_view.display_error_message(
                f"Error during create: {e}")

    def update_recipe_interactive(
        self
    ) -> None:
        try:
            recipe_id = self._recipe_view.get_recipe_id_input()
            update_request = self._recipe_view.get_recipe_update_input()
            update_request.id = recipe_id
            recipe_response = self._recipe_service.update_recipe(
                update_request)
            
            if isinstance(recipe_response, RecipeErrorResponse):
                self._recipe_view.display_error(
                    recipe_response.message)
            else:
                self._recipe_view.display_success(
                    "Product data successfully updated!")
                self._recipe_view.display_recipe(
                    recipe_response)

        except Exception as e:
            self._recipe_view.display_error_message(
                f"Error during update: {e}")
    
    def delete_recipe(
        self
    ) -> None:
        try:
            recipe_id = self._recipe_view.get_recipe_id_input()
            delete_response = self._recipe_service.delete_recipe(
                recipe_id)

            if isinstance(delete_response, RecipeErrorResponse):
                self._recipe_view.display_error(
                    delete_response.message)
            else:
                self._recipe_view.display_deletion_result(
                    delete_response)

        except Exception as e:
            self._recipe_view.display_error_message(
                f"Error during delete: {e}")
