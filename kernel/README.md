# Foundry Kernel

This README defines the Foundry Kernel: its purpose, the constitutional authority it enforces, its boundaries, how plugins communicate with it, and the definition of a Compliance Proof. This document defines the Kernel; it does not implement it.

1. What is the Kernel?

The Kernel is the minimal, technology-agnostic enforcement layer that ensures all system components (plugins, services, and pipelines) comply with the Foundry Business Constitution and the Engineering Constitution. The Kernel is an interface and contract: it specifies what compliance means, how it is proven, and how the system adjudicates compliance at a conceptual level.

2. What constitutional authority does it enforce?

The Kernel enforces the Business Constitution and the Engineering Constitution as the supreme authorities. It encodes the engineering contract constraints: append-only truth guarantees, read/write permissions per layer, human-governance requirements, traceability requirements, and the prohibition on runtime changes to doctrine.

3. What is explicitly outside the Kernel?

The Kernel contains zero business logic and no domain-specific rules. It does not know about Specialists, Workforce, Executive Review, TimeOff™, IPEs, Recommendations, Industries, or any product-specific concepts. It does not implement ingestion, compute, interpretation, presentation, authentication, storage, or deployment mechanisms. It defines the contract those systems must satisfy, not how they satisfy it.

4. How does a plugin communicate with the Kernel?

Plugins communicate with the Kernel by declaring adherence to one or more Kernel Contracts. A plugin provides:

- A contract declaration describing the interface it implements and the assertions it makes about its outputs.
- A Compliance Proof (see question 5) attesting that the plugin's outputs satisfy the contractual obligations and constitutional constraints.

The Kernel's role is to validate the contract declaration and verify the Compliance Proof against the constitutional rules. Communication is expressed at the level of contracts and proofs (interfaces and attestations), not implementation details.

5. What is a Compliance Proof?

A Compliance Proof is an attestation artifact supplied by a plugin that demonstrates, at the time of issuance, that the plugin's outputs and behavior conform to the relevant constitutional constraints and Kernel Contracts. A Compliance Proof contains:

- Reference to the constitution(s) and specific clause(s) relied upon.
- The contract(s) the plugin implements.
- A description of the evidence or artifacts that substantiate conformity (e.g., test-suite references, immutable artifact references, human approval records).
- A version identifier for the plugin's contract and the rule/rule-set versions used to produce outputs.

Compliance Proofs are not evaluated by the Kernel as business decisions; they are validated for structural and traceable conformity to constitutional requirements. Human governance is required for doctrinal changes; the Kernel only enforces compliance, it does not change doctrine.

Acceptance test (definition):

- The Kernel defines interfaces and validators only. It contains zero product/business logic. Any file or artifact under `kernel/` must only describe contracts, validators, audit formats, or versioning policies at an architectural level.

Stop here. Do not implement the Kernel. Define it.