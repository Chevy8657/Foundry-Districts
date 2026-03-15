from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-is-absolute")
def file_is_absolute(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_absolute": path.is_absolute()
    }
