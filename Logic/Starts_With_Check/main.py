from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/starts-with-check")
def starts_with_check(input_text: str, prefix: str):
    return {
        "input_text": input_text,
        "prefix": prefix,
        "starts_with": input_text.startswith(prefix)
    }
