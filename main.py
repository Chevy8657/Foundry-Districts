from fastapi import FastAPI
import os

app = FastAPI()

DB_FILE = "vault.txt"

# Ensure the vault file exists so the app does not crash
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")

# Root / heartbeat
@app.get("/")
def home():
    return {
        "status": "The Factory is Online",
        "storage": "Permanent Ledger Active"
    }

# Health check
@app.get("/health")
def health():
    return {
        "status": "Factory Healthy",
        "gateway": "Foundry-Districts",
        "runtime": "FastAPI"
    }

# API catalog
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
            }
        ]
    }

# Store data in vault
@app.post("/store-data")
async def store(item: str):
    with open(DB_FILE, "a") as f:
        f.write(item + "\n")
    return {
        "message": f"'{item}' permanently inked to ledger."
    }

# View vault contents
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
