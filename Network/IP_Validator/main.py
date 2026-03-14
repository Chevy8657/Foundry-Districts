from fastapi import APIRouter
import ipaddress

router = APIRouter()

@router.get("/network/ip-validator")
def ip_validator(ip: str):
    try:
        ipaddress.ip_address(ip)
        valid = True
    except ValueError:
        valid = False

    return {
        "ip": ip,
        "valid_ip": valid
    }
