from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()

    if not words:
        processed_data = {
            "most_common_word": None,
            "count": 0
        }
    else:
        counter = Counter(words)
        word, count = counter.most_common(1)[0]
        processed_data = {
            "most_common_word": word,
            "count": count
        }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
