---
name: prepare-release
version: "1.1.0"
stage: "prepare-release"
---

# Scenario: 发布准备 (Prepare Release)

## Overview

本场景用于准备版本发布，包括发布计划、变更评审、风险评估、回滚方案等。

## Chain of Thought

```
[THINK] 分析发布需求
├─ 确定发布范围和版本
├─ 识别关联系统和依赖
└─ 评估发布时间窗口

[ANALYZE] 制定发布计划
├─ 确定发布时间表
├─ 分配发布任务
└─ 准备回滚方案

[DESIGN] 设计发布流程
├─ 设计发布步骤
├─ 确定验证检查点
└─ 配置监控指标

[PREPARE] 准备发布资源
├─ 准备发布包/镜像
├─ 准备数据库变更
├─ 准备配置文件
├─ 通知相关方

[VERIFY] 验证发布就绪
├─ 验证环境和资源
├─ 验证回滚方案
└─ 确认沟通计划
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 发布评审 | 是否通过发布评审？ |
| DC-002 | 回滚方案 | 回滚方案是否就绪？ |
| DC-003 | 发布时间 | 确认发布时间窗口？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 发布包不完整 | 重新打包并验证 |
| 依赖未就绪 | 延迟发布时间 |
| 回滚失败 | 紧急故障响应 |
| 验证不通过 | 修复后重新验证 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `CHECKLIST-COMPLETE` | 100% | 检查清单完成率：发布前所有检查通过 |
| `DOC-ACCURACY` | ≥98% | 文档准确性：发布说明与实际变更一致 |
| `APPROVAL-COMPLY` | 100% | 审批合规率：所有必需审批已完成 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 发布计划已审批
- [x] 发布包已验证
- [x] 回滚方案已测试
- [x] 监控告警已配置
- [x] 沟通计划已通知

## Associated Assets

- **Prompt**: `prompts/prepare-release.prompt.md`
- **Instruction**: `instructions/prepare-release.instructions.md`
- **Agent**: `agents/prepare-release.agent.md`
- **Skill**: `skills/prepare-release/SKILL.md`


## Purpose

> Define the objectives and scope of the prepare-release scenario.
>
> This scenario ensures systematic execution of prepare-release activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/prepare-release/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/prepare-release.prompt.md` | Execution prompt |
| Instructions | `instructions/prepare-release.instructions.md` | Technical instructions |
| Agent | `agents/prepare-release.agent.md` | Responsible agent |
| Skill | `skills/prepare-release/SKILL.md` | Domain skill |
