from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/last-word")
def last_word(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "last_word": ""
        }

    return {
        "input_text": input_text,
        "last_word": words[-1]
    }
