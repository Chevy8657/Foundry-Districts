from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/remove-numbers")
def remove_numbers(input_text: str):
    cleaned = re.sub(r"\d+", "", input_text)

    return {
        "input_text": input_text,
        "cleaned_text": cleaned
    }
