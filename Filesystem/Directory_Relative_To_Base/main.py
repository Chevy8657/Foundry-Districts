from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-relative-to-base")
def directory_relative_to_base(directory_path: str, base_path: str):
    path = Path(directory_path)
    base = Path(base_path)

    try:
        relative = path.relative_to(base)
        return {
            "directory_path": directory_path,
            "base_path": base_path,
            "relative_path": str(relative)
        }
    except ValueError:
        return {
            "directory_path": directory_path,
            "base_path": base_path,
            "relative_path": None,
            "error": "directory_path is not under base_path"
        }
