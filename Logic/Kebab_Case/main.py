from fastapi import APIRouter
import re

router = APIRouter()

# Set path to "/" so the Gateway maps it to /Logic/Kebab_Case/ automatically
@router.get("/")
def kebab_case(input_text: str):
    # 1. Replace underscores with spaces (to handle Snake_Case inputs)
    text = input_text.replace("_", " ")
    
    # 2. Remove all non-word characters (keep only letters, numbers, spaces)
    text = re.sub(r"[^\w\s]", "", text)
    
    # 3. Strip whitespace, replace spaces with hyphens, and lowercase
    kebab = re.sub(r"\s+", "-", text.strip()).lower()

    return {
        "status": "SUCCESS",
        "input_text": input_text,
        "result": kebab
    }
