from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-contains-file")
def directory_contains_file(directory_path: str, file_name: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "contains_file": None
        }

    target = path / file_name

    return {
        "directory_path": directory_path,
        "file_name": file_name,
        "contains_file": target.exists()
    }
