from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-creation-time")
def file_creation_time(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "creation_time": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "creation_time": path.stat().st_ctime
    }
