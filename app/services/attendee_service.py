from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.attendee import Attendee
from app.models.event import Event

async def register_attendee(db: AsyncSession, event_id, attendee_data):
    event = await db.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    attendee_count = await db.execute(select(func.count(Attendee.id)).where(Attendee.event_id == event_id))
    attendee_count = attendee_count.scalar()

    if attendee_count >= event.max_capacity:
        raise HTTPException(status_code=400, detail="Event is at full capacity")

    attendee = Attendee(**attendee_data.dict(), event_id=event_id)
    db.add(attendee)

    try:
        await db.commit()
        await db.refresh(attendee)
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Attendee already registered")

    return attendee

async def get_attendees(db: AsyncSession, event_id, skip=0, limit=10):
    result = await db.execute(select(Attendee).where(Attendee.event_id == event_id).offset(skip).limit(limit))
    return result.scalars().all()
