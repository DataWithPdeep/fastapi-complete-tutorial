from fastapi.testclient import TestClient
from test import app

client = TestClient(app)

# Test Home API
def test_home():
    response = client.get("/")

    # Status code check
    assert response.status_code == 200

    # Response data check
    assert response.json() == {"message": "Hello Mohit"}


# Test Add API
def test_add():
    response = client.get("/add?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}
    