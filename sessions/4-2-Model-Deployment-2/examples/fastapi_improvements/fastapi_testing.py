
from fastapi.testclient import TestClient
from fastapi_error_handling import app  # Import your FastAPI app

client = TestClient(app)

def test_get_book_success():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"book_id": 1, "title": "1984"}

def test_get_book_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

