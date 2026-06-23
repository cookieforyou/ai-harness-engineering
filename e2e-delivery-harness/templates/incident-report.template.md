---
name: incident-report
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 故障报告 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 故障基本信息

| 字段 | 值 |
|------|----|
| 故障ID | INC-{number} |
| 标题 | {incident_title} |
| 严重级别 | P0 - Critical / P1 - Major / P2 - Minor / P3 - Trivial |
| 状态 | 已解决 / 处理中 / 已关闭 |
| 报告人 | {reporter} |
| 处理人 | {responder} |
| 发现时间 | {ISO8601} |
| 解决时间 | {ISO8601} |
| 持续时间 | {duration} |
| 关联服务 | {affected_services} |

## 影响评估

### 影响范围

- **影响服务**: {affected_services}
- **影响用户**: {affected_users_count} 用户
- **影响功能**: {affected_functions}
- **影响时间**: {downtime_duration}
- **SLA 影响**: {是否影响 SLA}

### 业务影响

{描述对业务的具体影响,如:订单流失、用户体验受损等}

## 时间线

| 时间 | 事件 | 操作人 | 备注 |
|------|------|--------|------|
| {ISO8601} | {event_description} | {operator} | {notes} |
| {ISO8601} | {event_description} | {operator} | {notes} |
| {ISO8601} | {event_description} | {operator} | {notes} |
| {ISO8601} | {event_description} | {operator} | {notes} |

## 根因分析

### 直接原因

{direct_cause_description}

### 根本原因

{root_cause_description}

### 触发条件

{what_triggered_the_incident}

## 解决方案

### 应急措施

{immediate_actions_taken}

### 长期修复

{long_term_fix_plan}

### 验证方法

{how_the_fix_was_verified}

## 后续行动

| 行动ID | 行动描述 | 负责人 | 截止日期 | 状态 |
|--------|----------|--------|----------|------|
| ACT-001 | {action} | {owner} | {deadline} | 待处理/处理中/已完成 |
| ACT-002 | {action} | {owner} | {deadline} | 待处理/处理中/已完成 |

## 关联文档

- **Post-mortem**: [post-mortem-{id}.md]({path})
- **Runbook**: [runbook-{service}.md]({path})
- **变更记录**: [change-{id}.md]({path})

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
