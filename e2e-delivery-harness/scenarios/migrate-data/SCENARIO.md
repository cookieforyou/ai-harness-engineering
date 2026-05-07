---
name: migrate-data
version: 1.1.0
stage: migrate-data
description: Migrate Data scenario for the E2E delivery lifecycle
author: AI Harness Engineering Team
type: scenario
---

# Migrate Data Scenario (数据迁移场景)

## Purpose

本场景用于指导 AI Agent 执行数据迁移工作，包括迁移方案设计、数据清洗转换、迁移执行验证和回滚方案准备。

## Chain of Thought (思维链)

### Think-Aloud Protocol

```
THINK: 理解源系统和目标系统
   ↓
THINK: 分析数据结构和迁移复杂度
   ↓
THINK: 设计迁移方案和策略
   ↓
THINK: 准备数据清洗和转换规则
   ↓
EXECUTE: 执行数据迁移
   ↓
VALIDATE: 验证数据完整性
   ↓
OUTPUT: 输出迁移报告
```

### Step-by-Step Reasoning

**Step 1: 迁移评估**
- 问：数据量和复杂度如何？
- 验证：评估准确性
- 检查：依赖关系完整

**Step 2: 方案设计**
- 问：迁移方案是否可行？
- 验证：风险可控
- 检查：回滚方案完备

**Step 3: 数据准备**
- 问：数据清洗是否完整？
- 验证：数据质量达标
- 检查：转换规则正确

**Step 4: 迁移执行**
- 问：迁移过程是否正常？
- 验证：进度符合预期
- 检查：无异常发生

**Step 5: 数据验证**
- 问：数据是否完整准确？
- 验证：校验通过
- 检查：业务功能正常

## Primary Assets

- **Agent**: [../../agents/migrate-data.agent.md](../../agents/migrate-data.agent.md)
- **Instruction**: [../../instructions/migrate-data.instructions.md](../../instructions/migrate-data.instructions.md)
- **Prompt**: [../../prompts/migrate-data.prompt.md](../../prompts/migrate-data.prompt.md)
- **Skill**: [../../skills/migrate-data/SKILL.md](../../skills/migrate-data/SKILL.md)

## Error Handling (错误处理)

### EH-1: 数据不一致

- **识别信号**：校验发现数据不一致
- **处理方式**：
  1. 定位不一致数据
  2. 分析不一致原因
  3. 修复或重新迁移
  4. 重新校验
- **升级条件**：不一致率 > 阈值

### EH-2: 迁移超时

- **识别信号**：迁移任务超时
- **处理方式**：
  1. 检查任务状态
  2. 分析超时原因
  3. 决定继续或回滚
- **升级条件**：预估超时严重

### EH-3: 依赖失败

- **识别信号**：依赖服务不可用
- **处理方式**：
  1. 暂停迁移
  2. 等待依赖恢复
  3. 继续或回滚
- **升级条件**：依赖长时间不可用

## Decision Checkpoints (决策检查点)

| 检查点 | 触发条件 | 等待决策 | 下一步 |
|--------|----------|----------|--------|
| **DC-1: 迁移方案确认** | 完成迁移方案后 | 方案是否可行？回滚策略？ | 继续准备 |
| **DC-2: 数据校验确认** | 完成数据验证后 | 数据是否可接受？ | 切换或回滚 |
| **DC-3: 业务验证确认** | 完成业务验证后 | 是否切换流量？ | 正式切换 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DATA-INTEGRITY` | 100% | 数据完整性：迁移后数据一致性校验通过 |
| `DOWNTIME` | ≤{{downtime_budget}} | 停机时间：在预算范围内 |
| `ROLLBACK-READY` | 100% | 回滚就绪：迁移全程可回滚 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria (交接标准)

| 条件项 | 状态 | 说明 |
|--------|------|------|
| 迁移方案 | ☐ | 已评审通过 |
| 回滚方案 | ☐ | 已测试验证 |
| 迁移脚本 | ☐ | 已测试通过 |
| 验证报告 | ☐ | 完整准确 |

## Metrics

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| 数据完整率 | 100% | 记录数校验 |
| 数据准确率 | ≥ 99.99% | 字段校验 |
| 迁移成功率 | ≥ 99.9% | 成功记录/总数 |
| 业务停机时间 | 最小化 | 实际停机时长 |


## Prerequisites

- [ ] Prerequisite 1: Source and target schemas are documented and aligned
- [ ] Prerequisite 2: Data volume and transformation rules are analyzed
- [ ] Prerequisite 3: Rollback procedures are prepared and tested
