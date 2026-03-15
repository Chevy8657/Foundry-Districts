from fastapi import APIRouter
import os

router = APIRouter(prefix="/filesystem")

@router.get("/directory-common-path")
def directory_common_path(path_a: str, path_b: str):
    common = os.path.commonpath([path_a, path_b])

    return {
        "path_a": path_a,
        "path_b": path_b,
        "common_path": common
    }
