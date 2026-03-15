from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-is-absolute")
def directory_is_absolute(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "is_absolute": path.is_absolute()
    }
