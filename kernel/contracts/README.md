# Kernel Contracts Directory

Purpose
- Define the shape and conventions of Kernel Contracts: the formal interface specifications that plugins declare to the Kernel.

What belongs here (architecture only)
- Contract descriptions (interface definitions, input/output assertions) expressed as human-readable documents or machine-readable stubs (no executable code).
- Example contract manifest templates that describe required fields for contract declarations (no rule logic, no executable schemas).

What is explicitly forbidden
- No business logic
- No executable code
- No rule engines or rule files

Notes
- Contracts describe obligations a plugin must attest to via a Compliance Proof. They do not implement validation. They do not contain domain-specific rules.