from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-exists")
def file_path_exists(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "exists": path.exists(),
        "is_file": path.is_file()
    }
