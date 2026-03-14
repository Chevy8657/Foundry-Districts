from fastapi import APIRouter
from urllib.parse import urlparse

router = APIRouter()

@router.get("/network/protocol-extractor")
def protocol_extractor(url: str):
    parsed = urlparse(url)

    return {
        "url": url,
        "protocol": parsed.scheme
    }
