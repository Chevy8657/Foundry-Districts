from fastapi import APIRouter
import base64

router = APIRouter()

@router.get("/security/base64-decode")
def base64_decode(encoded_text: str):
    decoded = base64.b64decode(encoded_text).decode()

    return {
        "encoded_text": encoded_text,
        "decoded_text": decoded
    }
