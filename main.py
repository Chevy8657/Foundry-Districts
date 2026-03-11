from fastapi import FastAPI
import os
import importlib.util
from pathlib import Path

app = FastAPI()

DB_FILE = "vault.txt"


# ---------------------------------
# Ensure vault exists
# ---------------------------------
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        f.write("")


# ---------------------------------
# Core gateway routes
# ---------------------------------
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


# ---------------------------------
# Safe auto-loader for district tools
# ---------------------------------
loaded_apis = []


def load_router_from_file(module_label: str, module_file: Path):
    """
    Load a Python module from file and register its router
    only if it exports a variable named 'router'.
    """
    module_name = f"{module_label}_{module_file.parent.name}"

    spec = importlib.util.spec_from_file_location(module_name, module_file)
    if spec is None or spec.loader is None:
        return

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, "router"):
        app.include_router(module.router)

        loaded_apis.append({
            "name": module_file.parent.name,
            "group": module_label,
            "path_hint": f"/{module_label.lower()}/{module_file.parent.name.lower().replace('_', '-')}"
        })


def load_district_group(group_name: str):
    """
    Scan a top-level folder such as Logic or Utility.
    Only load folders that contain main.py.
    """
    base_path = Path(group_name)

    if not base_path.exists() or not base_path.is_dir():
        return

    for child in sorted(base_path.iterdir()):
        if child.is_dir():
            module_file = child / "main.py"
            if module_file.exists():
                load_router_from_file(group_name, module_file)


# Load approved district groups only
load_district_group("Logic")
load_district_group("Utility")


# ---------------------------------
# API registry
# ---------------------------------
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
        ] + loaded_apis
    }
