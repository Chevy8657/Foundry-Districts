from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/remove-punctuation")
def remove_punctuation(input_text: str):
    cleaned = re.sub(r"[^\w\s]", "", input_text)

    return {
        "input_text": input_text,
        "cleaned_text": cleaned
    }
