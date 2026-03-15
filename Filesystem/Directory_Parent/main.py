from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-parent")
def directory_parent(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "parent_directory": str(path.parent)
    }
