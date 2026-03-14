from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()

@router.get("/time/current-timestamp")
def current_timestamp():
    now = datetime.now(timezone.utc)

    return {
        "unix_timestamp": int(now.timestamp()),
        "iso_timestamp": now.isoformat()
    }
