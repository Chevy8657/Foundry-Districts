from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/kebab-case")
def kebab_case(input_text: str):
    text = re.sub(r"[^\w\s]", "", input_text)
    text = re.sub(r"\s+", "-", text.strip()).lower()

    return {
        "input_text": input_text,
        "kebab_case": text
    }
