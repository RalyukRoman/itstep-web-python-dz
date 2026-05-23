from ShoeResponse import ShoeResponse
from ShoeDeleteResponse import ShoeDeleteResponse
from ShoeErrorResponse import ShoeErrorResponse
from ShoeUpdateRequest import ShoeUpdateRequest
from ShoeCreateRequest import ShoeCreateRequest
from ShoeEnums import GenderType, ShoeKind

class ShoeConsoleView:
    @staticmethod
    def display_shoe(
        shoe: ShoeResponse
    ) -> None:
        print("\n" + "=" * 40)
        print(f"Shoe (ID: {shoe.id})")
        print("-" * 40)
        
        print(f" Gender type:  {shoe.gender_type.value.capitalize()}")
        print(f" Shoe type:    {shoe.shoe_type.value.capitalize()}")
        print(f" Manufacturer: {shoe.manufacturer}")
        print(f" Color:        {shoe.color}")
        print(f" Size:         {shoe.size}")
        print(f" Price:        {shoe.price:,.2f}")

        print("-" * 40)
        print(f" Timestamp:    {
            shoe.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
        }")
        print("=" * 40 + "\n")

    @staticmethod
    def display_shoes_list(
        shoes: list[ShoeResponse]
    ) -> None:
        if not shoes:
            print("\nNo shoes to display\n")
            return
        
        print("\n" + "=" * 76)
        print(f"{'ID':<4} | {'Gender type':<10} | {'Shoe type':<12} |",
              f"{'Manufacture':<12} | {'Size':<6} | {'Price':<10}")
        print("-" * 76)

        for shoe in shoes:
            print(f"{shoe.id:<4} | "
                  f"{shoe.gender_type.value[:10]:<10} | "
                  f"{shoe.shoe_type.value[:12]:<12} | "
                  f"{shoe.manufacturer[:12]:<12} | "
                  f"{shoe.size:<6} | "
                  f"{shoe.price:<10,.2f}")
        print("=" * 76 + "\n")

    @staticmethod
    def display_deletion_result(
        delete_response: ShoeDeleteResponse
    ) -> None:
        print("\n" + "-" * 45)
        print(f"[SUCCESSFUL DELETE] — ID: {delete_response.id}")
        print(f"Timestamp: {
            delete_response.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
        }")
        print("-" * 45 + "\n")

    @staticmethod
    def display_error_message(
        message: str
    ) -> None:
        print(f"\n[ERROR]: {message}\n")

    @staticmethod
    def display_error(
        error_response: ShoeErrorResponse
    ) -> None:
        print(f"\n[ERROR]: {error_response.message}\n")
        print(f"Timestamp: {
            error_response.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
        }")

    @staticmethod
    def display_success(
        message: str
    ) -> None:
        print(f"\n[SUCCESS]: {message}\n")

    @staticmethod
    def get_shoe_id_input(
    ) -> int:
        while True:
            try:
                shoe_id = int(input("Enter shoe ID: "))
                if shoe_id <= 0:
                    print("ID must be greater than 0")
                    continue
                return shoe_id
            except ValueError:
                print("Please enter a valid number")
    
    @staticmethod
    def get_shoe_create_input(
    ) -> ShoeCreateRequest:
        print("\n--- DATA ENTRY FOR CREATING SHOES ---")
        
        print("Available categories: 1 - Men's, 2 - Women's")
        gender_choice = input("Choose a category (1 or 2): ")
        gender_type = GenderType.MALE if gender_choice == "1" else GenderType.FEMALE

        print("Available types: 1 - Sneakers, 2 - Boots, 3 - Sandals, 4 - Shoes")
        kind_choice = input("Choose a view (1-4): ")
        kinds_map = {
            "1": ShoeKind.SNEAKERS, 
            "2": ShoeKind.BOOTS, 
            "3": ShoeKind.SANDALS, 
            "4": ShoeKind.SHOES
        }
        shoe_type = kinds_map.get(
            kind_choice, ShoeKind.SHOES)

        color = input("Color: ")
        manufacturer = input("Manufacturer: ")

        while True:
            try:
                size = float(input("Size: "))
                if size <= 0:
                    print("Size must be greater than 0")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for size")

        while True:
            try:
                price = float(input("Price ($): "))
                if price < 0:
                    print("Price cannot be negative")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for price")

        return ShoeCreateRequest(
            gender_type = gender_type,
            shoe_type = shoe_type,
            color = color,
            price = price,
            manufacturer = manufacturer,
            size = size
        )

    @staticmethod
    def get_shoe_update_input(
    ) -> ShoeUpdateRequest:
        print("\n--- EDIT SHOES (press Enter to leave unchanged) ---")
        
        color_input = input("New color: ")
        color = color_input if color_input.strip() else None

        price = None
        while True:
            price_input = input("New price: ").strip()
            if not price_input:
                break
            try:
                price = float(price_input)
                if price < 0:
                    print("Price cannot be negative")
                    continue
                break
            except ValueError:
                print("Please enter a valid number or press Enter")

        size = None
        while True:
            size_input = input("New size: ").strip()
            if not size_input:
                break
            try:
                size = float(size_input)
                if size <= 0:
                    print("Size must be greater than 0")
                    continue
                break
            except ValueError:
                print("Please enter a valid number or press Enter")

        return ShoeUpdateRequest(
            id = 0,
            color = color,
            price = price,
            size = size
        )