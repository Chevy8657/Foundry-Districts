from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    cleaned = re.sub(r"\d+", "", input_text)
    processed_data = cleaned

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
