from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()

    if not words:
        processed_data = {
            "least_common_word": None,
            "count": 0
        }
    else:
        counter = Counter(words)
        least_count = min(counter.values())
        least_words = [word for word, count in counter.items() if count == least_count]

        processed_data = {
            "least_common_word": least_words[0],
            "count": least_count
        }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
