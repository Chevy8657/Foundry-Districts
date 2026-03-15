from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-extension-extractor")
def file_extension_extractor(file_path: str):
    return {
        "file_path": file_path,
        "file_extension": Path(file_path).suffix
    }
