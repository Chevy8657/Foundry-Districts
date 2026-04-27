from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()

    processed_data = [
        {
            "position": index,
            "word": word
        }
        for index, word in enumerate(words, start=1)
    ]

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
