from fastapi import APIRouter
import uuid

router = APIRouter()

@router.get("/utility/uuid")
def generate_uuid():
    return {
        "generated_uuid": str(uuid.uuid4())
    }
