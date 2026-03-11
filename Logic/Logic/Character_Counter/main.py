from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/character-count")
async def character_count(text: str):
    count = len(text)

    return {
        "input_text": text,
        "character_count": count
    }
