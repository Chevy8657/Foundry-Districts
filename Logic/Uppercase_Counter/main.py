from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/uppercase-count")
def uppercase_count(input_text: str):
    return {
        "input_text": input_text,
        "uppercase_count": sum(1 for c in input_text if c.isupper())
    }
