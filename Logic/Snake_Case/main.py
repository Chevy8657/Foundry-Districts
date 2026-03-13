from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/snake-case")
def snake_case(input_text: str):
    text = re.sub(r"[^\w\s]", "", input_text)
    text = re.sub(r"\s+", "_", text.strip()).lower()

    return {
        "input_text": input_text,
        "snake_case": text
    }
