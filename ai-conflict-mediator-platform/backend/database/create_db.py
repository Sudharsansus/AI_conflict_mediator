from backend.models.conflict_log import ConflictLog
from backend.database.db import engine
from sqlalchemy.orm import declarative_base

Base = ConflictLog.__bases__[0]

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")
