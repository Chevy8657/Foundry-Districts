from fastapi import APIRouter
import uuid

router = APIRouter()

@router.get("/utility/uuid")
async def generate_uuid():
    new_uuid = str(uuid.uuid4())

    return {
        "generated_uuid": new_uuid
    }
