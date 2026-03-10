from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/token-count")
async def token_count(text: str):
    count = len(text.split())
    return {
        "input_text": text,
        "token_count": count
    }
