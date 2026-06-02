# Copilot Instructions for E2E Delivery Harness

## Overview

This file provides instructions for AI assistants (Copilots) working with the E2E Delivery Harness asset library.

**Primary guide**: [AGENTS.md](AGENTS.md)  
**Compliance baseline**: [standards/harness-engineering.md](standards/harness-engineering.md) (Harness 六层模型)

## General Guidelines

### 1. Asset Discovery

When asked to assist with delivery tasks:

1. Read [AGENTS.md](AGENTS.md) execution protocol (R1–R5)
2. Identify pipeline stage via `workflows/*.pipeline.md`
3. Load assets in order:
   - `scenarios/{base}/SCENARIO.md`
   - `agents/{base}.agent.md` (confirm `tools` in YAML)
   - `prompts/{base}.prompt.md` (Variables → CoT → Output Validation → Handover)
   - `instructions/` and `skills/` as needed

### 2. Role Activation

When activating a specific role:

```
1. Read the .agent.md file for role definition
2. Load associated skills and instructions
3. Reference relevant prompts as needed
4. Follow the workflow defined in the scenario
```

### 3. Output Quality

Ensure all outputs meet the standards defined in:

- `standards/harness-engineering.md` - Harness compliance
- `standards/naming-conventions.md` - Naming rules
- `standards/output-quality-rubric.md` - Quality criteria
- `evaluations/output-validation-checklist.md` - Pre-handoff validation
- `evaluations/regression-checklist.md` - Phase regression

## Phase-Specific Instructions

### Requirement Analysis

- Focus on understanding business goals and constraints
- Identify stakeholders and user needs
- Output structured requirement specifications

### System Design

- Translate requirements into technical solutions
- Define system architecture and components
- Consider non-functional requirements

### Task Decomposition

- Break down work into manageable units
- Identify dependencies and sequencing
- Estimate effort and allocate resources

### Development

- Follow coding standards and best practices
- Produce clean, maintainable code
- Include appropriate documentation

### Testing

- Design comprehensive test cases
- Execute tests and document results
- Track and manage defects

### Deployment

- Follow deployment procedures
- Prepare rollback plans
- Ensure smooth transitions

### Monitoring

- Set up appropriate metrics and alerts
- Document operational procedures
- Plan for incident response

## Quality Gates

Before advancing to the next phase, verify:

1. Current phase outputs are complete
2. Quality standards are met
3. Documentation is updated
4. Stakeholders are aligned

## Handoff Protocol

When transitioning between phases or roles:

1. Summarize completed work
2. List pending items and assumptions
3. Provide context for next phase
4. Flag potential risks
