from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def execute_tool(text: str):
    processed_data = len(text.split())

    return {
        "status": "SUCCESS",
        "input_text": text,
        "result": processed_data
    }
