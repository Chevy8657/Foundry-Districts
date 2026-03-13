from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/shortest-word-length")
def shortest_word_length(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "shortest_length": 0
        }

    shortest = min(len(word) for word in words)

    return {
        "input_text": input_text,
        "shortest_length": shortest
    }
