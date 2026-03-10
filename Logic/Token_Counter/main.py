from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-count")
async def word_count(text: str):
    count = len(text.split())
    return {
        "input_text": text,
        "word_count": count
    }
