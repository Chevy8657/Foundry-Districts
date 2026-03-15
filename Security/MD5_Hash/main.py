from fastapi import APIRouter
import hashlib

router = APIRouter()

@router.get("/security/md5-hash")
def md5_hash(input_text: str):
    hashed = hashlib.md5(input_text.encode()).hexdigest()

    return {
        "input_text": input_text,
        "md5_hash": hashed
    }
