from ShoeService import ShoeService
from ShoeConsoleView import ShoeConsoleView
from ShoeErrorResponse import ShoeErrorResponse

class ShoeConsoleController:
    """
    Controller class that coordinates data flow between the ShoeService 
    (Business Logic) and the ShoeConsoleView (UI Layer).
    """
    
    def __init__(
        self, shoe_service: ShoeService, shoe_view: ShoeConsoleView
    ) -> None:
        self._shoe_service = shoe_service
        self._shoe_view = shoe_view

    def get_and_display_shoe(self) -> None:
        """Prompts the user for a shoe ID, fetches the shoe data, and displays it."""
        
        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            shoe_response = self._shoe_service.get_shoe(shoe_id)

            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(shoe_response.message)
            else:
                self._shoe_view.display_shoe(shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(f"Error: {e}")

    def create_shoe_interactive(self) -> None:
        """Creates a shoe record based on user input."""

        try:
            create_request = self._shoe_view.get_shoe_create_input()
            shoe_response = self._shoe_service.create_shoe(create_request)

            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(shoe_response.message)
            else:
                self._shoe_view.display_success("Shoe has been successfully added!")
                self._shoe_view.display_shoe(shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(f"Error: {e}")

    def update_shoe_interactive(self) -> None:
        """Updates an existing shoe record based on user input."""

        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            update_request = self._shoe_view.get_shoe_update_input()
            update_request.id = shoe_id
            shoe_response = self._shoe_service.update_shoe(update_request)
            
            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(shoe_response.message)
            else:
                self._shoe_view.display_success("Shoe successfully updated!")
                self._shoe_view.display_shoe(shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(f"Error: {e}")
    
    def delete_shoe(self) -> None:
        """Deletes a shoe record by its ID."""

        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            delete_response = self._shoe_service.delete_shoe(shoe_id)

            if isinstance(delete_response, ShoeErrorResponse):
                self._shoe_view.display_error(delete_response.message)
            else:
                self._shoe_view.display_deletion_result(delete_response)

        except Exception as e:
            self._shoe_view.display_error_message(f"Error: {e}")
