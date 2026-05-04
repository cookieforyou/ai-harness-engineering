---
name: hotfix
version: "1.1.0"
stage: "hotfix"
---

# Hotfix Scenario (紧急修复场景)

## Purpose

本场景用于指导 AI Agent 执行紧急缺陷修复工作，在最短时间内定位问题、修复代码、验证上线。

## Chain of Thought (思维链)

### Think-Aloud Protocol

```
THINK: 理解问题严重性和影响范围
   ↓
THINK: 快速定位问题根因
   ↓
THINK: 设计最小化修复方案
   ↓
THINK: 执行修复和验证
   ↓
VALIDATE: 验证修复有效
   ↓
OUTPUT: 输出修复报告
```

## Primary Assets

- **Agent**: [../../agents/hotfix.agent.md](../../agents/hotfix.agent.md)
- **Instruction**: [../../instructions/hotfix.instructions.md](../../instructions/hotfix.instructions.md)
- **Prompt**: [../../prompts/hotfix.prompt.md](../../prompts/hotfix.prompt.md)
- **Skill**: [../../skills/hotfix/SKILL.md](../../skills/hotfix/SKILL.md)

## Error Handling (错误处理)

### EH-1: 根因不明

- **识别信号**：无法快速定位问题
- **处理方式**：
  1. 扩大日志范围
  2. 排查最近变更
  3. 临时止血方案
- **升级条件**：30 分钟内无法定位

### EH-2: 修复失败

- **识别信号**：修复后问题仍存在
- **处理方式**：
  1. 回滚修复
  2. 重新分析
  3. 制定新方案
- **升级条件**：多次修复失败

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 问题确认** | 完成问题分析后 | 影响范围和优先级？ | 继续或升级 |
| **DC-2: 修复方案确认** | 完成修复设计后 | 方案是否可行？ | 执行修复 |
| **DC-3: 上线确认** | 完成验证后 | 是否接受上线？ | 部署发布 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `HOTFIX-TIME` | ≤4h | 修复时间：P0问题从发现到修复上线 |
| `REGRESSION-RATE` | ≤5% | 回归率：热修复引入新问题比例 |
| `VERIFY-COVERAGE` | 100% | 验证覆盖率：所有场景已回归验证 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 修复代码 | ☐ | 已测试通过 |
| 验证报告 | ☐ | 修复有效 |
| 回滚方案 | ☐ | 已准备 |
| 变更记录 | ☐ | 已记录 |

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 修复时间 | ≤ 目标时间 | 实际修复时长 |
| 问题复发 | 0 | 监控验证 |
| 引入新问题 | 0 | 回归测试 |


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]
