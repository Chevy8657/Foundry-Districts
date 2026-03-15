from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/directory-list-files")
def directory_list_files(directory_path: str):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        return {
            "directory_path": directory_path,
            "exists": False,
            "files": None
        }

    files = [p.name for p in path.iterdir() if p.is_file()]

    return {
        "directory_path": directory_path,
        "exists": True,
        "files": files
    }
