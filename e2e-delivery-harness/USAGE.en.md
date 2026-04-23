# E2E Delivery Harness Usage Guide

## Table of Contents

1. [Asset Overview](#asset-overview)
2. [Usage Process](#usage-process)
3. [Role Configuration](#role-configuration)
4. [Quality Assurance](#quality-assurance)
5. [Best Practices](#best-practices)

---

## Asset Overview

### Asset Types

| Type | Purpose | Format |
|------|---------|--------|
| Agent | Define AI role identity and rules | `*.agent.md` |
| Skill | Encapsulate domain capabilities | `skills/*/SKILL.md` |
| Instruction | Provide operational guidelines | `*.instructions.md` |
| Prompt | Guide AI output generation | `*.prompt.md` |
| Scenario | Combine assets into workflows | `scenarios/*/SCENARIO.md` |
| Standard | Define standards and checks | `standards/*.md` |

---

## Usage Process

### Step 1: Identify Delivery Phase

Select the appropriate scenario based on current project phase:

```
Requirement Analysis → System Design → Task Decomposition → Development → Testing → Deployment → Monitoring
```

### Step 2: Configure Role Assets

1. Read the corresponding **Agent** definition file
2. Understand role tool permissions and working rules
3. Adjust role configuration as needed

### Step 3: Reference Skills and Instructions

1. Load corresponding **Skill** under Agent guidance
2. Follow steps in **Instruction**
3. Reference **Prompt** templates for input construction

### Step 4: Execute and Produce

1. Execute tasks according to skill definitions
2. Self-check using instruction checklists
3. Output results that meet standards

### Step 5: Quality Assessment

1. Use `evaluations/regression-checklist.md` for regression checks
2. Reference `evaluations/scorecard-template.md` for scoring
3. Return to corresponding phase for fixes if issues found

---

## Role Configuration

### Role List

| Role | Responsibility | Phase |
|------|----------------|-------|
| Requirement Analyst | Requirement analysis and planning | Requirement Analysis |
| System Designer | System architecture design | System Design |
| Task Decomposer | Task decomposition and planning | Task Decomposition |
| Developer | Code development | Development |
| Tester | Testing and verification | Testing |
| DevOps Engineer | Deployment and release | Deployment |
| SRE Monitor | Monitoring and operations | Monitoring |

---

## Quality Assurance

### Checklist

After completing each phase, perform these checks:

1. **Input Completeness**: Are all required inputs included?
2. **Output Compliance**: Does it meet output format requirements?
3. **Quality Standards**: Does it meet quality assessment standards?
4. **Documentation Completeness**: Are necessary documents included?

### Scoring System

Use 1-5 scoring:

- 5: Excellent - Fully meets all standards
- 4: Good - Basically meets with minor improvement space
- 3: Acceptable - Meets core requirements
- 2: Needs improvement - Has obvious deficiencies
- 1: Unacceptable - Does not meet basic requirements

---

## Best Practices

### 1. Progressive Usage

Start with a single phase and gradually expand to the complete process.

### 2. Context Passing

Each phase's output should serve as the next phase's input, ensuring information continuity.

### 3. Iterative Optimization

Continuously optimize asset definitions based on actual usage feedback.

### 4. Team Collaboration

When multiple AI roles collaborate, clarify primary/secondary relationships and handover specifications.
