from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-contains-directory")
def directory_contains_directory(directory_path: str, directory_name: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "contains_directory": None
        }

    target = path / directory_name

    return {
        "directory_path": directory_path,
        "directory_name": directory_name,
        "contains_directory": target.exists() and target.is_dir()
    }
