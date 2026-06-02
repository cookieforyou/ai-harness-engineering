---
name: {agent-name}
description: "{agent-description}"
type: agent
tools: ["search", "read", "edit", "analyze"]
harness_layers: [goal, strategy, tooling, constraint, feedback, observability]
version: "1.2.0"
status: active
tags: [agent]
---

# Agent: {Agent Role}

## Role Definition

{Role definition for this scenario}

## Core Responsibilities

1. **Responsibility 1**: [Description]
2. **Responsibility 2**: [Description]
3. **Responsibility 3**: [Description]

## Use When

Activate this agent when:
- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]

## Working Rules

1. **Rule 1**: [Rule description]
2. **Rule 2**: [Rule description]
3. **Rule 3**: [Rule description]
4. **Rule 4**: [Rule description]

## Expected Input

```yaml
input_context:
  - field: "[input_field_1]"
    type: "[type]"
    required: true
    description: "[Description]"
  - field: "[input_field_2]"
    type: "[type]"
    required: false
    description: "[Description]"
```

## Expected Output

```yaml
output_deliverables:
  - artifact: "[output_artifact_1]"
    format: "[format]"
    validation: "[validation criteria]"
  - artifact: "[output_artifact_2]"
    format: "[format]"
    validation: "[validation criteria]"
```

## Handoff

### To Agent: [Next Agent]
**Trigger**: [When to hand off]
**Data**: [What data to pass]

### From Agent: [Previous Agent]
**Trigger**: [When this agent receives control]
**Data**: [What data is received]

## Associated Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/{scenario-name}/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/{scenario-name}.prompt.md` | Execution prompt |
| Instructions | `instructions/{scenario-name}.instructions.md` | Technical instructions |
| Skill | `skills/{scenario-name}/SKILL.md` | Domain skill |
