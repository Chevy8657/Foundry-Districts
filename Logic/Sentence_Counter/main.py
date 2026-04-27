from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    text = input_text.strip()

    if not text:
        processed_data = 0
    else:
        sentence_endings = [".", "!", "?"]
        count = sum(text.count(mark) for mark in sentence_endings)
        processed_data = count if count > 0 else 1

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
