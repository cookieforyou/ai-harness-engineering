---
name: {scenario-name}
description: Execution prompt for {scenario-name} scenario
type: execution
version: "1.1.0"
stage: "{scenario-name}"
---

# {Scenario Title}

## Task Description

> Describe the specific task for the {scenario-name} scenario execution.
>
> AI must understand the context, objectives, and success criteria before proceeding.

## Input Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `var_name` | type | true/false | Description |

## Execution Flow

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core {scenario-name} activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality

## Output Format

```
## {scenario-name} Deliverables

### Summary
- Status: [completed|partial|blocked]
- Completion: [percentage]

### Outputs
- [List of generated artifacts]

### Next Steps
- [Recommended follow-up actions]
```

## Error Handling

| Error Code | Description | Resolution |
|------------|-------------|------------|
| ERR_001 | [Error description] | [Resolution steps] |

## Handover Preparation

- [ ] All deliverables generated
- [ ] Quality checks passed
- [ ] Next stage dependencies documented
