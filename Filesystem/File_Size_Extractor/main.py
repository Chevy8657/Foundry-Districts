from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-size-extractor")
def file_size_extractor(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "file_size_bytes": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "file_size_bytes": path.stat().st_size
    }
