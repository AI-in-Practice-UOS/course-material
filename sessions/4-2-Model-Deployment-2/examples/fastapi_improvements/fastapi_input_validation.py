from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()

class CreateBookRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1000, le=2100)
    pages: int = Field(..., gt=0)
    genre: Optional[str] = Field(None, max_length=30)

@app.post("/books")
def create_book(book: CreateBookRequest):
    return {"message": f"Book '{book.title}' successfully created"}

class CreateBookValidRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1000, le=2100)
    pages: int = Field(..., gt=0)
    genre: Optional[str] = Field(None, max_length=30)

    @field_validator("year")
    @classmethod
    def validate_even_year(cls, year):
        """Ensure that the year is an even number."""
        if year % 2 != 0:
            raise ValueError("Year must be an even number")
        return year

    @model_validator(mode="after")
    def validate_science_fiction_year(self):
        """Ensure that Science Fiction books are from 1950 or later."""
        if self.genre and self.genre.lower() == "science fiction" and self.year < 1950:
            raise ValueError("Science Fiction books must be published in 1950 or later")
        return self

@app.post("/books/validated")
def create_validated_book(book: CreateBookValidRequest):
    return {"message": f"Book '{book.title}' successfully created"}

