from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-path-depth")
def directory_path_depth(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "depth": len(path.parts)
    }
