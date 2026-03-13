from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/text-length")
def text_length(input_text: str):
    return {
        "input_text": input_text,
        "length": len(input_text)
    }
