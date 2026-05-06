from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# 🧍 User-related Schemas
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    created_at: Optional[datetime]

    class Config:
        orm_mode = True  # ✅ small fix — you had `Trueschemas.py` typo


# 🔐 Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# 📸 Face Attendance Input Schema
class AttendanceIn(BaseModel):
    image_b64: str
    threshold: Optional[float] = None


# 📋 Attendance Output Schema
class AttendanceOut(BaseModel):
    id: int
    user_id: Optional[int]
    status: str
    confidence: float
    timestamp: datetime

    class Config:
        orm_mode = True

class LivenessAttendanceIn(BaseModel):
    image_b64_1: str
    image_b64_2: str
    threshold: Optional[float] = 0.5
