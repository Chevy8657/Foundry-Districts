from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()
    frequency = dict(Counter(words))

    processed_data = frequency

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
