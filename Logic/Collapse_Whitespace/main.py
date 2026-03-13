from fastapi import APIRouter
import re

router = APIRouter()

@router.get("/logic/collapse-whitespace")
def collapse_whitespace(input_text: str):
    collapsed = re.sub(r"\s+", " ", input_text).strip()

    return {
        "input_text": input_text,
        "collapsed_text": collapsed
    }
