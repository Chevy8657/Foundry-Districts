from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-parent-directory")
def file_parent_directory(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "parent_directory": str(path.parent)
    }
