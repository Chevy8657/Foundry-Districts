from fastapi import APIRouter
from pathlib import Path

router = APIRouter(prefix="/filesystem")

@router.get("/file-size-human-readable")
def file_size_human_readable(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return {
            "file_path": file_path,
            "exists": False,
            "size": None
        }

    size = path.stat().st_size

    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024 or unit == "TB":
            return {
                "file_path": file_path,
                "exists": True,
                "size": f"{round(size,2)} {unit}"
            }
        size /= 1024
