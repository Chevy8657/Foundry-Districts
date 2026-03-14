from fastapi import APIRouter

router = APIRouter()

@router.get("/math/round-number")
def round_number(number: float, decimals: int = 0):

    rounded = round(number, decimals)

    return {
        "number": number,
        "decimals": decimals,
        "rounded_value": rounded
    }
