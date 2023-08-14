from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.content == b"<h1>Hello, World</h1>"