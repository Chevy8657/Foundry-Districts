from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-list-all")
def directory_list_all(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "items": None
        }

    items = [p.name for p in path.iterdir()]

    return {
        "directory_path": directory_path,
        "exists": True,
        "items": items
    }
