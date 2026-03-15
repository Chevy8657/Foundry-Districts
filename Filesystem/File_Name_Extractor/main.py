from fastapi import APIRouter
from pathlib import Path

router = APIRouter()

@router.get("/filesystem/file-name-extractor")
def file_name_extractor(file_path: str):
    return {
        "file_path": file_path,
        "file_name": Path(file_path).name
    }
