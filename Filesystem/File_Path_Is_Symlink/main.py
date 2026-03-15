from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-is-symlink")
def file_path_is_symlink(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_symlink": path.is_symlink()
    }
