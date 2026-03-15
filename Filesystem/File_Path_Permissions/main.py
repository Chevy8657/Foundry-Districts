from fastapi import APIRouter
from pathlib import Path
import os

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-permissions")
def file_path_permissions(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "readable": None,
            "writable": None,
            "executable": None
        }

    return {
        "file_path": file_path,
        "exists": True,
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
