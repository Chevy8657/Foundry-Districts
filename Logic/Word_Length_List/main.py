from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-length-list")
def word_length_list(input_text: str):

    words = input_text.split()

    result = []

    for word in words:
        result.append({
            "word": word,
            "length": len(word)
        })

    return {
        "input_text": input_text,
        "word_lengths": result
    }
