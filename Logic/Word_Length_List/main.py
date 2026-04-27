from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()

    result = [
        {"word": word, "length": len(word)}
        for word in words
    ]

    processed_data = result

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
