---
name: setup-infra
version: "1.1.0"
stage: "setup-infra"
---

# Scenario: 基础设施搭建 (Setup Infrastructure)

## Overview

本场景用于搭建项目基础设施，包括云资源、网络、安全组、存储等。

## Chain of Thought

```
[THINK] 理解基础设施需求
├─ 分析业务负载类型
├─ 确定性能和安全要求
└─ 评估成本约束

[ANALYZE] 设计基础设施架构
├─ 选择云服务商和区域
├─ 设计网络拓扑
├─ 规划资源规格

[DESIGN] 规划资源清单
├─ 计算实例规格
├─ 设计存储方案
├─ 配置安全策略

[IMPLEMENT] 实施基础设施
├─ 创建网络资源
├─ 部署计算资源
├─ 配置存储资源

[VERIFY] 验证部署
├─ 资源连通性测试
├─ 性能基准测试
└─ 安全合规检查
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 云服务商选型 | 选择哪个云平台？ |
| DC-002 | 网络架构设计 | VPC CIDR 如何划分？ |
| DC-003 | 资源规格确认 | 实例类型是否合适？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 配额不足 | 申请配额或优化资源 |
| 网络冲突 | 调整 CIDR 范围 |
| 权限不足 | 申请 IAM 权限 |
| 资源创建失败 | 检查参数或重试 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `IAC-COVERAGE` | ≥95% | IaC覆盖率：基础设施即代码管理比例 |
| `DEPLOY-TIME` | ≤30min | 部署时间：新环境就绪时间 |
| `SEC-BASELINE` | 100% | 安全基线达标率 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 所有资源创建成功
- [x] 网络连通性验证通过
- [x] 安全组规则配置正确
- [x] 监控告警已配置
- [x] 运维文档已编写

## Associated Assets

- **Prompt**: `prompts/setup-infra.prompt.md`
- **Instruction**: `instructions/setup-infra.instructions.md`
- **Agent**: `agents/setup-infra.agent.md`
- **Skill**: `skills/setup-infra/SKILL.md`


## Purpose

> Define the objectives and scope of the setup-infra scenario.
>
> This scenario ensures systematic execution of setup-infra activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/setup-infra/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/setup-infra.prompt.md` | Execution prompt |
| Instructions | `instructions/setup-infra.instructions.md` | Technical instructions |
| Agent | `agents/setup-infra.agent.md` | Responsible agent |
| Skill | `skills/setup-infra/SKILL.md` | Domain skill |
