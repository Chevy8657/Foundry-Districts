from fastapi import APIRouter
import secrets

router = APIRouter()

@router.get("/security/random-token")
def random_token(length: int = 32):
    token = secrets.token_hex(length)

    return {
        "token_length": length,
        "random_token": token
    }
