from fastapi import APIRouter

router = APIRouter()

@router.get("/math/multiply-numbers")
def multiply_numbers(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "result": a * b
    }
