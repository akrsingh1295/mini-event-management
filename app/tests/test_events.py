import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/events", json={
            "name": "Coding Event",
            "location": "New Delhi",
            "start_time": "2025-08-04T10:00:00",
            "end_time": "2025-08-05T12:00:00",
            "max_capacity": 50
        })
        assert response.status_code == 200
        assert response.json()["name"] == "Coding Event"