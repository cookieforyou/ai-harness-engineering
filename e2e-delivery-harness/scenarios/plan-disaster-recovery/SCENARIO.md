---
name: plan-disaster-recovery
description: 灾备恢复场景，规划和实施灾难恢复策略，确保业务连续性
type: scenario
version: "1.1.0"
trigger: 当需要进行灾备规划或演练时触发
agent: design-architecture
phase: monitor-operate
tags: 
input: 
output: 
---

# Disaster Recovery Planning Scenario

## Overview

灾备恢复规划是确保业务连续性的关键，涵盖对灾难场景的预防、准备、响应和恢复能力建设。本场景定义 RPO/RTO 目标、恢复策略和演练机制。

## Key Metrics

### Recovery Point Objective (RPO)
- 定义：最大可接受的数据丢失时间窗口
- 计算：备份频率决定 RPO
- 示例：每 4 小时备份 → RPO = 4 小时

### Recovery Time Objective (RTO)
- 定义：最大可接受的系统恢复时间
- 计算：恢复步骤决定 RTO
- 示例：多可用区部署 → RTO = 15 分钟

## Disaster Categories

### Tier 1: Data Center Failure
| Aspect | Description |
|--------|-------------|
| 影响 | 单个数据中心不可用 |
| RTO | 15-60 分钟 |
| 策略 | 多可用区部署，自动 failover |

### Tier 2: Region Failure
| Aspect | Description |
|--------|-------------|
| 影响 | 整个区域不可用 |
| RTO | 1-4 小时 |
| 策略 | 跨区域备份，手动切换 |

### Tier 3: Cyber Attack
| Aspect | Description |
|--------|-------------|
| 影响 | 数据泄露或勒索软件 |
| RTO | 4-24 小时 |
| 策略 | 隔离，恢复备份 |

## Chain of Thought

```
1. 业务影响分析
   ↓
2. 确定 RPO/RTO
   ↓
3. 设计恢复策略
   ↓
4. 规划备份方案
   ↓
5. 设计故障转移
   ↓
6. 准备恢复流程
   ↓
7. 制定演练计划
   ↓
8. 执行演练验证
   ↓
9. 持续优化改进
```

## Decision Checkpoints

### Checkpoint 1: 需求分析
- 业务关键程度？
- 可接受的停机时间？
- 可接受的数据丢失？
- 合规要求？

### Checkpoint 2: 策略选择
- 采用什么备份策略？
- 使用什么恢复架构？
- 如何验证恢复能力？

### Checkpoint 3: 资源规划
- 需要多少备用资源？
- 成本预算？
- 人员配置？

### Checkpoint 4: 演练验证
- 多久演练一次？
- 如何衡量成功？
- 如何改进？


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `RTO-COMPLY` | 100% | RTO达成：恢复时间≤目标 |
| `RPO-COMPLY` | 100% | RPO达成：数据丢失≤目标 |
| `DR-TEST-FREQ` | ≥1/year | DR演练频率：每年至少一次全量演练 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [ ] DR 计划文档完整
- [ ] RPO/RTO 已定义
- [ ] 备份方案已实施
- [ ] 故障转移已配置
- [ ] 恢复流程已测试
- [ ] 演练已执行

## Related Scenarios

- [respond-incident](./respond-incident/SCENARIO.md) - 事件响应
- [plan-rollback](./plan-rollback/SCENARIO.md) - 回滚计划
- [backup-data](./backup-data/SCENARIO.md) - 数据备份
- [monitor-operate](./monitor-operate/SCENARIO.md) - 监控运维


## Purpose

> Define the objectives and scope of the plan-disaster-recovery scenario.
>
> This scenario ensures systematic execution of plan-disaster-recovery activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Business impact analysis (BIA) is completed with RTO/RPO
- [ ] Prerequisite 2: Infrastructure inventory and dependencies are documented
- [ ] Prerequisite 3: Threat scenarios and risk appetite are defined


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/plan-disaster-recovery/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/plan-disaster-recovery.prompt.md` | Execution prompt |
| Instructions | `instructions/plan-disaster-recovery.instructions.md` | Technical instructions |
| Agent | `agents/plan-disaster-recovery.agent.md` | Responsible agent |
| Skill | `skills/plan-disaster-recovery/SKILL.md` | Domain skill |


## Error Handling

### Error Scenario 1
**Error**: DR plan does not meet recovery time objective (RTO) targets
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: DR procedures have not been tested or are outdated
**Handling**: [Resolution steps]
