from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.event import EventCreate
from app.schemas.attendee import AttendeeCreate
from app.services import event_service, attendee_service
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/events")
async def create_event(event: EventCreate, db: AsyncSession = Depends(get_db)):
    return await event_service.create_event(db, event)

@router.get("/events")
async def list_events(db: AsyncSession = Depends(get_db)):
    return await event_service.list_upcoming_events(db)

@router.post("/events/{event_id}/register")
async def register_attendee(event_id: int, attendee: AttendeeCreate, db: AsyncSession = Depends(get_db)):
    return await attendee_service.register_attendee(db, event_id, attendee)

@router.get("/events/{event_id}/attendees")
async def get_attendees(event_id: int, db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = Query(10)):
    return await attendee_service.get_attendees(db, event_id, skip, limit)
