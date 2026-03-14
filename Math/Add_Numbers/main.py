from fastapi import APIRouter

router = APIRouter()

@router.get("/math/add-numbers")
def add_numbers(a: float, b: float):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }
