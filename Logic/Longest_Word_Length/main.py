from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/longest-word-length")
def longest_word_length(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "longest_length": 0
        }

    longest = max(len(word) for word in words)

    return {
        "input_text": input_text,
        "longest_length": longest
    }
