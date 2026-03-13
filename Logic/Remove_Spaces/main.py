from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/remove-spaces")
def remove_spaces(input_text: str):
    cleaned = input_text.replace(" ", "")

    return {
        "input_text": input_text,
        "cleaned_text": cleaned
    }
