from fastapi import APIRouter
from urllib.parse import urlparse

router = APIRouter()

@router.get("/network/domain-extractor")
def domain_extractor(url: str):
    parsed = urlparse(url)

    return {
        "url": url,
        "domain": parsed.netloc
    }
