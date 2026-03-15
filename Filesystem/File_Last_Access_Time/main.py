from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-last-access-time")
def file_last_access_time(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "last_access_time": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "last_access_time": path.stat().st_atime
    }
