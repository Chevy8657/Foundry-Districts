from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-path-type")
def directory_path_type(directory_path: str):
    path = Path(directory_path)

    if not path.exists():
        return {
            "directory_path": directory_path,
            "exists": False,
            "type": None
        }

    if path.is_dir():
        path_type = "directory"
    elif path.is_file():
        path_type = "file"
    elif path.is_symlink():
        path_type = "symlink"
    else:
        path_type = "unknown"

    return {
        "directory_path": directory_path,
        "exists": True,
        "type": path_type
    }
