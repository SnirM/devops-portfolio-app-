from httpx import Client
from app.main import app


def test_health():
    with Client(app=app, base_url="http://test") as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
