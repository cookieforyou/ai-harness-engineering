---
name: migrate-data
description: Detailed technical instructions for migrate-data scenario execution
type: instruction
version: "1.1.0"
stage: migrate-data
---

# Instruction: 数据迁移技术规范

## Overview

This instruction defines the technical standards and execution procedures for data migration projects within the E2E delivery lifecycle. It covers migration strategy selection (big-bang vs. incremental vs. synchronization), ETL pipeline design, data quality validation techniques, zero-downtime migration patterns, and rollback strategies. The instruction ensures data integrity is preserved throughout migration, downstream consumers are properly notified and validated, and business continuity is maintained. Key focus areas include consistency checks, reconciliation procedures, and performance optimization for large-scale data movements.


## Migration Strategy

| 策略 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| BIG_BANG | 简单 | 停机时间长 | 小数据量 |
| PARALLEL | 风险低 | 成本高 | 关键系统 |
| PHASE | 灵活 | 周期长 | 大数据量 |

## Data Validation Methods

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
- **Agent**: `agents/migrate-data.agent.md`
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

1. **Practice 1**: Plan migration with clear rollback strategy
2. **Practice 2**: Validate data integrity with checksums and row counts
3. **Practice 3**: Minimize downtime with incremental or online migration


## Error Handling

> Common error scenarios and resolution strategies for migrate-data.

### Error Category 1
**Symptom**: Data loss or corruption occurs during migration
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Migration downtime exceeds business tolerance
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for migrate-data deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Data integrity validation passes 100% | Automated check |
| Standard 2 | Downtime is within budget constraints | Automated check |
| Standard 3 | Rollback capability is maintained throughout migration | Automated check |
