from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-name-with-extension")
def file_name_with_extension(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "file_name": path.name
    }
