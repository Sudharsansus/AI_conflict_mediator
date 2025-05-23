from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..ai.model import analyze_conflict_text

router = APIRouter()

class ConflictInput(BaseModel):
    conversation_text: str

@router.post("/analyze")
async def analyze_conflict(input_data: ConflictInput):
    try:
        result = analyze_conflict_text(input_data.conversation_text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
