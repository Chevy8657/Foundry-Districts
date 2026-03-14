from fastapi import APIRouter
import re

router = APIRouter()

EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

@router.get("/network/email-validator")
def email_validator(email: str):

    valid = re.match(EMAIL_REGEX, email) is not None

    return {
        "email": email,
        "valid_email": valid
    }
