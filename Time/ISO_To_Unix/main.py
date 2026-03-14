from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/time/iso-to-unix")
def iso_to_unix(iso_timestamp: str):
    dt = datetime.fromisoformat(iso_timestamp)

    return {
        "iso_timestamp": iso_timestamp,
        "unix_timestamp": int(dt.timestamp())
    }
