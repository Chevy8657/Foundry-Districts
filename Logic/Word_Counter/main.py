from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def execute_tool(text: str):
    words = text.split()
    processed_data = len(words)

    return {
        "status": "SUCCESS",
        "input_text": text,
        "result": processed_data
    }
