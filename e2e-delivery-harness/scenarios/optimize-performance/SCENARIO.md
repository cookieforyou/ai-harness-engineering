---
name: optimize-performance
version: 1.1.0
stage: optimize-performance
description: Optimize Performance scenario for the E2E delivery lifecycle
author: AI Harness Engineering Team
type: scenario
---

# Scenario: 性能优化 (Optimize Performance)

## Overview

本场景用于识别和解决系统性能瓶颈，包括代码优化、数据库优化、缓存优化、网络优化等。

## Chain of Thought

```
[ANALYZE] 分析性能问题
├─ 确定性能指标基线
├─ 识别性能瓶颈
└─ 分析瓶颈原因

[MEASURE] 测量性能数据
├─ 性能分析工具
├─ 性能测试
└─ 监控数据

[OPTIMIZE] 实施优化
├─ 代码级优化
├─ 数据库优化
├─ 缓存优化
├─ 并发优化

[VERIFY] 验证优化效果
├─ 性能回归测试
├─ 压力测试
└─ 稳定性测试
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 瓶颈定位 | 哪个环节最慢？ |
| DC-002 | 优化方案选择 | 缓存/索引/重构？ |
| DC-003 | 优化优先级 | 哪个收益最大？ |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `IMPROVEMENT-GAIN` | ≥20% | 性能提升：优化后目标指标提升 |
| `REGRESSION-FREE` | 100% | 无回归：其他指标不劣化 |
| `COST-EFFICIENCY` | ≤100% | 成本效率：优化不增加资源成本 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 性能瓶颈已定位
- [x] 优化方案已实施
- [x] 性能指标已达标
- [x] 性能回归测试通过

## Associated Assets

- **Prompt**: `prompts/optimize-performance.prompt.md`
- **Instruction**: `instructions/optimize-performance.instructions.md`
- **Agent**: `agents/optimize-performance.agent.md`
- **Skill**: `skills/optimize-performance/SKILL.md`


## Purpose

> Define the objectives and scope of the optimize-performance scenario.
>
> This scenario ensures systematic execution of optimize-performance activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Performance baseline metrics are collected and documented
- [ ] Prerequisite 2: Target optimization goals and constraints are defined
- [ ] Prerequisite 3: Profiling tools and test environment are ready


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/optimize-performance/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/optimize-performance.prompt.md` | Execution prompt |
| Instructions | `instructions/optimize-performance.instructions.md` | Technical instructions |
| Agent | `agents/optimize-performance.agent.md` | Responsible agent |
| Skill | `skills/optimize-performance/SKILL.md` | Domain skill |


## Error Handling

### Error Scenario 1
**Error**: Optimization target is not clearly defined or measurable
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: Optimization causes regression in non-target performance metrics
**Handling**: [Resolution steps]
