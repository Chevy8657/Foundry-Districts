from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-list-directories")
def directory_list_directories(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "directories": None
        }

    directories = [p.name for p in path.iterdir() if p.is_dir()]

    return {
        "directory_path": directory_path,
        "exists": True,
        "directories": directories
    }
