from fastapi import APIRouter

router = APIRouter()

@router.get("/math/maximum-finder")
def maximum_finder(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "maximum": max(a, b)
    }
