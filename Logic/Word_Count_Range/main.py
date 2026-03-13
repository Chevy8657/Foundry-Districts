from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-count-range")
def word_count_range(input_text: str, min_length: int, max_length: int):

    words = input_text.split()

    filtered = [
        word for word in words
        if min_length <= len(word) <= max_length
    ]

    return {
        "input_text": input_text,
        "min_length": min_length,
        "max_length": max_length,
        "matching_words": filtered,
        "count": len(filtered)
    }
