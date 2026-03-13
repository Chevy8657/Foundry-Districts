from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/ends-with-check")
def ends_with_check(input_text: str, suffix: str):
    return {
        "input_text": input_text,
        "suffix": suffix,
        "ends_with": input_text.endswith(suffix)
    }
