from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/logic/word-frequency-list")
def word_frequency_list(input_text: str):

    words = input_text.split()
    frequency = dict(Counter(words))

    return {
        "input_text": input_text,
        "frequency": frequency
    }
