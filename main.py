from fastapi import FastAPI
import os

from Logic.Word_Counter.main import router as word_counter_router
from Logic.Token_Counter.main import router as token_counter_router
from Utility.UUID_Generator.main import router as uuid_generator_router

app = FastAPI()

DB_FILE = "vault.txt"

# Ensure the vault file exists so the app does not crash
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")


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
                "purpose": "Count the number of words in submitted text"
            },
            {
                "name": "token-count",
                "method": "GET",
                "path": "/logic/token-count",
                "purpose": "Count the number of tokens in submitted text"
            },
            {
                "name": "uuid",
                "method": "GET",
                "path": "/utility/uuid",
                "purpose": "Generate a new UUID"
            }
        ]
    }


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
        return {
            "secured_items": items
        }
    return {
        "secured_items": []
    }


app.include_router(word_counter_router)
app.include_router(token_counter_router)
app.include_router(uuid_generator_router)
