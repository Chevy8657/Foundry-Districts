from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/sentence-count")
def sentence_count(input_text: str):
    text = input_text.strip()

    if not text:
        count = 0
    else:
        sentence_endings = [".", "!", "?"]
        count = sum(text.count(mark) for mark in sentence_endings)

        if count == 0 and text:
            count = 1

    return {
        "input_text": input_text,
        "sentence_count": count
    }
