---
name: migrate-environment
description: "Detailed technical instructions for migrate-environment scenario execution"
applyTo: "scenarios/migrate-environment/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 环境迁移 (Migrate Environment)

## Migration Type Standards

### 迁移类型对比

| 类型 | 特点 | 停机时间 | 适用场景 |
|------|------|----------|----------|
| 全量迁移 | 一次性迁移 | 长 | 小数据量 |
| 增量迁移 | 分批次迁移 | 短 | 大数据量 |
| 蓝绿部署 | 双环境切换 | 极短 | 生产环境 |
| 滚动迁移 | 逐步迁移 | 无 | 高可用要求 |

## Data Migration Standards

### 数据迁移策略

```yaml
migration_strategy:
  small_data:
    size: "< 1GB"
    method: "mysqldump/pg_dump"
    downtime: "< 1 hour"

  medium_data:
    size: "1GB - 100GB"
    method: "增量备份 + 同步"
    downtime: "< 30 minutes"

  large_data:
    size: "> 100GB"
    method: "CDC + 增量同步"
    downtime: "接近零"
```

## Rollback Standards

### 回滚策略

```yaml
rollback:
  enabled: true
  trigger:
    - "功能验证失败"
    - "数据不一致"
    - "性能严重下降"

  steps:
    - "停止新环境"
    - "恢复数据"
    - "切换流量"
    - "验证旧环境"

  verification:
    - "健康检查"
    - "功能测试"
    - "数据验证"
```


## Overview

> High-level description of the migrate-environment execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the migrate-environment scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for migrate-environment.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for migrate-environment execution.

1. **Practice 1**: Map source-to-target environment configurations
2. **Practice 2**: Validate application functionality post-migration
3. **Practice 3**: Plan cutover with minimal service disruption


## Error Handling

> Common error scenarios and resolution strategies for migrate-environment.

### Error Category 1
**Symptom**: Applications fail after environment migration
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Performance degrades in the new environment
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for migrate-environment deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Migration success rate is 98% or higher | Automated check |
| Standard 2 | New environment performance is 95%+ of original | Automated check |
| Standard 3 | Environment cost is within 110% of original budget | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
