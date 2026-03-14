from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/time/add-minutes")
def add_minutes(iso_timestamp: str, minutes: int):
    dt = datetime.fromisoformat(iso_timestamp)
    new_time = dt + timedelta(minutes=minutes)

    return {
        "original_timestamp": iso_timestamp,
        "minutes_added": minutes,
        "new_timestamp": new_time.isoformat()
    }
