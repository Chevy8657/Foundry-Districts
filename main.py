from fastapi import FastAPI
import os

# Logic modules
from Logic.Word_Counter.main import router as word_counter_router
from Logic.Token_Counter.main import router as token_counter_router
from Logic.Character_Counter.main import router as character_counter_router

app = FastAPI()

DB_FILE = "vault.txt"

# Ensure vault exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")


# --------------------
# Gateway Status
# --------------------
@app.get("/")
def home():
    return {
        "status": "The Factory is Online",
        "storage": "Permanent Ledger Active"
    }


@app.get("/health")
def health():
    return {
        "status": "Factory Healthy",
        "gateway": "Foundry-Districts",
        "runtime": "FastAPI"
    }


# --------------------
# Ledger
# --------------------
@app.post("/store-data")
async def store(item: str):
    with open(DB_FILE, "a") as f:
        f.write(item + "\n")

    return {"message": f"'{item}' permanently inked to ledger."}


@app.get("/view-vault")
async def view():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            items = f.read().splitlines()
        return {"secured_items": items}

    return {"secured_items": []}


# --------------------
# Register Logic Tools
# --------------------
app.include_router(word_counter_router)
app.include_router(token_counter_router)
app.include_router(character_counter_router)


# --------------------
# API Registry
# --------------------
@app.get("/apis")
def list_apis():
    return {
        "available_apis": [
            {
                "name": "store-data",
                "method": "POST",
                "path": "/store-data"
            },
            {
                "name": "view-vault",
                "method": "GET",
                "path": "/view-vault"
            },
            {
                "name": "health",
                "method": "GET",
                "path": "/health"
            },
            {
                "name": "word-count",
                "method": "GET",
                "path": "/logic/word-count"
            },
            {
                "name": "token-count",
                "method": "GET",
                "path": "/logic/token-count"
            },
            {
                "name": "character-count",
                "method": "GET",
                "path": "/logic/character-count"
            }
        ]
    }
    
