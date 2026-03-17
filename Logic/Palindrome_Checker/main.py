from fastapi import APIRouter

router = APIRouter(prefix="/logic")

@router.get("/is-palindrome")
def is_palindrome(text: str):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return {
        "input": text,
        "is_palindrome": cleaned == cleaned[::-1]
    }
