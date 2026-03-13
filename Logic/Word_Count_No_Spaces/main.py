from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-count-no-spaces")
def word_count_no_spaces(input_text: str):
    compact = input_text.replace(" ", "")
    return {
        "input_text": input_text,
        "character_count_no_spaces": len(compact)
    }
