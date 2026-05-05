---
name: design-database
version: "1.1.0"
stage: "design-database"
---

# Scenario: 数据库设计 (Design Database)

## Overview

本场景用于设计数据库架构，包括概念模型、逻辑模型、物理模型，以及表结构设计、索引设计、分库分表策略等。

## Chain of Thought

```
[THINK] 分析业务需求
├─ 理解业务实体和关系
├─ 分析数据访问模式
└─ 评估数据量和增长趋势

[ANALYZE] 设计概念模型
├─ 识别核心业务实体
├─ 定义实体属性
├─ 建立实体间关系

[DESIGN] 设计逻辑模型
├─ 将概念模型转换为逻辑模型
├─ 定义表结构和字段
├─ 确定主键和外键

[DESIGN] 设计物理模型
├─ 选择数据库类型
├─ 设计索引策略
├─ 规划分区策略

[OPTIMIZE] 优化设计方案
├─ 分析查询性能
├─ 优化表结构
├─ 完善约束和触发器
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 数据库类型选择 | OLTP/OLAP/NoSQL？ |
| DC-002 | 分库分表策略 | 是否需要分库分表？ |
| DC-003 | 索引策略 | 索引覆盖还是回表？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 数据不一致 | 引入事务约束 |
| 查询性能差 | 优化索引和 SQL |
| 表结构冲突 | 评审和协调 |
| 容量预估不足 | 扩容或归档策略 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `NORMALIZATION` | 3NF | 规范化程度：达到第三范式 |
| `INDEX-COVERAGE` | ≥90% | 查询索引覆盖率：高频查询有索引 |
| `SCHEMA-DOCS` | 100% | Schema文档化率：所有表和字段有注释 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] ER 图已完成
- [x] 表结构设计已评审
- [x] 索引设计已优化
- [x] DDL 脚本已准备
- [x] 数据字典已编写

## Associated Assets

- **Prompt**: `prompts/design-database.prompt.md`
- **Instruction**: `instructions/design-database.instructions.md`
- **Agent**: `agents/design-database.agent.md`
- **Skill**: `skills/design-database/SKILL.md`


## Purpose

> Define the objectives and scope of the design-database scenario.
>
> This scenario ensures systematic execution of design-database activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/design-database/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/design-database.prompt.md` | Execution prompt |
| Instructions | `instructions/design-database.instructions.md` | Technical instructions |
| Agent | `agents/design-database.agent.md` | Responsible agent |
| Skill | `skills/design-database/SKILL.md` | Domain skill |
