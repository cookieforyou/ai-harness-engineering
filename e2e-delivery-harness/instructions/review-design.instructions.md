---
name: review-design
description: Detailed technical instructions for review-design scenario execution
type: instruction
version: "1.1.0"
stage: review-design
---

# Instruction: 技术方案评审技术规范

## Overview

本文档定义了技术方案评审的评审维度和标准。

## Review Dimensions

| 维度 | 评审要点 | 权重 |
|------|----------|------|
| 需求匹配 | 满足业务需求 | 20% |
| 技术可行性 | 技术方案可行 | 20% |
| 安全性 | 安全风险可控 | 20% |
| 性能 | 性能满足要求 | 15% |
| 可维护性 | 易于维护 | 15% |
| 成本 | 成本合理 | 10% |

## Associated Assets

- **Scenario**: `scenarios/review-design/SCENARIO.md`
- **Prompt**: `prompts/review-design.prompt.md`
- **Agent**: `agents/review-design.agent.md`
- **Skill**: `skills/review-design/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for review-design.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for review-design execution.

1. **Practice 1**: Evaluate design against requirements and quality attributes
2. **Practice 2**: Check for consistency with architecture standards
3. **Practice 3**: Document review findings with severity and action items


## Error Handling

> Common error scenarios and resolution strategies for review-design.

### Error Category 1
**Symptom**: Design does not satisfy key requirements
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Review feedback is vague or not actionable
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for review-design deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Issue detection rate is 95% or higher | Automated check |
| Standard 2 | Review turnaround is 2 days or less | Automated check |
| Standard 3 | Defect escape rate after review is 5% or lower | Automated check |
