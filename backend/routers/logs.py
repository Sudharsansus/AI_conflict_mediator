from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from backend.database import crud
from backend.database.db import get_db
from backend import schemas

router = APIRouter(prefix="/api/logs", tags=["Logs"])

@router.get("/", response_model=List[schemas.ConflictLog])
def read_logs(keyword: Optional[str] = "", log_date: Optional[date] = None, db: Session = Depends(get_db)):
    return crud.get_logs(db, keyword=keyword, log_date=log_date)

@router.get("/{log_id}", response_model=schemas.ConflictLog)
def read_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.get_log(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log

@router.delete("/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    if crud.delete_log(db, log_id):
        return {"detail": "Log deleted"}
    raise HTTPException(status_code=404, detail="Log not found")

@router.delete("/")
def delete_all_logs(db: Session = Depends(get_db)):
    crud.delete_all_logs(db)
    return {"detail": "All logs deleted"}
