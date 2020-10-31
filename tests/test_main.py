from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hola": "Mundo"}


def test_read_health_check():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"Message": "DIPLOMA API V1 - Up and running!!!"}
