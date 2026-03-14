from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/time/date-difference-days")
def date_difference_days(start_iso: str, end_iso: str):
    start = datetime.fromisoformat(start_iso)
    end = datetime.fromisoformat(end_iso)

    difference = (end - start).days

    return {
        "start_date": start_iso,
        "end_date": end_iso,
        "difference_days": difference
    }
