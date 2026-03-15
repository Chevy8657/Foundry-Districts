from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-path-normalizer")
def file_path_normalizer(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "normalized_path": str(path.resolve().as_posix())
    }
