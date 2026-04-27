from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str, prefix: str):
    processed_data = input_text.startswith(prefix)

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
