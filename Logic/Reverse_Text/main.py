from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/reverse-text")
def reverse_text(input_text: str):
    reversed_text = input_text[::-1]

    return {
        "input_text": input_text,
        "reversed_text": reversed_text
    }
