---
name: plan-capacity
version: "1.1.0"
stage: "plan-capacity"
---

# Plan Capacity Scenario (容量规划场景)

## Purpose

本场景用于指导 AI Agent 执行容量规划工作，评估系统当前容量、预测未来需求、制定扩容计划。

## Chain of Thought (思维链)

### Think-Aloud Protocol

```
THINK: 分析当前容量使用
   ↓
THINK: 预测未来业务增长
   ↓
THINK: 评估容量差距
   ↓
THINK: 制定扩容方案
   ↓
VALIDATE: 验证方案可行性
   ↓
OUTPUT: 输出容量规划报告
```

## Primary Assets

- **Agent**: [../../agents/plan-capacity.agent.md](../../agents/plan-capacity.agent.md)
- **Instruction**: [../../instructions/plan-capacity.instructions.md](../../instructions/plan-capacity.instructions.md)
- **Prompt**: [../../prompts/plan-capacity.prompt.md](../../prompts/plan-capacity.prompt.md)
- **Skill**: [../../skills/plan-capacity/SKILL.md](../../skills/plan-capacity/SKILL.md)

## Error Handling (错误处理)

### EH-1: 数据不足

- **识别信号**：历史数据不足
- **处理方式**：
  1. 收集更多数据
  2. 使用行业基准
  3. 标注为估算
- **升级条件**：数据严重不足

### EH-2: 预测偏差大

- **识别信号**：预测与实际差异大
- **处理方式**：
  1. 调整预测模型
  2. 增加安全系数
  3. 缩短规划周期
- **升级条件**：预测误差 > 50%

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 预测模型确认** | 完成需求预测后 | 预测模型是否合理？ | 继续规划 |
| **DC-2: 扩容方案确认** | 完成方案制定后 | 扩容方案和预算？ | 输出报告 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `FORECAST-ACCURACY` | ±15% | 预测准确度：实际vs预测偏差 |
| `HEADROOM-MAINTAIN` | ≥20% | 容量余量：峰值时剩余容量 |
| `COST-ACCURACY` | ±20% | 成本准确度：预测vs实际成本 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 容量评估报告 | ☐ | 当前容量分析 |
| 需求预测报告 | ☐ | 未来需求预测 |
| 扩容方案 | ☐ | 详细方案 |
| 预算估算 | ☐ | 成本估算 |

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 容量利用率 | < 80% | 监控数据 |
| 扩容周期 | 按计划 | 执行记录 |
| 预测准确度 | > 80% | 偏差分析 |


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]
