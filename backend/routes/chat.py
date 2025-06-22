from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from model import get_ai_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_ai(data: ChatRequest):
    try:
        reply, mood = get_ai_response(data.message)
        return {
            "reply": reply,
            "mood": mood
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
