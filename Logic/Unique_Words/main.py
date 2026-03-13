from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/unique-words")
def unique_words(input_text: str):
    words = input_text.split()
    unique = list(set(words))

    return {
        "input_text": input_text,
        "unique_words": unique,
        "unique_count": len(unique)
    }
