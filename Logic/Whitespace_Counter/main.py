from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/whitespace-count")
def whitespace_count(input_text: str):
    return {
        "input_text": input_text,
        "whitespace_count": sum(1 for c in input_text if c.isspace())
    }
