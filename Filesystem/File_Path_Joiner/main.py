from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-joiner")
def file_path_joiner(base_path: str, name: str):
    path = Path(base_path) / name

    return {
        "base_path": base_path,
        "name": name,
        "joined_path": str(path)
    }
