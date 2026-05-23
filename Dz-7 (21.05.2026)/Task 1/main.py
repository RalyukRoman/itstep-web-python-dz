import sys
from ShoeConsoleView import ShoeConsoleView
from ShoeConsoleController import ShoeConsoleController
from ShoeService import ShoeService
from ShoeRepository import ShoeRepository

def main() -> None:
    view = ShoeConsoleView()
    repository = ShoeRepository()

    service = ShoeService(
        shoe_repository=repository)
    
    controller = ShoeConsoleController(
        shoe_service=service, shoe_view=view)

    print("=== Welcome to the Shoe Management System ===")
    while True:
        print("\nAvailable Commands:")
        print("1. View shoe by ID")
        print("2. Add new shoe")
        print("3. Edit shoe characteristics")
        print("4. Delete shoe")
        print("5. View all shoes")
        print("0. Exit application")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            controller.get_and_display_shoe()
            
        elif choice == "2":
            controller.create_shoe_interactive()
            
        elif choice == "3":
            controller.update_shoe_interactive()
            
        elif choice == "4":
            controller.delete_shoe()

        elif choice == "5":
            all_shoes = service.get_all_shoes()
            view.display_shoes_list(all_shoes)
            
        elif choice == "0":
            print("\nShutting down. Thank you for using our system!")
            sys.exit(0)
            
        else:
            print("\n[WARNING]: Invalid option. Please enter a number from 0 to 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
        sys.exit(0)