from pathlib import Path

CAPABILITIES = [
    {
        "district": "Logic",
        "capability": "Boolean_Inverter",
        "route": "boolean-inverter",
        "function_name": "boolean_inverter",
        "params": [
            {"name": "value", "type": "bool"}
        ],
        "return_fields": [
            {"key": "input", "value": "value"},
            {"key": "output", "value": "not value"}
        ]
    },
    {
        "district": "Math",
        "capability": "Number_Doubler",
        "route": "number-doubler",
        "function_name": "number_doubler",
        "params": [
            {"name": "value", "type": "float"}
        ],
        "return_fields": [
            {"key": "input", "value": "value"},
            {"key": "output", "value": "value * 2"}
        ]
    },
    {
        "district": "Time",
        "capability": "Timestamp_Passthrough",
        "route": "timestamp-passthrough",
        "function_name": "timestamp_passthrough",
        "params": [
            {"name": "timestamp", "type": "str"}
        ],
        "return_fields": [
            {"key": "timestamp", "value": "timestamp"}
        ]
    }
]


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
    root = Path(".")

    for item in CAPABILITIES:
        district = item["district"]
        capability = item["capability"]
        route = item["route"]
        function_name = item["function_name"]
        params = item["params"]
        return_fields = item["return_fields"]

        district_path = root / district
        capability_path = district_path / capability
        main_file_path = capability_path / "main.py"

        district_path.mkdir(exist_ok=True)
        capability_path.mkdir(exist_ok=True)

        if main_file_path.exists():
            print(f"SKIPPED: {main_file_path}")
            continue

        code = build_code(
            district=district,
            route=route,
            function_name=function_name,
            params=params,
            return_fields=return_fields
        )

        main_file_path.write_text(code, encoding="utf-8")
        print(f"CREATED: {main_file_path}")


if __name__ == "__main__":
    main()
