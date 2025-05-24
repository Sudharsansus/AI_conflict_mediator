# backend/api/conflict.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.routers.ai_analyzer import analyze_text

router = APIRouter()

class AnalyzeRequest(BaseModel):
    message: str

@router.post("/analyze")
async def analyze(request: AnalyzeRequest):
    try:
        result = analyze_text(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
