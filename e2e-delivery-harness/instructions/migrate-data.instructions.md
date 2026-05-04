---
name: migrate-data
description: Detailed technical instructions for migrate-data scenario execution
type: instruction
version: "1.1.0"
stage: migrate-data
---

# Instruction: 数据迁移技术规范

## Overview

本文档定义了数据迁移阶段的技术规范和执行标准。

## 迁移策略

| 策略 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| BIG_BANG | 简单 | 停机时间长 | 小数据量 |
| PARALLEL | 风险低 | 成本高 | 关键系统 |
| PHASE | 灵活 | 周期长 | 大数据量 |

## 数据校验方法

```sql
-- 记录数校验
SELECT COUNT(*) FROM source;
SELECT COUNT(*) FROM target;

-- 数据和校验
SELECT SUM(column) FROM source;
SELECT SUM(column) FROM target;

--抽样校验
SELECT * FROM source ORDER BY RAND() LIMIT 100;
SELECT * FROM target ORDER BY id LIMIT 100;
```

## Associated Assets

- **Scenario**: `scenarios/migrate-data/SCENARIO.md`
- **Prompt**: `prompts/migrate-data.prompt.md`
- **Agent**: `agents/data-migration-engineer.agent.md`
- **Skill**: `skills/migrate-data/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for migrate-data.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for migrate-data execution.

1. **Practice 1**: [Description]
2. **Practice 2**: [Description]
3. **Practice 3**: [Description]


## Error Handling

> Common error scenarios and resolution strategies for migrate-data.

### Error Category 1
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: [Description]
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for migrate-data deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | [Description] | [How to verify] |
| Standard 2 | [Description] | [How to verify] |
| Standard 3 | [Description] | [How to verify] |
