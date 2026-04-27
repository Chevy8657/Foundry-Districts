from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str, target_word: str):
    words = input_text.split()
    processed_data = target_word in words

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
