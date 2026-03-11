from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/character-count")
def character_count(input_text: str):
    return {
        "input_text": input_text,
        "character_count": len(input_text)
    }
