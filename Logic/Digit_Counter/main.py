from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/digit-count")
def digit_count(input_text: str):
    return {
        "input_text": input_text,
        "digit_count": sum(1 for c in input_text if c.isdigit())
    }
