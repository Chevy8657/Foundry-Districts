from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-is-empty")
def directory_is_empty(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "is_empty": None
        }

    is_empty = not any(path.iterdir())

    return {
        "directory_path": directory_path,
        "exists": True,
        "is_empty": is_empty
    }
