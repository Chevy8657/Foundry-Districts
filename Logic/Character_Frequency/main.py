from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/logic/character-frequency")
def character_frequency(input_text: str):
    frequency = dict(Counter(input_text))

    return {
        "input_text": input_text,
        "frequency": frequency
    }
