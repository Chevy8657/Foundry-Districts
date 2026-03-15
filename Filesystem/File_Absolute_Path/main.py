from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-absolute-path")
def file_absolute_path(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "absolute_path": str(path.resolve())
    }
