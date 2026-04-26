from fastapi import APIRouter
import re

# This router is the "Plug" that your Gateway's autoloader looks for
router = APIRouter()

# By using "/", the Gateway automatically maps this to /Logic/Extract_Numbers/
@router.get("/")
def extract_numbers(input_text: str):
    # The Regex engine: \d+ finds all sequences of digits
    numbers = re.findall(r"\d+", input_text)

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "numbers_found": numbers,
        "count": len(numbers)
    }
