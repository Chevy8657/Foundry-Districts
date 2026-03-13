from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/extract-numbers")
def extract_numbers(input_text: str):
    numbers = re.findall(r"\d+", input_text)

    return {
        "input_text": input_text,
        "numbers_found": numbers
    }
