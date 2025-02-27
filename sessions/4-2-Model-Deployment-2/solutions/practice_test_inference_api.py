from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_successful_response():
    """Test for a successful response"""

    body = {"message": "The meaning of life is", "max_length": 50}
    response = client.post("/chat", json=body)

    assert response.status_code == 200
    json_response = response.json()
    assert "response" in json_response
    assert json_response["response"].startswith(body["message"])


def test_too_large_max_length():
    """Test a too large max_length parameter"""

    body = {"message": "The meaning of life is", "max_length": 500}
    response = client.post("/chat", json=body)
    assert response.status_code == 422


def test_max_length_greater_than_message():
    """Test a greater max_length than message allows"""

    body = {"message": "The meaning of life is", "max_length": 4}
    response = client.post("/chat", json=body)
    assert response.status_code == 422
