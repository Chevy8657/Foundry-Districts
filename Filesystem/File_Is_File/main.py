from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-is-file")
def file_is_file(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_file": path.is_file()
    }
