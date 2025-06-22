from fastapi import APIRouter, HTTPException
from model import get_motivation_response

router = APIRouter()

@router.get("/motivate")
async def get_motivation():
    try:
        reply = get_motivation_response()
        return {"motivation": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
