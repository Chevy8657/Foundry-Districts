from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str, target_word: str):
    words = input_text.split()

    if not words:
        processed_data = False
    else:
        processed_data = (words[0] == target_word)

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
