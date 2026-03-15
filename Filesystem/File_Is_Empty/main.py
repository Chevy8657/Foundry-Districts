from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-is-empty")
def file_is_empty(file_path: str):
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return {
            "file_path": file_path,
            "exists": False,
            "is_empty": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "is_empty": path.stat().st_size == 0
    }
