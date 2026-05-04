---
name: manage-config
version: "1.1.0"
stage: "manage-config"
---

# Scenario: 配置管理 (Manage Configuration)

## 概述

本场景用于管理应用程序配置、环境变量、特性开关等。

## Chain of Thought

```
[THINK] 分析配置需求
├─ 识别配置类型（运行时/构建时/特性开关）
├─ 确定配置来源（代码/环境变量/配置中心）
└─ 评估敏感配置处理方式

[ANALYZE] 设计配置结构
├─ 设计配置分层（全局/环境/本地）
├─ 规划配置存储方式
└─ 设计配置变更流程

[DESIGN] 实现配置管理
├─ 选择配置管理方案
├─ 实现配置加载逻辑
└─ 配置加密和访问控制

[IMPLEMENT] 部署配置管理
├─ 搭建配置中心（Consul/Apollo/Nacos）
├─ 迁移现有配置
└─ 配置监控和审计

[VERIFY] 验证配置生效
├─ 配置推送验证
├─ 配置回滚测试
└─ 敏感信息验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 配置方案选型 | 使用配置中心还是文件？ |
| DC-002 | 敏感配置处理 | 如何加密存储？ |
| DC-003 | 配置变更策略 | 实时生效还是重启生效？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 配置获取失败 | 使用本地缓存/默认值 |
| 配置格式错误 | 回退到默认配置 |
| 配置服务不可用 | 降级到文件配置 |
| 敏感配置泄露 | 立即轮换密钥 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `CONFIG-VALID` | 100% | 配置验证通过率 |
| `ENV-PARITY` | ≥95% | 环境一致性：配置项在各环境对齐率 |
| `SECRETS-ISOLATION` | 100% | 密钥隔离率：无硬编码密钥 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 配置中心部署完成
- [x] 所有配置已迁移
- [x] 访问控制已配置
- [x] 监控告警已设置
- [x] 运维文档已编写

## Associated Assets

- **Prompt**: `prompts/manage-config.prompt.md`
- **Instruction**: `instructions/manage-config.instructions.md`
- **Agent**: `agents/manage-config.agent.md`
- **Skill**: `skills/manage-config/SKILL.md`


## Purpose

> Define the objectives and scope of the manage-config scenario.
>
> This scenario ensures systematic execution of manage-config activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/manage-config/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/manage-config.prompt.md` | Execution prompt |
| Instructions | `instructions/manage-config.instructions.md` | Technical instructions |
| Agent | `agents/manage-config.agent.md` | Responsible agent |
| Skill | `skills/manage-config/SKILL.md` | Domain skill |
