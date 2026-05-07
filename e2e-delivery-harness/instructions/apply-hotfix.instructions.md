---
name: apply-hotfix
description: "Detailed technical instructions for apply-hotfix scenario execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instruction: 紧急修复技术规范

## Overview

This instruction establishes the emergency response technical standards and execution procedures for production apply-hotfix scenarios. It covers rapid defect triage, minimal-change fix strategies, expedited testing protocols, and safe deployment procedures under time pressure. The instruction balances speed with safety by defining risk-based approval workflows, rollback-ready deployment practices, and communication cadences appropriate for P0/P1 incidents. Key focus areas include change scope minimization, regression test prioritization, and post-apply-hotfix permanent-fix planning to prevent recurring emergency patches.


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

- **Scenario**: `scenarios/apply-hotfix/SCENARIO.md`
- **Prompt**: `prompts/apply-hotfix.prompt.md`
- **Agent**: `agents/apply-hotfix.agent.md`
- **Skill**: `skills/apply-hotfix/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for apply-hotfix.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for apply-hotfix execution.

1. **Practice 1**: Prioritize apply-hotfix severity and impact assessment
2. **Practice 2**: Maintain minimal change scope to reduce regression risk
3. **Practice 3**: Validate fix through targeted testing before deployment


## Error Handling

> Common error scenarios and resolution strategies for apply-hotfix.

### Error Category 1
**Symptom**: Hotfix introduces new defects or regressions
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Emergency deployment bypasses standard validation
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for apply-hotfix deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Hotfix resolves the target defect without regression | Automated check |
| Standard 2 | Hotfix deploys within 4 hours for P0 issues | Automated check |
| Standard 3 | All apply-hotfixes have follow-up plans for permanent fixes | Automated check |
