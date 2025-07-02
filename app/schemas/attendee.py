from pydantic import BaseModel, EmailStr

class AttendeeCreate(BaseModel):
    name: str
    email: EmailStr
