---
name: plan-rollback
description: 回滚计划场景，为部署发布制定详细的回滚策略和执行方案
type: scenario
version: "1.1.0"
trigger: 当需要进行部署发布前触发
agent: release-manager
phase: deploy-release
tags: 
input: 
output: 
---

# Rollback Planning Scenario

## Overview

回滚计划是部署发布流程的关键组成部分，确保在部署出现问题时能够快速、安全地恢复到稳定状态。本场景涵盖回滚策略制定、脚本准备和验证流程。

## Trigger Conditions

- 任何生产环境部署前
- 重大版本升级
- 架构变更部署
- 配置变更部署
- 紧急热修复部署

## Chain of Thought

```
1. 评估变更风险
   ↓
2. 确定回滚策略
   ↓
3. 设计回滚路径
   ↓
4. 准备回滚脚本
   ↓
5. 定义触发条件
   ↓
6. 制定验证清单
   ↓
7. 安排回滚演练
   ↓
8. 沟通协调准备
```

## Rollback Strategies

### Strategy 1: Blue-Green Deployment

| Aspect | Description |
|--------|-------------|
| 原理 | 维护两套环境，一套备用 |
| 回滚方式 | 切换流量到原环境 |
| 回滚时间 | 分钟级 |
| 成本 | 高（双倍资源） |

### Strategy 2: Canary Deployment

| Aspect | Description |
|--------|-------------|
| 原理 | 逐步放量，发现问题立即停止 |
| 回滚方式 | 停止放量，部分流量回滚 |
| 回滚时间 | 分钟级 |
| 成本 | 中等 |

### Strategy 3: Feature Toggle

| Aspect | Description |
|--------|-------------|
| 原理 | 通过开关控制功能 |
| 回滚方式 | 关闭功能开关 |
| 回滚时间 | 秒级 |
| 成本 | 低 |

### Strategy 4: Database Migration Rollback

| Aspect | Description |
|--------|-------------|
| 原理 | 使用可逆的数据库变更 |
| 回滚方式 | 执行逆向迁移 |
| 回滚时间 | 分钟级到小时级 |
| 成本 | 中等 |

## Decision Checkpoints

### Checkpoint 1: 风险评估
- 变更的影响范围？
- 回滚的复杂度？
- 回滚窗口期？
- 数据一致性要求？

### Checkpoint 2: 策略选择
- 哪种回滚策略最合适？
- 是否需要组合策略？
- 回滚触发条件？

### Checkpoint 3: 准备就绪
- 回滚脚本已验证？
- 回滚权限已配置？
- 回滚人员已就绪？
- 沟通渠道已建立？

### Checkpoint 4: 执行验证
- 回滚后服务正常？
- 数据完整性？
- 监控告警正常？
- 业务功能正常？

## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 回滚失败 | 立即升级到 P0 事故，启动应急响应 |
| 部分回滚 | 评估状态，决定是否完全回滚 |
| 数据损坏 | 启动数据恢复流程 |
| 回滚超时 | 强制停止，分析原因 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `ROLLBACK-TESTED` | 100% | 回滚方案测试率：所有场景已演练 |
| `RECOVERY-RTO` | ≤15min | 恢复时间目标：回滚到稳定状态 |
| `DATA-CONSISTENCY` | 100% | 数据一致性：回滚后数据完整性 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [ ] 回滚策略已评审
- [ ] 回滚脚本已测试
- [ ] 触发条件已定义
- [ ] 验证清单已准备
- [ ] 回滚权限已配置
- [ ] 沟通计划已制定

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| rollback-plan.md | 完整回滚计划 |
| rollback-scripts.md | 回滚脚本和命令 |
| verification-checklist.md | 回滚后验证清单 |
| communication-plan.md | 回滚沟通计划 |

## Related Scenarios

- [deploy-release](./deploy-release/SCENARIO.md) - 部署发布
- [prepare-release](./prepare-release/SCENARIO.md) - 发布准备
- [review-incident](./review-incident/SCENARIO.md) - 事件复盘
- [plan-disaster-recovery](./plan-disaster-recovery/SCENARIO.md) - 灾备恢复


## Purpose

> Define the objectives and scope of the plan-rollback scenario.
>
> This scenario ensures systematic execution of plan-rollback activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/plan-rollback/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/plan-rollback.prompt.md` | Execution prompt |
| Instructions | `instructions/plan-rollback.instructions.md` | Technical instructions |
| Agent | `agents/plan-rollback.agent.md` | Responsible agent |
| Skill | `skills/plan-rollback/SKILL.md` | Domain skill |
