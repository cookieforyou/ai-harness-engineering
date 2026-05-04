---
name: plan-capacity
description: Detailed technical instructions for plan-capacity scenario execution
type: instruction
version: "1.1.0"
stage: plan-capacity
---

# Instruction: 容量规划技术规范

## Overview

本文档定义了容量规划的技术规范和方法。

## 容量评估方法

### 指标采集
- CPU 利用率
- 内存利用率
- 存储利用率
- 网络带宽
- TPS/QPS

### 扩容策略

| 策略 | 适用场景 | 成本 |
|------|----------|------|
| 垂直扩展 | 小规模 | 中 |
| 水平扩展 | 大规模 | 中高 |
| 混合扩展 | 复杂系统 | 高 |

## Associated Assets

- **Scenario**: `scenarios/plan-capacity/SCENARIO.md`
- **Prompt**: `prompts/plan-capacity.prompt.md`
- **Agent**: `agents/capacity-planner.agent.md`
- **Skill**: `skills/plan-capacity/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for plan-capacity.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for plan-capacity execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for plan-capacity.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for plan-capacity deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
