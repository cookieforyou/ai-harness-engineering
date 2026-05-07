---
name: monitor-operate
description: 监控运维场景，负责系统上线后的监控、告警和运维支持
type: scenario
category: operations
stage: monitoring
version: 1.1.0
author: AI Harness Engineering Team
---

# Monitor Operate

## Purpose

监控系统运行状态，处理告警和故障，确保系统稳定运行和SLO达成。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成监控运维工作

### Think-Aloud Protocol

```
[THINK] 了解系统基线和SLO
   ↓
[SETUP] 配置监控和告警
   ↓
[WATCH] 监控系统状态
   ↓
[RESPOND] 响应告警和事件
   ↓
[IMPROVE] 优化监控体系
   ↓
[REPORT] 产出运维报告
```

### Step-by-Step Reasoning

**Step 1: 系统理解**
- 问：系统的基线和SLO是什么？
- 验证：与业务确认指标
- 检查：识别核心监控点

**Step 2: 监控配置**
- 问：需要监控哪些指标？
- 验证：覆盖核心路径
- 检查：告警阈值合理

**Step 3: 状态监控**
- 问：系统当前状态如何？
- 验证：指标在正常范围
- 检查：无异常告警

**Step 4: 告警响应**
- 问：告警是否需要处理？
- 验证：判断告警级别
- 检查：按流程响应

**Step 5: 问题诊断**
- 问：问题的根本原因是什么？
- 验证：定位问题根因
- 检查：彻底解决问题

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 监控覆盖 | 核心指标是否全覆盖？ |
| DC-002 | 告警配置 | 告警阈值是否合理？ |
| DC-003 | 响应及时性 | 告警是否及时处理？ |
| DC-004 | 问题解决 | 问题是否彻底解决？ |

## Error Handling

### 告警风暴

| 属性 | 值 |
|------|-----|
| **识别信号** | 大量告警同时触发 |
| **处理方式** | 1. 识别根本告警；2. 抑制次要告警；3. 优先处理核心问题；4. 优化告警规则 |
| **升级条件** | 影响核心服务 |

### 告警误报

| 属性 | 值 |
|------|-----|
| **识别信号** | 告警触发但无实际问题 |
| **处理方式** | 1. 验证告警真伪；2. 调整告警阈值；3. 优化告警条件；4. 减少误报 |
| **升级条件** | 误报率超过20% |

### 服务降级

| 属性 | 值 |
|------|-----|
| **识别信号** | 系统性能下降但未宕机 |
| **处理方式** | 1. 评估影响范围；2. 触发降级预案；3. 通知相关方；4. 持续监控 |
| **升级条件** | SLO 面临违约风险 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `MTTD` | ≤5min | 平均检测时间：异常发生到告警触发 |
| `ALERT-NOISE` | ≤20% | 告警噪声率：无效告警占比 |
| `SLO-COMPLY` | ≥99.5% | SLO合规率：服务水平目标达成 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 监控系统已配置
✅ 告警规则已设置
✅ 运维手册已编写
✅ 应急预案已准备
✅ SLO 监控面板已就绪
```

### 交付物清单

1. **监控配置**：监控指标和阈值
2. **告警规则**：告警定义和响应
3. **运维手册**：日常运维指南
4. **应急预案**：故障处理流程

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/monitor-operate.agent.md` | 监控运维角色 |
| **Prompt** | `../../prompts/monitor-operate.prompt.md` | 监控运维提示词 |
| **Instruction** | `../../instructions/monitor-operate.instructions.md` | 监控运维技术指令 |
| **Skill** | `../../skills/monitor-operate/SKILL.md` | 监控运维技能 |

## Prerequisites

### 必需前置条件

1. 系统已部署上线
2. 具备监控工具
3. 明确 SLO 指标

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `system_info` | 是 | 系统信息 |
| `slo_targets` | 是 | SLO 目标 |
| `monitoring_tools` | 是 | 监控工具 |
