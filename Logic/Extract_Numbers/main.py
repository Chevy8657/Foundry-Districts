from fastapi import APIRouter

router = APIRouter()

@router.post("/extract")
async def extract(text: str):
    # Logic to find numbers...
    return {"numbers": results}
