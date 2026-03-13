from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/shortest-word")
def shortest_word(input_text: str):

    words = input_text.split()

    if not words:
        return {
            "input_text": input_text,
            "shortest_word": ""
        }

    shortest = min(words, key=len)

    return {
        "input_text": input_text,
        "shortest_word": shortest
    }
