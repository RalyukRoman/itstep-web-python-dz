from RecipeResponse import RecipeResponse
from RecipeDeleteResponse import RecipeDeleteResponse
from RecipeErrorResponse import RecipeErrorResponse
from RecipeUpdateRequest import RecipeUpdateRequest
from RecipeCreateRequest import RecipeCreateRequest
from RecipeEnums import RecipeType, NameOfCuisine

class RecipeConsoleView:
    @staticmethod
    def display_recipe(
        recipe: RecipeResponse
    ) -> None:
        print("\n" + "=" * 40)
        print(f"Recipe (ID: {recipe.id})")
        print("-" * 40)
        
        print(f" Name:        {recipe.name}")
        print(f" Author:      {recipe.author}")
        print(f" Recipe type: {recipe.type.value.capitalize()}")
        print(f" Cuisine:     {recipe.cuisine.value.capitalize()}")
        print(f" Decription:  {recipe.description}")
        print(f" Link video:  {recipe.link_video}")
        print(f" Ingredients: {recipe.ingredients}")

        print("-" * 40)
        print(f" Timestamp:    {
            recipe.timestamp.strftime(
                '%Y-%m-%d %H:%M:%S')
        }")
        print("=" * 40 + "\n")

    @staticmethod
    def display_recipes_list(
        recipes: list[RecipeResponse]
    ) -> None:
        if not recipes:
            print("\nNo recipes to display\n")
            return
        
        print("\n" + "=" * 70)
        print(f"{'ID':<4} | {'Name':<10} | {'Author':<10} |",
              f"{'Type':<12} | {'Cuisine':<12}")
        print("-" * 70)

        for recipe in recipes:
            print(f"{recipe.id:<4} | "
                  f"{recipe.name:<10} | "
                  f"{recipe.author:<10} | "
                  f"{recipe.type.value[:12]:<12} | "
                  f"{recipe.cuisine.value[:12]:<12} | ")
        print("=" * 70 + "\n")

    @staticmethod
    def display_deletion_result(
        delete_response: RecipeDeleteResponse
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
        error_response: RecipeErrorResponse
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
    def get_recipe_id_input(
    ) -> int:
        while True:
            try:
                recipe_id = int(input("Enter recipe ID: "))
                if recipe_id <= 0:
                    print("ID must be greater than 0")
                    continue
                return recipe_id
            except ValueError:
                print("Please enter a valid number")
    
    @staticmethod
    def get_recipe_create_input(
    ) -> RecipeCreateRequest:
        print("\n--- DATA ENTRY FOR CREATING SHOES ---")

        name = input("Name: ")
        author = input("Author: ")
        
        print("Available categories: 1 - Italian, 2 - French, 3 - Ukrainian")
        cousine_choice = input("Choose a category (1-3): ")
        cousine_map = {
            "1": NameOfCuisine.ITALIAN, 
            "2": NameOfCuisine.FRENCH,
            "3": NameOfCuisine.UKRAINIAN
        }
        name_of_cousine = cousine_map.get(
            cousine_choice, NameOfCuisine.ITALIAN)

        print("Available types: 1 - First, 2 - Second")
        type_choice = input("Choose a view (1-2): ")
        types_map = {
            "1": RecipeType.FIRST, 
            "2": RecipeType.SECOND
        }
        recipe_type = types_map.get(
            type_choice, RecipeType.FIRST)

        description = input("Description: ")
        link_video = input("Link of video: ")

        ingredients_input = input("Ingredients (through a space): ")
        ingredients = ingredients_input.split()

        return RecipeCreateRequest(
            name = name,
            author = author,
            type = recipe_type,
            description = description,
            link_video = link_video,
            ingredients = ingredients,
            cuisine = name_of_cousine
        )

    @staticmethod
    def get_recipe_update_input(
    ) -> RecipeUpdateRequest:
        print("\n--- EDIT SHOES (press Enter to leave unchanged) ---")
        
        description_input = input("Description: ")
        description = description_input if description_input.strip() else None
        
        link_video_input = input("Link of video: ")
        link_video = link_video_input if link_video_input.strip() else None

        return RecipeUpdateRequest(
            id = 0,
            description = description,
            link_video = link_video
        )