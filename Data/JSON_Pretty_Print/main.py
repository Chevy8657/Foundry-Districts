from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/data/json-pretty-print")
def json_pretty_print(input_text: str):
    try:
        parsed = json.loads(input_text)
        pretty = json.dumps(parsed, indent=4)
        return {
            "input_text": input_text,
            "pretty_json": pretty
        }
    except Exception as e:
        return {
            "input_text": input_text,
            "error": str(e)
        }
