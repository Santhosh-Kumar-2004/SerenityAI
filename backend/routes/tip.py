from fastapi import APIRouter, HTTPException
from model import get_wellness_tip

router = APIRouter()

@router.get("/tip")
async def get_tip():
    try:
        tip = get_wellness_tip()
        return {"tip": tip}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
