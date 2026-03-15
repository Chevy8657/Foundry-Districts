from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-stem-extractor")
def file_stem_extractor(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "file_stem": path.stem
    }
