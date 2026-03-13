from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/trim-text")
def trim_text(input_text: str):
    trimmed = input_text.strip()

    return {
        "input_text": input_text,
        "trimmed_text": trimmed
    }
