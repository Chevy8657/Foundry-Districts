from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/count-words-list")
def count_words_list(input_text: str):
    words = input_text.split()

    return {
        "input_text": input_text,
        "word_list": words,
        "word_count": len(words)
    }
