from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-suffix-list")
def file_suffix_list(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "suffixes": list(path.suffixes)
    }
