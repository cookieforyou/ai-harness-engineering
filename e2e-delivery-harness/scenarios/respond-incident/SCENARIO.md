---
name: respond-incident
description: 事件响应场景，定义生产环境事故的发现、响应、处理和恢复流程
type: scenario
version: "1.1.0"
trigger: 当发生生产环境事故时触发
agent: integrate-monitor
phase: monitor-operate
tags: 
input: 
output: 
---

# Incident Response Scenario

## Overview

事件响应是保障服务稳定性的关键能力，涵盖从发现问题到恢复服务的完整流程。本场景定义事件的分级、响应流程、处理步骤和复盘改进机制。

## Severity Levels

### P0 - Critical

| Aspect | Definition |
|--------|------------|
| 影响 | 核心服务完全不可用，影响所有用户 |
| SLA | 响应时间: 5 分钟，恢复时间: 1 小时 |
| 人员 | 全员响应，管理层介入 |
| 沟通 | 每 15 分钟状态更新 |

### P1 - High

| Aspect | Definition |
|--------|------------|
| 影响 | 核心功能受损，影响大部分用户 |
| SLA | 响应时间: 15 分钟，恢复时间: 4 小时 |
| 人员 | On-call + 值班经理 |
| 沟通 | 每 30 分钟状态更新 |

### P2 - Medium

| Aspect | Definition |
|--------|------------|
| 影响 | 非核心功能异常，影响部分用户 |
| SLA | 响应时间: 1 小时，恢复时间: 8 小时 |
| 人员 | On-call 工程师 |
| 沟通 | 每 2 小时状态更新 |

### P3 - Low

| Aspect | Definition |
|--------|------------|
| 影响 | 功能降级或小范围问题 |
| SLA | 响应时间: 4 小时，恢复时间: 24 小时 |
| 人员 | 工作时间处理 |
| 沟通 | 每日状态更新 |

## Chain of Thought

```
1. 检测与确认
   ↓
2. 评估与定级
   ↓
3. 组建响应团队
   ↓
4. 沟通启动
   ↓
5. 诊断分析
   ↓
6. 制定解决方案
   ↓
7. 执行修复
   ↓
8. 验证恢复
   ↓
9. 事后复盘
   ↓
10. 预防改进
```

## Decision Checkpoints

### Checkpoint 1: 事件确认
- 是否真的是事故？
- 影响范围和时间？
- 是否有用户投诉？

### Checkpoint 2: 严重程度定级
- 符合哪个 P0/P1/P2/P3？
- 是否需要升级？
- 响应团队规模？

### Checkpoint 3: 解决方案选择
- 临时修复还是根本解决？
- 回滚还是热修复？
- 灰度发布还是全量？

### Checkpoint 4: 恢复验证
- 服务是否稳定？
- 功能是否正常？
- 监控是否正常？

## Error Handling

| Error Scenario | Handling Strategy |
|----------------|-------------------|
| 诊断困难 | 请求更多资源，多角度分析 |
| 修复失败 | 回滚到上一版本，重复修复 |
| 影响扩大 | 立即升级，启动应急响应 |
| 数据损坏 | 启动数据恢复流程 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `MTTR` | ≤1h | 恢复时间目标 |
| `ESCALATION-ACCURACY` | ≥90% | 升级准确性：正确触发升级的比例 |
| `COMM-TIMELINESS` | ≤15min | 沟通及时性：首次沟通时间 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [ ] 事件已恢复
- [ ] 影响已评估
- [ ] 根本原因已识别
- [ ] 修复已验证
- [ ] 监控已加强
- [ ] 复盘已完成

## Expected Artifacts

| Artifact | Description |
|----------|-------------|
| incident-timeline.md | 事件时间线 |
| resolution-steps.md | 解决步骤 |
| impact-report.md | 影响评估报告 |
| follow-up-actions.md | 后续行动项 |

## Related Scenarios

- [monitor-operate](./monitor-operate/SCENARIO.md) - 监控运维
- [review-incident](./review-incident/SCENARIO.md) - 事件复盘
- [plan-rollback](./plan-rollback/SCENARIO.md) - 回滚计划
- [plan-disaster-recovery](./plan-disaster-recovery/SCENARIO.md) - 灾备恢复


## Purpose

> Define the objectives and scope of the respond-incident scenario.
>
> This scenario ensures systematic execution of respond-incident activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/respond-incident/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/respond-incident.prompt.md` | Execution prompt |
| Instructions | `instructions/respond-incident.instructions.md` | Technical instructions |
| Agent | `agents/respond-incident.agent.md` | Responsible agent |
| Skill | `skills/respond-incident/SKILL.md` | Domain skill |
