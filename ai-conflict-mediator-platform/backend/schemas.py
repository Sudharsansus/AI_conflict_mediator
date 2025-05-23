from pydantic import BaseModel
from datetime import datetime


class ConflictLogCreate(BaseModel):
    message: str
    conflict_score: float
    sentiment: str
    emotion: str
    language: str


class ConflictLogResponse(ConflictLogCreate):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True  # ✅ For Pydantic v2 (replaces orm_mode=True)
