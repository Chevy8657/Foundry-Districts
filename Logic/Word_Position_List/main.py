from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-position-list")
def word_position_list(input_text: str):

    words = input_text.split()

    result = []

    for index, word in enumerate(words, start=1):
        result.append({
            "position": index,
            "word": word
        })

    return {
        "input_text": input_text,
        "words": result
    }
