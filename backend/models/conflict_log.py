from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.database.db import Base  # ✅ this is safe ONLY if Base exists in db.py

class ConflictLog(Base):
    __tablename__ = 'conflict_logs'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    conflict_score = Column(Float)
    sentiment = Column(String)
    emotion = Column(String)
    language = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
