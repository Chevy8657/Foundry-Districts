# Foundry Compiler (Minimal CLI)

Purpose
- A minimal, safe compiler that reads a Foundry Definition and generates a plugin skeleton that includes constitutional references and a Compliance Proof template.

Scope & Constraints
- No business logic is generated.
- No /rules, no databases, no FastAPI, no UI, no doctrine changes.
- The compiler refuses to generate if constitution references are missing in the Foundry Definition.

Usage
- Run locally in a Python environment:

  python compiler.py example_definition.yaml --out-dir generated_example

Requirements
- Python 3.8+
- PyYAML (optional). If PyYAML is not installed, supply a JSON input instead.

Acceptance Test
- Running the CLI against the provided example_definition.yaml will create a generated plugin skeleton under `generated_example/` with manifest.yaml and compliance-proof-template.json that include constitutional references.
