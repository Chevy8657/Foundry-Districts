from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/data/json-validator")
def json_validator(input_text: str):
    try:
        parsed = json.loads(input_text)
        return {
            "input_text": input_text,
            "valid_json": True,
            "parsed_type": type(parsed).__name__
        }
    except Exception as e:
        return {
            "input_text": input_text,
            "valid_json": False,
            "error": str(e)
        }
