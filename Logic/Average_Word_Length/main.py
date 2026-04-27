from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()

    if not words:
        processed_data = 0
    else:
        total_length = sum(len(word) for word in words)
        processed_data = round(total_length / len(words), 2)

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
