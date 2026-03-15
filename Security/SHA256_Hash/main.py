from fastapi import APIRouter
import hashlib

router = APIRouter()

@router.get("/security/sha256-hash")
def sha256_hash(input_text: str):
    hashed = hashlib.sha256(input_text.encode()).hexdigest()

    return {
        "input_text": input_text,
        "sha256_hash": hashed
    }
