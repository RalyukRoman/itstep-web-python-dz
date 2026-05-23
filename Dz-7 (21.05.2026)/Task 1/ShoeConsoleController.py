from ShoeService import ShoeService
from ShoeConsoleView import ShoeConsoleView
from ShoeErrorResponse import ShoeErrorResponse

class ShoeConsoleController:
    def __init__(
        self, 
        shoe_service: ShoeService,
        shoe_view: ShoeConsoleView
    ):
        self._shoe_service = shoe_service
        self._shoe_view = shoe_view

    def get_and_display_shoe(
        self
    ) -> None:
        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            shoe_response = self._shoe_service.get_shoe(
                shoe_id)

            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(
                    shoe_response.message)
            else:
                self._shoe_view.display_shoe(shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(
                f"Error during get: {e}")

    def create_shoe_interactive(
        self
    ) -> None:
        try:
            create_request = self._shoe_view.get_shoe_create_input()
            shoe_response = self._shoe_service.create_shoe(
                create_request)

            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(
                    shoe_response.message)
            else:
                self._shoe_view.display_success(
                    "The product has been successfully added to the warehouse!")
                self._shoe_view.display_shoe(shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(
                f"Error during create: {e}")

    def update_shoe_interactive(
        self
    ) -> None:
        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            update_request = self._shoe_view.get_shoe_update_input()
            update_request.id = shoe_id
            shoe_response = self._shoe_service.update_shoe(
                update_request)
            
            if isinstance(shoe_response, ShoeErrorResponse):
                self._shoe_view.display_error(
                    shoe_response.message)
            else:
                self._shoe_view.display_success(
                    "Product data successfully updated!")
                self._shoe_view.display_shoe(
                    shoe_response)

        except Exception as e:
            self._shoe_view.display_error_message(
                f"Error during update: {e}")
    
    def delete_shoe(
        self
    ) -> None:
        try:
            shoe_id = self._shoe_view.get_shoe_id_input()
            delete_response = self._shoe_service.delete_shoe(
                shoe_id)

            if isinstance(delete_response, ShoeErrorResponse):
                self._shoe_view.display_error(
                    delete_response.message)
            else:
                self._shoe_view.display_deletion_result(
                    delete_response)

        except Exception as e:
            self._shoe_view.display_error_message(
                f"Error during delete: {e}")
