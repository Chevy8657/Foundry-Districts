from fastapi import APIRouter

# Create router object that the gateway imports
router = APIRouter()


@router.get("/logic/word-count")
async def word_count(text: str):
    """
    Counts the number of words in a string.
    Example:
    /logic/word-count?text=The%20factory%20is%20online
    """

    words = text.split()
    count = len(words)

    return {
        "input_text": text,
        "word_count": count
    }
