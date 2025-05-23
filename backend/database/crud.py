from sqlalchemy.orm import Session
from backend.models.conflict_log import ConflictLog
from backend import schemas
from datetime import date

def get_logs(db: Session, keyword: str = "", log_date: date = None):
    query = db.query(ConflictLog)
    if keyword:
        query = query.filter(ConflictLog.message.ilike(f"%{keyword}%"))
    if log_date:
        query = query.filter(ConflictLog.timestamp.cast(date) == log_date)
    return query.order_by(ConflictLog.timestamp.desc()).all()

def get_log(db: Session, log_id: int):
    return db.query(ConflictLog).filter(ConflictLog.id == log_id).first()

def delete_log(db: Session, log_id: int):
    log = get_log(db, log_id)
    if log:
        db.delete(log)
        db.commit()
        return True
    return False

def delete_all_logs(db: Session):
    db.query(ConflictLog).delete()
    db.commit()
