from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()
    processed_data = {
        "word_list": words,
        "count": len(words)
    }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
