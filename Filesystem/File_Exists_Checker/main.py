from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-exists-checker")
def file_exists_checker(file_path: str):
    path = Path(file_path)

    return {
        "file_path": file_path,
        "exists": path.exists()
    }
