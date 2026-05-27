import sys
from RecipeConsoleView import RecipeConsoleView
from RecipeConsoleController import RecipeConsoleController
from RecipeService import RecipeService
from RecipeRepository import RecipeRepository

def main() -> None:
    view = RecipeConsoleView()
    repository = RecipeRepository()
    service = RecipeService(repository)
    controller = RecipeConsoleController(service, view)

    print("=== Welcome to the Recipe Management System ===")
    while True:
        print("\nAvailable Commands:")
        print("1. View recipe by ID")
        print("2. Add new recipe")
        print("3. Edit recipe characteristics")
        print("4. Delete recipe")
        print("5. View all recipes")
        print("0. Exit application")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            controller.get_and_display_recipe()
            
        elif choice == "2":
            controller.create_recipe_interactive()
            
        elif choice == "3":
            controller.update_recipe_interactive()
            
        elif choice == "4":
            controller.delete_recipe()

        elif choice == "5":
            all_recipes = service.get_all_recipes()
            view.display_recipes_list(all_recipes)
            
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