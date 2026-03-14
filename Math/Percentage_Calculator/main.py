from fastapi import APIRouter

router = APIRouter()

@router.get("/math/percentage-calculator")
def percentage_calculator(part: float, whole: float):

    if whole == 0:
        return {
            "part": part,
            "whole": whole,
            "error": "division by zero"
        }

    percentage = (part / whole) * 100

    return {
        "part": part,
        "whole": whole,
        "percentage": percentage
    }
