from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    if input_text == "":
        processed_data = 0
    else:
        count = len(input_text.splitlines())
        processed_data = count if count > 0 else 1

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
