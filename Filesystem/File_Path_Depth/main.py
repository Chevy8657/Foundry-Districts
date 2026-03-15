from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-depth")
def file_path_depth(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "depth": len(path.parts)
    }
