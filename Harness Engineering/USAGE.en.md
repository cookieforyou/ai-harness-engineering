# Usage Guide

## 1. Asset Reference Path Convention

All assets are referenced relative to this library root:

```yaml
# Scenario orchestration example (scenarios/code-review.yaml)
agent:
  role: "agents/senior-engineer.role.md"
  instructions:
    system: "instructions/code-review-system.md"
    safety: "instructions/safety-guardrails.md"
  skills:
    - "skills/static-analysis.yaml"
    - "skills/security-audit.yaml"
  prompts:
    main: "prompts/code-review/v1.md"
    report: "prompts/code-review/report-template.md"
  evaluation:
    checkpoint: "evaluations/code-review-checkpoint.yaml"
```

---

## 2. Workflow: From Requirement to Delivery

### Step 1: Scenario Identification
Match or create a scenario in `scenarios/` based on business requirements:
- If a match exists → reuse with variable substitution
- If not → create new using `templates/scenario-skeleton/`

### Step 2: Asset Assembly
Compose assets from each module according to the scenario declaration:
```
Scenario ( orchestration )
  ├── Agent (role + goal)
  ├── Instructions (system + constraints)
  ├── Skills (tool calling + atomic capabilities)
  ├── Prompts (context + task definition)
  └── Evaluation (quality gate + feedback)
```

### Step 3: Execution & Evaluation
1. Load the scenario using an orchestration engine (LangChain / AutoGen / custom Harness Runner)
2. Agent executes according to the strategy layer plan
3. Each checkpoint triggers evaluation logic from `evaluations/`
4. Failed gates trigger retry or human escalation

### Step 4: Asset Maturation
- Execution logs and traces go into the observability system
- Successful new combinations are solidified back into the library (per `standards/versioning.md`)
- Failure cases are added to `evaluations/` as negative examples

---

## 3. Directory-Level Usage

### agents/
Stores role definitions. Each Agent must include:
- `{agent-name}.role.md` — Role card (goal, personality, capabilities, limits)
- `{agent-name}.config.yaml` — Runtime config (model params, tool bindings, timeout strategy)

### evaluations/
Stores evaluation definitions. Each checkpoint includes:
- `{checkpoint-name}.yaml` — Metrics, scoring dimensions, pass thresholds
- `{checkpoint-name}-dataset.jsonl` — Evaluation dataset (optional)

### instructions/
Stores instruction files. Categorized by scope:
- `system/` — System-level behavioral constraints
- `safety/` — Safety guardrails and compliance requirements
- `format/` — Output format enforcement

### prompts/
Stores prompt templates. Organization:
- Grouped by domain, e.g., `prompts/code-review/`, `prompts/doc-gen/`
- Version management within each directory: `v1.md`, `v2.md`
- Template variables use `{{variable_name}}` double-brace notation

### scenarios/
Stores scenario orchestrations. Each scenario is an independent directory:
```
scenarios/{scenario-name}/
├── README.md           # Scenario description, I/O definitions
├── flow.yaml           # Orchestration definition (nodes, edges, conditionals)
├── checkpoint.yaml     # Checkpoint configuration
└── assets.lock         # Dependency asset version lock
```

### skills/
Stores skill modules. Each skill must include:
- `{skill-name}.yaml` — Skill description, I/O schema, implementation type (LLM / Tool / Code)
- `{skill-name}/` — Expanded subdirectory for complex skills

### standards/
Stores specification documents. Required reading:
- `naming-convention.md` — Naming conventions
- `versioning.md` — Version management strategy
- `quality-checklist.md` — Asset onboarding checklist

### templates/
Stores project templates. Choose as needed:
- `project-scaffold/` — New project AI Harness initialization template
- `scenario-skeleton/` — Minimal structure for new scenarios
- `agent-template/` — Minimal structure for new agents

---

## 4. Version Locking & Compatibility

Scenarios lock dependency asset versions via `assets.lock`:

```yaml
# assets.lock example
lock_version: "1.0"
dependencies:
  - asset: "prompts/code-review/v1.md"
    checksum: "sha256:abc123..."
  - asset: "skills/static-analysis.yaml"
    version: "^2.1.0"
```

Upgrading dependencies requires re-running the evaluation suite to verify compatibility.
