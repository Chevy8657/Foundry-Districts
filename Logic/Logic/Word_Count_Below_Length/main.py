from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-count-below-length")
def word_count_below_length(input_text: str, max_length: int):

    words = input_text.split()

    filtered = [
        word for word in words
        if len(word) < max_length
    ]

    return {
        "input_text": input_text,
        "max_length": max_length,
        "matching_words": filtered,
        "count": len(filtered)
    }
