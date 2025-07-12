from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task():
    new_task = {"id": 3, "title": "Write tests"}
    response = client.post("/tasks", json=new_task)
    assert response.status_code == 200
    assert response.json()["id"] == 3
