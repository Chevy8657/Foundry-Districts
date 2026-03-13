from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-length-average")
def word_length_average(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "average_length": 0
        }

    total_length = sum(len(word) for word in words)
    avg = total_length / len(words)

    return {
        "input_text": input_text,
        "average_length": avg
    }
