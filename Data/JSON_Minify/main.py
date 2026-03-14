from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/data/json-minify")
def json_minify(input_text: str):
    try:
        parsed = json.loads(input_text)
        minified = json.dumps(parsed, separators=(",", ":"))
        return {
            "input_text": input_text,
            "minified_json": minified
        }
    except Exception as e:
        return {
            "input_text": input_text,
            "error": str(e)
        }
