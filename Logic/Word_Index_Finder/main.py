from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/word-index-finder")
def word_index_finder(input_text: str, target_word: str):

    words = input_text.split()

    indexes = []

    for index, word in enumerate(words, start=1):
        if word == target_word:
            indexes.append(index)

    return {
        "input_text": input_text,
        "target_word": target_word,
        "positions": indexes
    }
