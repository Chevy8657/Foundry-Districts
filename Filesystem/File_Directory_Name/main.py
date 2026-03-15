from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-directory-name")
def file_directory_name(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "directory_name": path.parent.name
    }
