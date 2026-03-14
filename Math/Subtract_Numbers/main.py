from fastapi import APIRouter

router = APIRouter()

@router.get("/math/subtract-numbers")
def subtract_numbers(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "result": a - b
    }
