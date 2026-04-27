from fastapi import APIRouter
from collections import Counter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()
    lengths = [len(word) for word in words]
    distribution = dict(Counter(lengths))

    processed_data = distribution

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
