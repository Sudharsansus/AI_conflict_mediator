from pydantic import BaseModel
from datetime import datetime

class ConflictLog(BaseModel):
    id: int
    message: str
    conflict_score: float
    sentiment: str
    emotion: str
    language: str
    timestamp: datetime

    class Config:
        orm_mode = True  # Pydantic v1
