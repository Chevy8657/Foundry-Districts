from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/text-to-word-list")
def text_to_word_list(input_text: str):

    words = input_text.split()

    return {
        "input_text": input_text,
        "word_list": words,
        "count": len(words)
    }
