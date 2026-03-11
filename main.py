from fastapi import FastAPI
import os

# Import Logic Modules
from Logic.Word_Counter.main import router as word_counter_router
from Logic.Token_Counter.main import router as token_counter_router
from Logic.Character_Counter.main import router as character_counter_router

# Import Utility Modules
from Utility.UUID_Generator.main import router as uuid_router


app = FastAPI()

DB_FILE = "vault.txt"

# Ensure vault exists so the machine never crashes
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")


# -----------------------------
# Gateway Health
# -----------------------------
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


# -----------------------------
# Ledger Storage
# -----------------------------
@app.post("/store-data")
async def store(item: str):
    with open(DB_FILE, "a") as f:
        f.write(item + "\n")

    return {
        "message": f"'{item}' permanently inked to ledger."
    }


@app.get("/view-vault")
async def view():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            items = f.read().splitlines()

        return {"secured_items": items}

    return {"secured_items": []}


# -----------------------------
# Register Logic Routers
# -----------------------------
app.include_router(word_counter_router)
app.include_router(token_counter_router)
app.include_router(character_counter_router)

# -----------------------------
# Register Utility Routers
# -----------------------------
app.include_router(uuid_router)


# -----------------------------
# API Registry
# -----------------------------
@app.get("/apis")
def list_apis():
    return {
        "available_apis": [
            {
                "name": "store-data",
                "method": "POST",
                "path": "/store-data",
                "purpose": "Store an item in the permanent ledger"
            },
            {
                "name": "view-vault",
                "method": "GET",
                "path": "/view-vault",
                "purpose": "View all secured ledger items"
            },
            {
                "name": "health",
                "method": "GET",
                "path": "/health",
                "purpose": "Check gateway health status"
            },
            {
                "name": "apis",
                "method": "GET",
                "path": "/apis",
                "purpose": "List available APIs in the district"
            },
            {
                "name": "word-count",
                "method": "GET",
                "path": "/logic/word-count",
                "purpose": "Count number of words in submitted text"
            },
            {
                "name": "token-count",
                "method": "GET",
                "path": "/logic/token-count",
                "purpose": "Count number of tokens in submitted text"
            },
            {
                "name": "character-count",
                "method": "GET",
                "path": "/logic/character-count",
                "purpose": "Count number of characters in submitted text"
            },
            {
                "name": "uuid",
                "method": "GET",
                "path": "/utility/uuid",
                "purpose": "Generate a unique UUID identifier"
            }
        ]
    }
