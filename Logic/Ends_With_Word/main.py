from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/ends-with-word")
def ends_with_word(input_text: str, target_word: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "target_word": target_word,
            "ends_with_word": False
        }

    return {
        "input_text": input_text,
        "target_word": target_word,
        "ends_with_word": words[-1] == target_word
    }
