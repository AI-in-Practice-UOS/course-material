from enum import Enum

from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

# API metadata with OpenAPI details
app = FastAPI(
    title="Library API",
    description="API for managing a book collection",
    version="1.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    terms_of_service="https://example.com/terms",
    servers=[
        {"url": "https://api.example.com", "description": "Production"},
        {"url": "https://staging.example.com", "description": "Staging"},
    ],
)


# Enum for predefined choices
class Genre(str, Enum):
    fiction = "Fiction"
    nonfiction = "Non-fiction"


# Book model with metadata and example responses
class Book(BaseModel):
    """Represents a book in the library"""

    title: str = Field(..., example="1984", description="Book title")
    year: int = Field(..., example=1949, description="Publication year")
    genre: Genre = Field(..., example="Fiction", description="Book genre")

    class Config:
        schema_extra = {"example": {"title": "1984", "year": 1949, "genre": "Fiction"}}


# Error message response
class ErrorResponse(BaseModel):
    """The response to an error"""

    detail: str = Field(..., description="Error details")


# Sample database (simulated)
books_db = {
    1: Book(title="1984", year=1949, genre="Fiction"),
    2: Book(title="Sapiens", year=2011, genre="Non-fiction"),
}


# GET endpoint with response documentation and tags
@app.get(
    "/books/{book_id}",
    response_model=Book,
    summary="Retrieve a book",
    tags=["Books"],
    responses={
        200: {"description": "Book retrieved"},
        404: {"description": "Book not found", "model": ErrorResponse},
    },
)
def get_book(book_id: int) -> Book:
    """Fetch book details by ID."""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]


# POST endpoint with detailed request body documentation
@app.post("/books/", response_model=Book, summary="Create a new book", tags=["Books"])
def create_book(
    book: Book = Body(..., description="Book details to be added to the library"),
) -> Book:
    """Add a new book to the library"""
    new_id = max(books_db.keys()) + 1
    books_db[new_id] = book
    return book
