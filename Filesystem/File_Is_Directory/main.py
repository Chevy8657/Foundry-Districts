from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-is-directory")
def file_is_directory(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_directory": path.is_dir()
    }
