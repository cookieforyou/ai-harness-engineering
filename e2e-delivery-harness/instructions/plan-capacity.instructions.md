# Instruction: 容量规划技术规范

## 概述

本文档定义了容量规划的技术规范和方法。

## 容量评估方法

### 指标采集
- CPU 利用率
- 内存利用率
- 存储利用率
- 网络带宽
- TPS/QPS

### 扩容策略

| 策略 | 适用场景 | 成本 |
|------|----------|------|
| 垂直扩展 | 小规模 | 中 |
| 水平扩展 | 大规模 | 中高 |
| 混合扩展 | 复杂系统 | 高 |

## 关联资产

- **Scenario**: `scenarios/plan-capacity/SCENARIO.md`
- **Prompt**: `prompts/plan-capacity.prompt.md`
- **Agent**: `agents/capacity-planner.agent.md`
- **Skill**: `skills/plan-capacity/SKILL.md`
