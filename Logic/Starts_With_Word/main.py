from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/starts-with-word")
def starts_with_word(input_text: str, target_word: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "target_word": target_word,
            "starts_with_word": False
        }

    return {
        "input_text": input_text,
        "target_word": target_word,
        "starts_with_word": words[0] == target_word
    }
