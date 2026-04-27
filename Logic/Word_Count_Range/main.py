from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str, min_length: int, max_length: int):
    words = input_text.split()

    filtered = [
        word for word in words
        if min_length <= len(word) <= max_length
    ]

    processed_data = {
        "matching_words": filtered,
        "count": len(filtered)
    }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
