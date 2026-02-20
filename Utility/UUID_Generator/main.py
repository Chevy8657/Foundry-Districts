from fastapi import FastAPI
import os

app = FastAPI()
DB_FILE = "vault.txt"

# Ensure the file exists so the machine doesn't crash
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")

@app.get("/")
def home():
    return {"status": "The Factory is Online", "storage": "Permanent Ledger Active"}

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
