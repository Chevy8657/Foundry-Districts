# Engineering Constitution

This document translates the business Foundry Constitution into an engineering contract and a layered architecture. It defines what may read and write each layer, the immutability guarantees, and the enforcement patterns that keep Foundry trustworthy.

> Note: The authoritative business doctrine remains in Notion. This engineering constitution implements contract checks so engineering cannot drift from doctrine.

## Foundational Principle
- The engine may suggest changes but cannot apply them. AI proposes; humans govern.

## Layers

### Layer 1 — Constitution (Business)
- Read Only in engineering systems. Managed and governed by humans via Notion.

### Layer 2 — Operational Truth Layer (Append-Only)
- Previously: "Operational Data (Record Layer)"; renamed to emphasize verified truth.
- Append-only ledger of immutable evidence pointers and metadata. Stores references to raw evidence (immutable object store) and required provenance fields.

### Layer 3 — Compute Engine
- Stateless compute that reads Constitution + Operational Truth and produces deterministic Metrics. Cannot mutate records or doctrine.

### Layer 4 — Interpretation Engine (VANCE)
- Interprets computed metrics and produces Recommendations. Must cite evidence and rule versions. Cannot invent facts or mutate records.

### Layer 5 — Presentation
- Executive Operating Review™, Command Center, Reports. Read-only for doctrine and truth; humans act on recommendations.

## Engineering Contract (Who can read/write)

| Layer                 | Can Read                        | Can Write                  |
|----------------------:|---------------------------------|---------------------------:|
| Constitution          | —                               | Human Governance Only      |
| Operational Truth     | Constitution                     | Append Only (ingest agents)|
| Compute               | Constitution + Operational Truth | Metrics Only               |
| VANCE (Interpretation)| Constitution + Operational Truth + Metrics | Recommendations Only |
| Executive Review      | Everything                       | Nothing                    |

## Core Enforcement Rules
- All evidence must include provenance metadata: source_id, ingestion_timestamp, ingestion_hash, ingestion_agent_id, original_uri, and rule_version (when applicable).
- Every verification outcome records the rule_version (immutable reference to the rule commit or Notion revision) used to produce it.
- The ledger is append-only at the API and DB level; updates can only be performed by creating compensating events (never overwriting historical records).
- Compute pipelines must be deterministic and replayable from the ledger and rule versions.
- VANCE must attach citations to the exact evidence items and rule versions that support any interpretation or recommendation.
- Any change that would modify doctrine or rules requires human approval and a documented decision in the Notion Decision Log.

## Rule Management
- Doctrine & rules are authored in Notion but exported to a machine-readable format (YAML or JSON) stored in `/rules` with tests and examples.
- Rule changes are versioned in Git and must include unit tests and positive/negative examples that run in CI.
- CI must block merges where rule changes change computed executive metrics without explicit human review and approval.

## Auditability & Replay
- All metrics and recommendations must be recomputable by replaying ledger events with the same rule_version.
- Provide an audit export format (JSON/CSV) that includes evidence hashes, rule_version, and event_ids for every metric.

## Security & Privacy
- Evidence storage must support encryption at rest and in transit.
- PII must be redacted before inclusion in executive views; raw evidence may be segregated with tighter access controls.
- RBAC enforces Creator ≠ Verifier and restricts who can push rule changes to production.

## Recommended Developer Workflows
- Notion → rules export creates PR against `/rules` with rule files and tests.
- PR template requires: linkage to Notion doctrine page, list of test cases, traceability checklist.
- CI runs: lint, unit tests, rule-tests, replay-tests for affected metrics, Notion manifest consistency check.

## Next steps (engineering)
1. Add a Notion export manifest and a `/rules` directory with a sample rule and test.
2. Scaffold a minimal ingest + ledger schema and a deterministic compute example.
3. Add PR and CI templates that enforce the engineering contract.

---

This file is a living, enforceable engineering contract. When you approve, I can scaffold the `/docs` entry, `/rules` export, CI checks, or a minimal Python prototype to start enforcing these rules.
