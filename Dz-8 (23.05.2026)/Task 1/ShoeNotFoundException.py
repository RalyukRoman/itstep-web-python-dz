class ShoeNotFoundException(Exception):
    """Exception raised when a shoe is not found."""

    def __init__(self, shoe_id: int) -> None:
        self.shoe_id = shoe_id
        self.message = f"Shoes not found (ID {shoe_id})"
        super().__init__(self.message)