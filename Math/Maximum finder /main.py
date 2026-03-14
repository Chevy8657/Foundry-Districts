from fastapi import APIRouter

router = APIRouter()

@router.get("/math/minimum-finder")
def minimum_finder(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "minimum": min(a, b)
    }
