# AI Harness Assets Library Introduction

## What is the AI Harness Assets Library

This assets library is the engineering implementation of the **Harness Engineering** methodology. It structurally consolidates all control elements required in AI delivery—Agents, Instructions, Prompts, Evaluations, Scenarios, and Skills—into an orchestrable, reusable, and evolvable asset system.

> **Core Philosophy**: "Humans steer, Assets enable, Agents execute."

---

## Why a Unified Assets Library

AI engineering teams commonly face these challenges:

- **Scattered prompts**: Repeated reinvention across projects with inconsistent quality
- **Unpredictable Agent behavior**: Lack of unified role definitions and constraints
- **Missing evaluations**: Inability to quantify AI output quality or improve continuously
- **Fragmented scenarios**: Broken E2E flows with chaotic human intervention points
- **Knowledge attrition**: Loss of core engineering expertise when team members change

This library solves these problems through systematic design across **eight modules**.

---

## Eight Modules Overview

| Module | Responsibility | Typical Deliverables |
| :--- | :--- | :--- |
| **agents** | Define AI Agent roles, goals, capability boundaries, and toolsets | Role Cards, Agent Configuration Files |
| **evaluations** | Establish quality assessment systems covering correctness, safety, usability | Evaluation Datasets, Scoring Rubrics, Automated Test Scripts |
| **instructions** | Author system-level instructions and behavioral constraints | System Prompts, Safety Guardrails, Output Format Constraints |
| **prompts** | Accumulate high-quality, scenario-specific prompt templates | Categorized Prompt Library, Parameterized Templates |
| **scenarios** | Orchestrate end-to-end workflows defining I/O, steps, and human-AI collaboration | Scenario Specs, Flow Diagrams, Orchestration YAML |
| **skills** | Package reusable atomic capabilities for Agents or scenarios | Skill Definitions, Tool Function Descriptions, Schemas |
| **standards** | Define asset conventions, naming rules, versioning strategy, and best practices | Specification Docs, Checklists |
| **templates** | Provide project scaffolds and quick-start templates | Project Templates, Initialization Scripts, Sample Code |

---

## Mapping to the Six-Layer Architecture

This library directly maps to the Harness Engineering six-layer technical architecture:

```
Goal Layer        →  scenarios/ + agents/ define goals and success criteria
Strategy Layer    →  skills/ + prompts/ provide planning and reasoning capabilities
Tooling Layer     →  skills/ integrate external tool interfaces
Constraint Layer  →  instructions/ + standards/ enforce boundary controls
Feedback Layer    →  evaluations/ complete the quality feedback loop
Observability Layer → standards/ define logging, tracing, and audit conventions
```

---

## Next Steps

- Learn how to use: [USAGE.en.md](./USAGE.en.md)
- Explore typical scenarios: [scenarios/README.md](./scenarios/README.md)
- Read specification standards: [standards/README.md](./standards/README.md)
