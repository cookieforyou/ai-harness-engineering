---
name: design-architecture
version: "1.1.0"
stage: "design-architecture"
---

# Scenario: 架构设计 (Design Architecture)

## 概述

本场景用于设计系统高层架构，包括微服务拆分、技术选型、系统拓扑、数据架构等。

## Chain of Thought

```
[THINK] 理解业务需求
├─ 分析业务用例和用户故事
├─ 确定核心功能域
└─ 评估业务优先级

[ANALYZE] 分析技术需求
├─ 性能要求（QPS、延迟）
├─ 可用性要求（SLA）
├─ 可扩展性要求

[DESIGN] 设计系统架构
├─ 微服务拆分策略
├─ 技术栈选型
├─ 系统拓扑设计

[EVALUATE] 评估备选方案
├─ 技术可行性分析
├─ 成本效益分析
├─ 风险评估

[DOCUMENT] 输出架构文档
├─ 架构图和说明
├─ 接口设计
├─ 部署架构
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 服务拆分粒度 | 微服务 vs 模块化单体？ |
| DC-002 | 技术栈选型 | 选择哪些技术？ |
| DC-003 | 数据架构 | 集中式 vs 分布式？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 服务边界不清晰 | 重构服务边界 |
| 技术选型不合理 | 重新评估和调整 |
| 性能不达标 | 优化架构设计 |
| 成本超预算 | 调整方案 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `QAS-COVERAGE` | ≥90% | 质量属性场景覆盖率 |
| `DECISION-RATIONALE` | 100% | 决策依据完整率：每个ADR都有 rationale |
| `STAKEHOLDER-ALIGN` | ≥85% | 干系人一致性：评审共识度 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 架构设计文档已完成
- [x] 架构评审已通过
- [x] 接口契约已定义
- [x] 部署架构已规划
- [x] 技术风险已识别

## Associated Assets

- **Prompt**: `prompts/design-architecture.prompt.md`
- **Instruction**: `instructions/design-architecture.instructions.md`
- **Agent**: `agents/design-architecture.agent.md`
- **Skill**: `skills/design-architecture/SKILL.md`


## Purpose

> Define the objectives and scope of the design-architecture scenario.
>
> This scenario ensures systematic execution of design-architecture activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/design-architecture/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/design-architecture.prompt.md` | Execution prompt |
| Instructions | `instructions/design-architecture.instructions.md` | Technical instructions |
| Agent | `agents/design-architecture.agent.md` | Responsible agent |
| Skill | `skills/design-architecture/SKILL.md` | Domain skill |
