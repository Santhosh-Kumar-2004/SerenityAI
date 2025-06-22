from fastapi import APIRouter, HTTPException
from model import get_affirmation_response

router = APIRouter()

@router.get("/affirmation")
async def get_affirmation():
    try:
        reply = get_affirmation_response()
        return {"affirmation": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
