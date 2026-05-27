from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from ShoeNotFoundException import ShoeNotFoundException
from ShoeRepository import ShoeRepository
from ShoeRequest import ShoeRequest
from ShoeResponse import ShoeResponse
from ShoeService import ShoeService

app = FastAPI()

shoe_repository = ShoeRepository()
shoe_service = ShoeService(shoe_repository)

@app.exception_handler(ShoeNotFoundException)
async def shoe_not_found_exception_handler(
    request: Request, 
    exc: ShoeNotFoundException
) -> JSONResponse:
    """Custom exception handler for ShoeNotFoundException."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": exc.message}
    )

@app.get("/shoes/")
def get_shoes() -> list[ShoeResponse]:
    """Retrieves all shoe entities from repository."""
    return shoe_service.get_all_shoes()

@app.get("/shoes/{shoe_id}")
def get_shoe(shoe_id: int) -> ShoeResponse:
    """Retrieves a single shoe by ID."""
    return shoe_service.get_shoe(shoe_id)

@app.post("/shoes/")
def create_shoe(shoe_request: ShoeRequest) -> ShoeResponse:
    """Creates a new shoe record based on the received data."""
    return shoe_service.create_shoe(shoe_request)

@app.put("/shoes/{shoe_id}")
def update_shoe(shoe_id: int, shoe_request: ShoeRequest) -> ShoeResponse:
    """Applies partial updates to an existing shoe record."""
    return shoe_service.update_shoe(shoe_id, shoe_request)

@app.delete("/shoes/{shoe_id}")
def delete_shoe(shoe_id: int) -> int:
    """Deletes existing shoe record by ID."""
    return shoe_service.delete_shoe(shoe_id)
