from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-relative-to-base")
def file_relative_to_base(file_path: str, base_path: str):
    path = Path(file_path)
    base = Path(base_path)

    try:
        relative_path = path.relative_to(base)
        return {
            "file_path": file_path,
            "base_path": base_path,
            "relative_path": str(relative_path)
        }
    except ValueError:
        return {
            "file_path": file_path,
            "base_path": base_path,
            "relative_path": None,
            "error": "file_path is not under base_path"
        }
