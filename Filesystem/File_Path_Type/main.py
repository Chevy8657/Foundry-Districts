from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-type")
def file_path_type(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "type": None
        }

    if path.is_file():
        path_type = "file"
    elif path.is_dir():
        path_type = "directory"
    elif path.is_symlink():
        path_type = "symlink"
    else:
        path_type = "unknown"

    return {
        "file_path": file_path,
        "exists": True,
        "type": path_type
    }
