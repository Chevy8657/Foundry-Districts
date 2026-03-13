from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/logic/most-common-word")
def most_common_word(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "most_common_word": None,
            "count": 0
        }

    counter = Counter(words)
    word, count = counter.most_common(1)[0]

    return {
        "input_text": input_text,
        "most_common_word": word,
        "count": count
    }
