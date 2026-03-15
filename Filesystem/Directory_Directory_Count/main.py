from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-directory-count")
def directory_directory_count(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "directory_count": None
        }

    count = sum(1 for p in path.iterdir() if p.is_dir())

    return {
        "directory_path": directory_path,
        "exists": True,
        "directory_count": count
    }
