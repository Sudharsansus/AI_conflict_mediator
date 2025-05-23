from fastapi import APIRouter, Body, Depends
from backend.database import crud, db
from backend.models.conflict_log import ConflictLog
from backend.schemas import ConflictLogCreate, ConflictLogResponse
from backend.services.gpt_client import rewrite_message  # type: ignore
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/logs", response_model=ConflictLogResponse)
def create_conflict_log(
    log_data: ConflictLogCreate, db_session: Session = Depends(db.get_db)
):
    log = crud.create_conflict_log(db_session, log_data)
    return log


@router.get("/logs", response_model=list[ConflictLogResponse])
def get_conflict_logs(db_session: Session = Depends(db.get_db)):
    return crud.get_all_logs(db_session)


@router.post("/rewrite")
def rewrite_message_api(message: str = Body(..., embed=True)):
    rewritten = rewrite_message(message)
    return {
        "original": message,
        "rewritten": rewritten
    }
