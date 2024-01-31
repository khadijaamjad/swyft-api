from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/", params={"token" : "dev1"})
    assert response.status_code == 200
    assert response.json() == {"message": "API is working!"}