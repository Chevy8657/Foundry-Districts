from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/lowercase-count")
def lowercase_count(input_text: str):
    return {
        "input_text": input_text,
        "lowercase_count": sum(1 for c in input_text if c.islower())
    }
