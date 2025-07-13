import pytest
from httpx import AsyncClient, ASGITransport
from backend.main import app
from backend.database import get_db
from backend.test_database import override_get_db, create_test_db

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module", autouse=True)
async def setup_test_db():
    await create_test_db()

@pytest.mark.anyio
async def test_create_task():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/tasks", json={"title": "Write tests"})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Write tests"
        assert "id" in data

@pytest.mark.anyio
async def test_read_tasks():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/tasks")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

