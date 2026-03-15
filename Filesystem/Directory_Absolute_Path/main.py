from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-absolute-path")
def directory_absolute_path(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "absolute_path": str(path.resolve())
    }
