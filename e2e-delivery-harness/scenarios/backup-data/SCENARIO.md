---
name: backup-data
version: "1.1.0"
stage: "backup-data"
---

# Scenario: 数据备份 (Backup Data)

## Overview

本场景用于设计、实现和管理数据备份策略，包括数据库备份、文件备份、灾备方案等。

## Chain of Thought

```
[THINK] 分析备份需求
├─ 识别需要备份的数据
├─ 评估 RTO/RPO 要求
├─ 确定备份频率和保留期

[ANALYZE] 设计备份策略
├─ 选择备份类型（全量/增量/差异）
├─ 设计备份存储方案
├─ 规划备份验证机制

[DESIGN] 实现备份系统
├─ 搭建备份服务
├─ 配置备份任务
├─ 设置监控告警

[IMPLEMENT] 部署备份方案
├─ 配置备份脚本/工具
├─ 测试备份恢复
├─ 验证备份完整性

[VERIFY] 验证备份就绪
├─ 备份恢复测试
├─ 备份时间验证
├─ 备份监控验证
```

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 备份策略选型 | 哪种备份方案？ |
| DC-002 | 存储位置 | 本地还是云端？ |
| DC-003 | 恢复验证 | 是否需要定期演练？ |

## Error Handling

| 错误类型 | 处理方式 |
|----------|----------|
| 备份失败 | 重试并告警 |
| 存储空间不足 | 清理旧备份 |
| 备份损坏 | 使用上一版本 |
| 恢复失败 | 触发灾备恢复 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `BACKUP-SUCCESS` | ≥99.5% | 备份成功率 |
| `RPO-COMPLY` | 100% | RPO达成：数据丢失量≤RPO目标 |
| `RESTORE-TEST` | ≥1/quarter | 恢复测试频率：每季度至少一次 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

- [x] 备份策略已定义
- [x] 备份任务已配置
- [x] 监控告警已设置
- [x] 恢复演练已通过
- [x] 运维文档已编写

## Associated Assets

- **Prompt**: `prompts/backup-data.prompt.md`
- **Instruction**: `instructions/backup-data.instructions.md`
- **Agent**: `agents/backup-data.agent.md`
- **Skill**: `skills/backup-data/SKILL.md`


## Purpose

> Define the objectives and scope of the backup-data scenario.
>
> This scenario ensures systematic execution of backup-data activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/backup-data/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/backup-data.prompt.md` | Execution prompt |
| Instructions | `instructions/backup-data.instructions.md` | Technical instructions |
| Agent | `agents/backup-data.agent.md` | Responsible agent |
| Skill | `skills/backup-data/SKILL.md` | Domain skill |
