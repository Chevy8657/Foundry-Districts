from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get("/time/unix-to-iso")
def unix_to_iso(timestamp: int):
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)

    return {
        "unix_timestamp": timestamp,
        "iso_timestamp": dt.isoformat()
    }
