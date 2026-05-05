---
name: migrate-environment
version: "1.1.0"
stage: "migrate-environment"
---

# Scenario: 环境迁移 (Migrate Environment)

## Overview

本场景用于将应用程序从一个环境迁移到另一个环境，包括开发、测试、预发布、生产环境之间的迁移。

## Chain of Thought

```
[ANALYZE] 分析迁移需求
├─ 确定源环境和目标环境
├─ 分析差异和依赖
└─ 评估迁移风险

[PLAN] 制定迁移计划
├─ 数据迁移策略
├─ 配置迁移策略
├─ 回滚方案

[PREPARE] 准备迁移
├─ 备份数据
├─ 准备配置文件
├─ 验证目标环境

[MIGRATE] 执行迁移
├─ 数据迁移
├─ 配置迁移
├─ 服务部署

[VERIFY] 验证迁移
├─ 功能验证
├─ 数据验证
├─ 监控验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 迁移方案 | 全量迁移还是增量迁移？ |
| DC-002 | 数据同步 | 在线迁移还是停机迁移？ |
| DC-003 | 回滚方案 | 是否需要保留回滚能力？ |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `MIGRATION-SUCCESS` | ≥98% | 迁移成功率：应用功能无损迁移 |
| `PERF-PARITY` | ≥95% | 性能对等：新环境性能≥原环境95% |
| `COST-EFFICIENCY` | ≤110% | 成本效率：新环境成本≤原环境110% |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 迁移计划已评审
- [x] 数据已备份
- [x] 迁移已执行
- [x] 验证已通过

## Associated Assets

- **Prompt**: `prompts/migrate-environment.prompt.md`
- **Instruction**: `instructions/migrate-environment.instructions.md`
- **Agent**: `agents/migrate-environment.agent.md`
- **Skill**: `skills/migrate-environment/SKILL.md`


## Purpose

> Define the objectives and scope of the migrate-environment scenario.
>
> This scenario ensures systematic execution of migrate-environment activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/migrate-environment/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/migrate-environment.prompt.md` | Execution prompt |
| Instructions | `instructions/migrate-environment.instructions.md` | Technical instructions |
| Agent | `agents/migrate-environment.agent.md` | Responsible agent |
| Skill | `skills/migrate-environment/SKILL.md` | Domain skill |


## Error Handling

### Error Scenario 1
**Error**: [Description]
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: [Description]
**Handling**: [Resolution steps]
