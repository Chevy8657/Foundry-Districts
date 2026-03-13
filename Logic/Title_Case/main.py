from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/title-case")
def title_case(input_text: str):
    return {
        "input_text": input_text,
        "title_case": input_text.title()
    }
