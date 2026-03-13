from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/logic/least-common-word")
def least_common_word(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "least_common_word": None,
            "count": 0
        }

    counter = Counter(words)
    least_count = min(counter.values())
    least_words = [word for word, count in counter.items() if count == least_count]

    return {
        "input_text": input_text,
        "least_common_word": least_words[0],
        "count": least_count
    }
