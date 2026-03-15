from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-is-relative")
def directory_is_relative(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "is_relative": not path.is_absolute()
    }
