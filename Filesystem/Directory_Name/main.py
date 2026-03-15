from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-name")
def directory_name(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "directory_name": path.name
    }
