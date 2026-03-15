from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-is-relative")
def file_is_relative(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "is_relative": not path.is_absolute()
    }
