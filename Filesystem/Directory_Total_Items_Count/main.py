from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-total-items-count")
def directory_total_items_count(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "total_items": None
        }

    count = sum(1 for _ in path.iterdir())

    return {
        "directory_path": directory_path,
        "exists": True,
        "total_items": count
    }
