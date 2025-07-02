import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_attendee():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First, create an event
        event_response = await ac.post("/events", json={
            "name": "Full Stack Hackathon",
            "location": "Mumbai",
            "start_time": "2025-08-03T10:00:00",
            "end_time": "2025-08-03T13:00:00",
            "max_capacity": 2
        })
        event = event_response.json()
        event_id = event["id"]
        assert event_response.status_code == 200

        # Register the first attendee
        response = await ac.post(f"/events/{event_id}/register", json={
            "name": "Akash Singh",
            "email": "akash@example.com"
        })
        assert response.status_code == 200
        attendee = response.json()
        assert attendee["name"] == "Akash Singh"
        assert attendee["email"] == "akash@example.com"

        # Register the second attendee
        response = await ac.post(f"/events/{event_id}/register", json={
            "name": "Bikash Prasad",
            "email": "Bikash@example.com"
        })
        assert response.status_code == 200

        # Attempt to exceed max capacity
        response = await ac.post(f"/events/{event_id}/register", json={
            "name": "Exceeded Attendee",
            "email": "exceed@example.com"
        })
        assert response.status_code == 400
        assert response.json()["detail"] == "Event is at full capacity"

        # Attempt duplicate registration
        response = await ac.post(f"/events/{event_id}/register", json={
            "name": "Akash Singh Duplicate",
            "email": "akash@example.com"
        })
        assert response.status_code == 400
        assert response.json()["detail"] == "Attendee already registered"

@pytest.mark.asyncio
async def test_get_attendees_pagination():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create an event
        event_response = await ac.post("/events", json={
            "name": "Test Pagination Event",
            "location": "Test Bangalore",
            "start_time": "2025-09-01T10:00:00",
            "end_time": "2025-09-01T12:00:00",
            "max_capacity": 5
        })
        event_id = event_response.json()["id"]

        # Add attendees
        attendees = [
            {"name": f"Attendee {i}", "email": f"attendee{i}@example.com"}
            for i in range(5)
        ]
        for attendee in attendees:
            response = await ac.post(f"/events/{event_id}/register", json=attendee)
            assert response.status_code == 200

        # Test pagination
        response = await ac.get(f"/events/{event_id}/attendees?skip=0&limit=3")
        assert response.status_code == 200
        assert len(response.json()) == 3

        response = await ac.get(f"/events/{event_id}/attendees?skip=3&limit=3")
        assert response.status_code == 200
        assert len(response.json()) == 2
