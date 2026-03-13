from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-count-above-length")
def word_count_above_length(input_text: str, min_length: int):

    words = input_text.split()

    filtered = [
        word for word in words
        if len(word) > min_length
    ]

    return {
        "input_text": input_text,
        "min_length": min_length,
        "matching_words": filtered,
        "count": len(filtered)
    }
