from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/data/list-unique")
def list_unique(input_text: str):
    try:
        parsed = json.loads(input_text)

        if not isinstance(parsed, list):
            return {
                "input_text": input_text,
                "error": "input is not a JSON list"
            }

        unique_items = list(set(parsed))

        return {
            "input_text": input_text,
            "unique_items": unique_items,
            "unique_count": len(unique_items)
        }

    except Exception as e:
        return {
            "input_text": input_text,
            "error": str(e)
        }
