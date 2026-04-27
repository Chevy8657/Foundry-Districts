from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(text: str):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    processed_data = (cleaned == cleaned[::-1])

    return {
        "status": "SUCCESS",
        "input_text": text,
        "result": processed_data
    }
