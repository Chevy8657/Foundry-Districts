import json
from pathlib import Path


def build_params(params):
    parts = []
    for param in params:
        parts.append(f'{param["name"]}: {param["type"]}')
    return ", ".join(parts)


def build_return_block(return_fields):
    lines = []
    for field in return_fields:
        lines.append(f'        "{field["key"]}": {field["value"]}')
    return ",\n".join(lines)


def build_code(district, route, function_name, params, return_fields):

    prefix = district.lower()

    param_string = build_params(params)
    return_block = build_return_block(return_fields)

    code = f'''from fastapi import APIRouter

router = APIRouter(prefix="/{prefix}")

@router.get("/{route}")
def {function_name}({param_string}):
    return {{
{return_block}
    }}
'''
    return code


def main():

    manifest_path = Path("factory_manifest.json")

    if not manifest_path.exists():
        print("ERROR: factory_manifest.json not found")
        return

    with open(manifest_path) as file:
        capabilities = json.load(file)

    root = Path(".")

    for item in capabilities:

        district = item["district"]
        capability = item["capability"]
        route = item["route"]
        function_name = item["function_name"]
        params = item["params"]
        return_fields = item["return_fields"]

        district_folder = root / district
        capability_folder = district_folder / capability
        main_file = capability_folder / "main.py"

        district_folder.mkdir(exist_ok=True)
        capability_folder.mkdir(exist_ok=True)

        if main_file.exists():
            print(f"SKIPPED: {main_file}")
            continue

        code = build_code(
            district,
            route,
            function_name,
            params,
            return_fields
        )

        main_file.write_text(code, encoding="utf-8")

        print(f"CREATED: {main_file}")


if __name__ == "__main__":
    main()
