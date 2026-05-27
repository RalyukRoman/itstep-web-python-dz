from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from RecipeNotFoundException import RecipeNotFoundException
from RecipeRepository import RecipeRepository
from RecipeRequest import RecipeRequest
from RecipeResponse import RecipeResponse
from RecipeService import RecipeService

app = FastAPI()

recipe_repository = RecipeRepository()
recipe_service = RecipeService(recipe_repository)

@app.exception_handler(RecipeNotFoundException)
async def recipe_not_found_exception_handler(
    request: Request, 
    exc: RecipeNotFoundException
) -> JSONResponse:
    """Custom exception handler for RecipeNotFoundException."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exc.message}
    )

@app.get("/recipes/")
def get_recipes() -> list[RecipeResponse]:
    """Retrieves all recipe entities from repository."""
    return recipe_service.get_all_recipes()

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int) -> RecipeResponse:
    """Retrieves a single recipe by ID."""
    return recipe_service.get_recipe(recipe_id)

@app.post("/recipes/")
def create_recipe(recipe_request: RecipeRequest) -> RecipeResponse:
    """Creates a new recipe record based on the received data."""
    return recipe_service.create_recipe(recipe_request)

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe_request: RecipeRequest) -> RecipeResponse:
    """Applies partial updates to an existing recipe record."""
    return recipe_service.update_recipe(recipe_id, recipe_request)

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int) -> int:
    """Deletes existing recipe record by ID."""
    return recipe_service.delete_recipe(recipe_id)
