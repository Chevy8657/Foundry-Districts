from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    processed_data = re.sub(r"\s+", " ", input_text).strip()

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
