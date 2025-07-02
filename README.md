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

# POSTMAN Curl
# Registering an Event
curl --location 'http://localhost:8001/events' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "name": "Wimbeldon",
  "location": "France",
  "start_time": "2025-07-10T07:47:19.193Z",
  "end_time": "2025-07-14T08:47:19.193Z",
  "max_capacity": 15
}'


# get the list of all attendeess of the event
curl --location 'http://localhost:8001/events/2/attendees?skip=0&limit=15' \
--header 'accept: application/json'

[
    {
        "event_id": 2,
        "name": "Roger federer",
        "email": "roger@gmail.com.com",
        "id": 6
    },
    {
        "event_id": 2,
        "name": "Maria sharapoa",
        "email": "maria@gmail.com.com",
        "id": 7
    },
    {
        "event_id": 2,
        "name": "rafal nadal",
        "email": "rafal@gmail.com.com",
        "id": 8
    },
    {
        "event_id": 2,
        "name": "bupendra",
        "email": "bhupendra@gmail.com.com",
        "id": 9
    },
    {
        "event_id": 2,
        "name": "sachin",
        "email": "sachin@gmail.com.com",
        "id": 10
    },
    {
        "event_id": 2,
        "name": "kevin",
        "email": "kevin@gmail.com.com",
        "id": 11
    },
    {
        "event_id": 2,
        "name": "David",
        "email": "davic@gmail.com.com",
        "id": 12
    },
    {
        "event_id": 2,
        "name": "Alastair",
        "email": "alastair@gmail.com.com",
        "id": 13
    },
    {
        "event_id": 2,
        "name": "Pete Sampras",
        "email": "Pete@gmail.com.com",
        "id": 14
    },
    {
        "event_id": 2,
        "name": "John McEnroe",
        "email": "John@gmail.com.com",
        "id": 15
    },
    {
        "event_id": 2,
        "name": "Carlos Alcaraz",
        "email": "Carlos@gmail.com.com",
        "id": 16
    },
    {
        "event_id": 2,
        "name": "Jannik Sinner",
        "email": "Jannik@gmail.com.com",
        "id": 17
    },
    {
        "event_id": 2,
        "name": "Jimmy Connors",
        "email": "Jimmy@gmail.com.com",
        "id": 18
    },
    {
        "event_id": 2,
        "name": "Rod Laver",
        "email": "Rod@gmail.com.com",
        "id": 19
    },
    {
        "event_id": 2,
        "name": "Bjorn Borg",
        "email": "Bjorn@gmail.com",
        "id": 20
    }
]

# trying to resgister 16th attendee to an event
curl --location 'http://localhost:8001/events/2/register' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "Novak Djokovic",
  "email": "Novak@gmail.com"
}'

{
    "detail": "Event is at full capacity"
}