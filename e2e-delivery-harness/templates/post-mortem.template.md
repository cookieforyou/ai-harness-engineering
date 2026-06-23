---
name: post-mortem
type: deliverable-template
version: "1.0.0"
status: active
---

# 事故复盘 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 故障概述

- **故障标题**: {incident_title}
- **故障ID**: INC-{number}
- **复盘日期**: {ISO8601}
- **主持**: {facilitator}
- **参会人员**: {participants}
- **类型**: {代码缺陷 / 配置错误 / 架构设计 / 运维操作 / 第三方依赖 / 安全事件 / 其他}

## 故障摘要

{简要描述故障过程、影响和结果}

## 时间线

| 时间 | 事件 | 持续时间 | 关键决策 |
|------|------|----------|----------|
| {ISO8601} | {event} | {duration} | {decision} |
| {ISO8601} | {event} | {duration} | {decision} |
| {ISO8601} | {event} | {duration} | {decision} |

## 5 Whys 根因分析

```
Why 1: {故障现象}
  → 为什么? {原因1}
Why 2: {原因1}
  → 为什么? {原因2}
Why 3: {原因2}
  → 为什么? {原因3}
Why 4: {原因3}
  → 为什么? {原因4}
Why 5: {原因4}
  → 根本原因: {root_cause}
```

## 促成因素

| 因素 | 类别 | 描述 | 是否可控 |
|------|------|------|----------|
| {factor} | {技术/流程/人员} | {description} | 是/否/部分 |
| {factor} | {技术/流程/人员} | {description} | 是/否/部分 |

## 做得好的

1. {success_1}: {具体表现}
2. {success_2}: {具体表现}
3. {success_3}: {具体表现}

## 做得不好的

1. {failure_1}: {具体表现}
2. {failure_2}: {具体表现}
3. {failure_3}: {具体表现}

## 行动项

| 行动ID | 行动描述 | 类型 | 负责人 | 截止日期 | 状态 |
|--------|----------|------|--------|----------|------|
| PM-001 | {action} | {预防/检测/流程} | {owner} | {deadline} | {待处理/处理中/已完成} |
| PM-002 | {action} | {预防/检测/流程} | {owner} | {deadline} | {待处理/处理中/已完成} |
| PM-003 | {action} | {预防/检测/流程} | {owner} | {deadline} | {待处理/处理中/已完成} |

## 经验教训总结

{总结本次故障的核心经验教训和后续改进方向}

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
