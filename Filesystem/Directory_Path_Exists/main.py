from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-path-exists")
def directory_path_exists(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "exists": path.exists(),
        "is_directory": path.is_dir()
    }
