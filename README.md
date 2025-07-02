This is a FastAPI-based backend API for managing events and attendees. It features clear separation of concerns, modular structure, async database interactions, and automated testing.

### Prerequisites
- Python 3.11+

### Installation

Create and activate a virtual environment:

```bash
python3.11 -m venv env
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Database Initialization

Initialize database migrations:

```bash
alembic upgrade head
```

## Running the Application

Start the local server:

```bash
uvicorn app.main:app --reload --port 8001
```

The API will be accessible at:
- [Swagger UI Documentation](http://localhost:8001/docs)
- [OpenAPI JSON](http://localhost:8001/openapi.json)

## Testing

Run tests using pytest:

```bash
pytest app/tests
```

## Features

### API Endpoints
- `POST /events`: Create a new event
- `GET /events`: Retrieve upcoming events
- `POST /events/{event_id}/register`: Register an attendee (with checks for duplicates and max capacity)
- `GET /events/{event_id}/attendees`: Retrieve attendees with pagination

### Bonus Features
- Asynchronous implementation
- Pagination
- Automated unit tests with pytest
- Automated Swagger/OpenAPI documentation
- Database migrations with Alembic

## Environment Variables

Manage configurations via `.env` file:

```env
DATABASE_URL=sqlite+aiosqlite:///./events.db
ENVIRONMENT=development
```