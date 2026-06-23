# E2E Delivery Harness Usage Guide

> **Compliance Status**: 🟢 **95.3% A+** (verified via `python3 scripts/harness-compliance-check.py`)
> **Primary Protocol**: [AGENTS.md](./AGENTS.md)

## Table of Contents

1. [Asset Overview](#asset-overview)
2. [Usage Process](#usage-process)
3. [Scenario Selection](#scenario-selection)
4. [Quality Assurance](#quality-assurance)
5. [Best Practices](#best-practices)

---

## Asset Overview

### Asset Types and Responsibilities

| Type | Purpose | Format | Load Order |
|------|---------|--------|-----------|
| Workflow | Pipeline stage order, entry/exit criteria | `workflows/*.pipeline.md` | ① First |
| Scenario | Entry point: Purpose + CoT + DC-* + Error Handling + KPI | `scenarios/*/SCENARIO.md` | ② |
| Agent | Role identity: Working Rules + I/O Contract + Tools + Handoff | `agents/*.agent.md` | ③ Concurrent |
| Prompt | Execution script: Variables → CoT → Validation → Handover | `prompts/*.prompt.md` | ④ Main document |
| Instruction | Operational runbook: Tools + Environment + Config | `instructions/*.instructions.md` | ⑤ As needed |
| Skill | Domain knowledge: Methodology + Best Practices + Pitfalls | `skills/*/SKILL.md` | ⑥ As needed |
| Standard | Standards: Naming / Quantification / Quality / Asset Model | `standards/*.md` | ⑦ Pre-gate |
| Evaluation | Checklists: Regression / Scorecard / Error Patterns | `evaluations/*.md` | ⑧ Phase end |

### Asset Scale

| Category | Count | Grade |
|----------|------|-------|
| Scenario | 37 | 100.0% A |
| Agent | 37 | 98.1% A |
| Prompt | 37 | 97.1% A |
| Instruction | 37 | 94.8% A |
| Skill | 37 | 100.0% A |
| Standard | 44 | 94.7% A |
| Evaluation | 27 | 100.0% A |
| Template | 26 | 92.9% A |
| **Total** | **282** | **95.3% A+** |

---

## Usage Process

### Step 1: Identify Pipeline Stage

Check `workflows/e2e-delivery.pipeline.md` to confirm current pipeline and stage:

```
analyze-requirement → design-system → decompose-task
  → implement-feature → verify-test → deploy-release → monitor-operate
```

For incidents, switch to `workflows/incident-response.pipeline.md` (Detect → Respond → Recover → Review).

### Step 2: Load Scenario Entry

Read `scenarios/{name}/SCENARIO.md`:

- **Purpose / Business Value**: Why this scenario exists
- **Chain of Thought**: Mandatory step-by-step reasoning protocol
- **Decision Checkpoints**: DC-001 to DC-006 with trigger conditions and criteria
- **Error Handling**: P0-P4 scenarios with escalation thresholds
- **Quality Metrics**: Weighted KPI scoring with 3-tier thresholds (70/85/95)

### Step 3: Configure Agent Role

Read `agents/{name}.agent.md`:

1. **Role Definition**: Core responsibilities and professional capabilities
2. **Use When / Not Applicable**: Activation and exclusion conditions
3. **Working Rules**: Principles + YAML workflow steps
4. **Expected Input / Output**: Field-level validation rules
5. **Handoff**: Structured YAML template for downstream stage
6. **Quality Checklist**: Pre/During/Post execution checks

### Step 4: Execute via Prompt

Use `prompts/{name}.prompt.md` as the main execution document:

1. **Input Variables**: Verify all `Required: true` variables are populated
2. **Chain of Thought**: Execute step by step, `[VALIDATE]` after each step
3. **Error Handling**: Reference Scenario error flows on exceptions
4. **Output Validation**: Verify output against V-001~V-004 criteria
5. **Handover Preparation**: Fill in the YAML handoff package

### Step 5: Reference Skill and Instruction (as needed)

- Load `skills/{name}/SKILL.md` for domain expertise (Best Practices + Common Pitfalls)
- Load `instructions/{name}.instructions.md` for operational details (tools + environment + config)

### Step 6: Quality Assessment and Gate Exit

1. Run `evaluations/output-validation-checklist.md` for generic validation
2. Run `evaluations/regression-checklist.md` for phase-specific sections
3. Check `evaluations/common-error-patterns.md` for known anti-patterns
4. Verify KPIs against `standards/id-generation-quantification.md`
5. Update `contexts/global-context.md` and execute Handover

---

## Scenario Selection

### Quick Route by Intent

| User says… | Primary Scenario | Optional Parallel |
|------------|-----------------|-------------------|
| Analyze/clarify requirements | `analyze-requirement` | `plan-sprint` |
| Design architecture | `design-system` | `design-architecture`, `design-database`, `review-design` |
| Break down tasks | `decompose-task` | `plan-sprint` |
| Write code | `implement-feature` | `integrate-api`, `manage-dependencies`, `manage-tech-debt` |
| Test | `verify-test` | `automate-test`, `performance-testing` |
| Deploy | `deploy-release` | `prepare-release`, `plan-rollback`, `implement-cicd` |
| Production issue | `respond-incident` | `apply-hotfix`, `review-incident` |
| Security/compliance | `audit-security` | `manage-secrets` |
| Performance tuning | `optimize-performance` | `plan-capacity` |
| Documentation debt | `document-project` | `manage-knowledge` |

### Decision Tree

```
Production incident?
  Yes → respond-incident → (need code fix?) apply-hotfix → review-incident
  No → Which phase?
        Requirements → analyze-requirement
        Design → design-system (+ specialized design)
        Development → implement-feature (+ manage-dependencies)
        Testing → verify-test
        Deployment → deploy-release (+ plan-rollback)
        Operations → monitor-operate
```

---

## Quality Assurance

### Compliance Check

```bash
# Full compliance audit (1,974 checks)
python3 scripts/harness-compliance-check.py

# Single category
python3 scripts/harness-compliance-check.py --category agents

# Single file
python3 scripts/harness-compliance-check.py --file agents/deploy-release.agent.md
```

### Quality Gates (Pipeline Level)

| Transition | Gate | Standard |
|------------|------|----------|
| Req → Design | Q-001 | REQ-COVER ≥ 95% |
| Design → Task | Q-002 | Design review 100% passed |
| Task → Dev | Q-003 | TASK-COVER ≥ 98% |
| Dev → Test | Q-004 | DEV-COVERAGE ≥ 80% |
| Test → Deploy | Q-005 | TEST-PASS ≥ 90% |
| Deploy → Ops | Q-006 | DEPLOY-SUCCESS ≥ 99% |
| Ops steady | Q-007 | MON-SLO ≥ 99.5% |

### Scoring System

Aligned with [evaluations/scorecard-template.md](./evaluations/scorecard-template.md):

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A (Excellent) | Exceeds expectations |
| 80-89 | B (Good) | Meets expectations with minor improvements |
| 70-79 | C (Satisfactory) | Meets basic requirements (minimum exit) |
| 60-69 | D (Needs Improvement) | Significant deficiencies |
| 0-59 | F (Fail) | Does not meet requirements |

---

## Best Practices

### 1. Five Non-Negotiable Rules (R1-R5)

| # | Rule | Consequence of Violation |
|---|------|--------------------------|
| R1 | Scenario before Prompt | Skipped quality gates and error handling |
| R2 | No execution with unfilled variables | Untraceable outputs, broken handoffs |
| R3 | VALIDATE after every CoT step | Hallucinated requirements / design drift |
| R4 | Quantify before gate exit (against KPIs) | Cannot advance to next stage |
| R5 | Always Handover (YAML handoff) | Downstream agent context broken |

### 2. Progressive Adoption

Start with the core 7 scenarios, then gradually introduce extended scenarios as needed.

### 3. Context Passing

Each stage's output must serve as the next stage's input — use `contexts/unified-handover-template.md` YAML handoff template.

### 4. Iterative Optimization

Run `python3 scripts/harness-compliance-check.py` periodically to audit and continuously improve asset quality.

### 5. Team Collaboration

When multiple Agents collaborate, follow the Handoff YAML contract: clarify `from_stage`/`to_stage` routing and `artifacts` deliverables.

---

## FAQ

### Q: How to choose the right scenario?
A: See [Scenario Selection](#scenario-selection) decision tree and routing table, or check [AGENTS.md full scenario directory](./AGENTS.md).

### Q: How to ensure output quality?
A: Every Prompt includes Output Validation (V-001~V-004). Verify against `evaluations/` checklists; revert and fix if not passing.

### Q: How to contribute new assets?
A: Reference `standards/authoring-checklist.md` and [AGENTS.md maintenance section](./AGENTS.md). Copy from `templates/`, pass compliance checks, then submit.

### Q: How to check asset library compliance status?
A: Run `python3 scripts/harness-compliance-check.py` for real-time compliance report, or read the [Deep Analysis Report](./资产库全面评估深度分析报告.md).

---

## Related Documents

| Document | Purpose |
|----------|---------|
| [AGENTS.md](./AGENTS.md) | Agent navigation and execution protocol |
| [INTRODUCTION.en.md](./INTRODUCTION.en.md) | Project introduction |
| [资产库全面评估深度分析报告.md](./资产库全面评估深度分析报告.md) | Comprehensive assessment (v3.0) |
| [standards/harness-engineering.md](./standards/harness-engineering.md) | Harness six-layer alignment standard |
| [workflows/e2e-delivery.pipeline.md](./workflows/e2e-delivery.pipeline.md) | Main delivery pipeline |
| [copilot-instructions.md](./copilot-instructions.md) | Copilot/IDE integration guide |
