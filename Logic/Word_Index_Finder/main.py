from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str, target_word: str):
    words = input_text.split()

    positions = [
        index for index, word in enumerate(words, start=1)
        if word == target_word
    ]

    processed_data = {
        "positions": positions
    }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
