from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/letter-count")
def letter_count(input_text: str):
    return {
        "input_text": input_text,
        "letter_count": sum(1 for c in input_text if c.isalpha())
    }
