from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    words = input_text.split()
    unique = list(set(words))

    processed_data = {
        "unique_words": unique,
        "unique_count": len(unique)
    }

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
