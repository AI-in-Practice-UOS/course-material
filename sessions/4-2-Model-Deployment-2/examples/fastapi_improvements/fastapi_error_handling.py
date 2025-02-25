from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

books_db = {1: "1984", 2: "Brave New World"}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"book_id": book_id, "title": books_db[book_id]}

class BookNotFoundException(Exception):
    def __init__(self, book_id: int):
        self.book_id = book_id

@app.exception_handler(BookNotFoundException)
async def book_not_found_handler(req: Request, exc: BookNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"error": "Book not found", "book_id": exc.book_id},
    )

@app.get("/books/custom/{book_id}")
def get_custom_book(book_id: int):
    if book_id not in books_db:
        raise BookNotFoundException(book_id)
    return {"book_id": book_id, "title": books_db[book_id]}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error"},
    )

