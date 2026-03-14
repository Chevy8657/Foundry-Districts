from fastapi import APIRouter
from urllib.parse import urlparse

router = APIRouter()

@router.get("/network/url-validator")
def url_validator(url: str):
    parsed = urlparse(url)

    valid = all([parsed.scheme, parsed.netloc])

    return {
        "url": url,
        "valid_url": valid
    }
