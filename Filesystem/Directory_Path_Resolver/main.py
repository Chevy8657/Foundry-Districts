from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-path-resolver")
def directory_path_resolver(directory_path: str):
    path = Path(directory_path)

    return {
        "directory_path": directory_path,
        "resolved_path": str(path.resolve())
    }
