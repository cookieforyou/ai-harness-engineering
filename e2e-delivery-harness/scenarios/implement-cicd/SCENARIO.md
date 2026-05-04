---
name: implement-cicd
version: "1.1.0"
stage: "implement-cicd"
---

# Scenario: CI/CD 实施 (Implement CI/CD)

## 概述

本场景用于设计并实施持续集成/持续部署流水线，包括构建、测试、部署全流程自动化。

## Chain of Thought

```
[THINK] 分析 CI/CD 需求
├─ 了解项目技术栈
├─ 确定部署环境
└─ 评估发布频率

[ANALYZE] 设计流水线架构
├─ 设计构建流程
├─ 设计测试阶段
├─ 设计部署策略

[DESIGN] 设计流水线
├─ 设计触发机制
├─ 设计审批流程
├─ 设计回滚机制

[IMPLEMENT] 实现流水线
├─ 配置构建任务
├─ 配置测试任务
├─ 配置部署任务

[VERIFY] 验证流水线
├─ 端到端测试
├─ 性能验证
└─ 安全扫描
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | CI/CD 工具选型 | GitHub Actions/GitLab CI/Jenkins？ |
| DC-002 | 部署策略 | 蓝绿/金丝雀/滚动更新？ |
| DC-003 | 环境配置 | 如何管理环境变量？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 构建失败 | 发送通知、阻止部署 |
| 测试失败 | 阻止合并、发送通知 |
| 部署失败 | 自动回滚、发送通知 |
| 超时 | 重试或人工介入 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `LEAD-TIME` | ≤1d | 交付前置时间：代码提交到生产部署 |
| `DEPLOY-FREQ` | ≥1/day | 部署频率：每日部署次数 |
| `MTTR` | ≤1h | 恢复时间：故障到恢复平均时间 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 流水线配置完成
- [x] 所有环境可用
- [x] 回滚机制已验证
- [x] 监控告警已配置
- [x] 文档已编写

## Associated Assets

- **Prompt**: `prompts/implement-cicd.prompt.md`
- **Instruction**: `instructions/implement-cicd.instructions.md`
- **Agent**: `agents/implement-cicd.agent.md`
- **Skill**: `skills/implement-cicd/SKILL.md`


## Purpose

> Define the objectives and scope of the implement-cicd scenario.
>
> This scenario ensures systematic execution of implement-cicd activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/implement-cicd/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/implement-cicd.prompt.md` | Execution prompt |
| Instructions | `instructions/implement-cicd.instructions.md` | Technical instructions |
| Agent | `agents/implement-cicd.agent.md` | Responsible agent |
| Skill | `skills/implement-cicd/SKILL.md` | Domain skill |
