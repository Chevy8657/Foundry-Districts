from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-modified-time")
def file_modified_time(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "modified_time": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "modified_time": path.stat().st_mtime
    }
