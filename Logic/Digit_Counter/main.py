from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    processed_data = sum(1 for c in input_text if c.isdigit())

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
