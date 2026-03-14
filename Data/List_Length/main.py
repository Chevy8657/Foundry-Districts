from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/data/list-length")
def list_length(input_text: str):
    try:
        parsed = json.loads(input_text)

        if not isinstance(parsed, list):
            return {
                "input_text": input_text,
                "error": "input is not a JSON list"
            }

        return {
            "input_text": input_text,
            "list_length": len(parsed)
        }

    except Exception as e:
        return {
            "input_text": input_text,
            "error": str(e)
        }
