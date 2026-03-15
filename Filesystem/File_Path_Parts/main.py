from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-parts")
def file_path_parts(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "parts": list(path.parts)
    }
