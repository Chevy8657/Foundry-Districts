from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def execute_tool(input_text: str):
    compact = input_text.replace(" ", "")
    processed_data = len(compact)

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": processed_data
    }
