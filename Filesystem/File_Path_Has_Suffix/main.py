from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-has-suffix")
def file_path_has_suffix(file_path: str, suffix: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "suffix": suffix,
        "has_suffix": path.suffix == suffix
    }
