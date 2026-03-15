from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-resolver")
def file_path_resolver(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "resolved_path": str(path.resolve())
    }
