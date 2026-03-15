from fastapi import APIRouter
import base64

router = APIRouter()

@router.get("/security/base64-encode")
def base64_encode(input_text: str):
    encoded = base64.b64encode(input_text.encode()).decode()

    return {
        "input_text": input_text,
        "base64_encoded": encoded
    }
