from fastapi import APIRouter

router = APIRouter()

@router.get("/math/average-calculator")
def average_calculator(a: float, b: float):

    avg = (a + b) / 2

    return {
        "a": a,
        "b": b,
        "average": avg
    }
