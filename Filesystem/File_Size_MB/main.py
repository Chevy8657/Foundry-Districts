from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-size-mb")
def file_size_mb(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "size_mb": None
        }

    size_bytes = path.stat().st_size
    size_mb = size_bytes / (1024 * 1024)

    return {
        "file_path": file_path,
        "exists": True,
        "size_mb": size_mb
    }
