from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-is-root")
def file_path_is_root(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_root": path == path.anchor
    }
