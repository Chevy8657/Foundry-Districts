from fastapi import APIRouter

router = APIRouter()

@router.get("/math/absolute-value")
def absolute_value(number: float):
    return {
        "number": number,
        "absolute_value": abs(number)
    }
