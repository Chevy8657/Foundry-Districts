from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    processed_data = input_text.replace(" ", "")

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
