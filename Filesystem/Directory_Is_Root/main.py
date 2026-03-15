from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-is-root")
def directory_is_root(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "is_root": str(path.resolve()) == path.anchor
    }
