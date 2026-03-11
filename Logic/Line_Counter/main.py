from fastapi import APIRouter

router = APIRouter()

@router.get("/logic/line-count")
def line_count(input_text: str):
    if input_text == "":
        count = 0
    else:
        count = len(input_text.splitlines())
        if count == 0:
            count = 1

    return {
        "input_text": input_text,
        "line_count": count
    }
