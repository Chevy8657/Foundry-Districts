from fastapi import APIRouter
from pathlib import Path
import os

router = APIRouter(prefix="/filesystem")

@router.get("/file-common-path")
def file_common_path(path_a: str, path_b: str):
    common = os.path.commonpath([path_a, path_b])

    return {
        "path_a": path_a,
        "path_b": path_b,
        "common_path": common
    }
