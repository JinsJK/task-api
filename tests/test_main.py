import pytest
from httpx import AsyncClient
from backend.main import app

@pytest.mark.anyio
async def test_read_tasks():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/tasks")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.anyio
async def test_create_task():
    new_task = {"title": "Write tests"}  # Do not pass 'id'; the DB auto-generates it
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/tasks", json=new_task)
        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["title"] == "Write tests"
