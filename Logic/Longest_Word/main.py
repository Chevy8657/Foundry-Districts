from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/longest-word")
def longest_word(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "longest_word": ""
        }

    longest = max(words, key=len)

    return {
        "input_text": input_text,
        "longest_word": longest
    }
