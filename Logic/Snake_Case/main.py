from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    text = re.sub(r"[^\w\s]", "", input_text)
    processed_data = re.sub(r"\s+", "_", text.strip()).lower()

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
