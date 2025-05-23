from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.ai_service import analyze_conflict_message

router = APIRouter()

class MessageRequest(BaseModel):
    message: str

@router.post("/analyze_message/")
def analyze_message(request: MessageRequest):
    return analyze_conflict_message(request.message)