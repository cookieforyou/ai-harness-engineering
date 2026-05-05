---
name: hotfix
description: Detailed technical instructions for hotfix scenario execution
type: instruction
version: "1.1.0"
stage: hotfix
---

# Instruction: 紧急修复技术规范

## Overview

本文档定义了紧急修复阶段的技术规范和执行标准。

## Emergency Fix Process

```
问题报告 → 评估 → 定位 → 修复 → 验证 → 上线
```

## Response Time Requirements

| 严重等级 | 响应时间 | 修复时间 | 上线时间 |
|----------|----------|----------|----------|
| P0 | 15 分钟 | 1 小时 | 2 小时 |
| P1 | 30 分钟 | 4 小时 | 8 小时 |
| P2 | 1 小时 | 24 小时 | 48 小时 |

## Associated Assets

- **Scenario**: `scenarios/hotfix/SCENARIO.md`
- **Prompt**: `prompts/hotfix.prompt.md`
- **Agent**: `agents/hotfix-engineer.agent.md`
- **Skill**: `skills/hotfix/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for hotfix.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for hotfix execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for hotfix.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for hotfix deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
