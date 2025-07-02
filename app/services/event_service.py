from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.event import Event
from datetime import datetime

async def create_event(db: AsyncSession, event_data):
    event = Event(**event_data.dict())
    db.add(event)
    await db.commit()
    await db.refresh(event)
    return event

async def list_upcoming_events(db: AsyncSession):
    result = await db.execute(select(Event).where(Event.end_time > datetime.now()))
    return result.scalars().all()
