---
name: inspection-report
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 巡检报告 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 巡检概要

- **巡检周期**: {start_date} ~ {end_date}
- **巡检负责人**: {inspector}
- **巡检环境**: {production / staging / all}
- **巡检类型**: {日常巡检 / 深度巡检 / 节假日巡检 / 故障后巡检}
- **总体健康状态**: {健康 / 警告 / 异常}

## 服务清单

| 服务名称 | 运行状态 | CPU 使用率 | 内存使用率 | 磁盘使用率 | 响应时间 | 错误率 |
|----------|----------|------------|------------|------------|----------|--------|
| {service} | {正常/异常} | {usage}% | {usage}% | {usage}% | {ms} | {rate}% |
| {service} | {正常/异常} | {usage}% | {usage}% | {usage}% | {ms} | {rate}% |
| {service} | {正常/异常} | {usage}% | {usage}% | {usage}% | {ms} | {rate}% |

## 基础设施状态

| 资源 | 总量 | 已用 | 可用 | 使用率 | 状态 |
|------|------|------|------|--------|------|
| {resource} | {total} | {used} | {available} | {rate}% | 正常/警告/异常 |
| {resource} | {total} | {used} | {available} | {rate}% | 正常/警告/异常 |

## 发现的异常

### 异常 1: {异常标题}

| 属性 | 值 |
|------|----|
| 发现时间 | {ISO8601} |
| 关联服务 | {service} |
| 异常描述 | {description} |
| 严重级别 | P0/P1/P2/P3 |
| 当前状态 | 处理中/已解决/待处理 |

### 异常 2: {异常标题}

| 属性 | 值 |
|------|----|
| 发现时间 | {ISO8601} |
| 关联服务 | {service} |
| 异常描述 | {description} |
| 严重级别 | P0/P1/P2/P3 |
| 当前状态 | 处理中/已解决/待处理 |

## 趋势分析

### 资源使用趋势

{描述 CPU、内存、磁盘等资源的趋势变化}

### 错误率趋势

{描述错误率的趋势变化}

### 告警趋势

| 指标 | 本期 | 上期 | 环比 | 趋势 |
|------|------|------|------|------|
| 告警总数 | {current} | {previous} | {delta}% | 上升/下降/持平 |
| P0 告警 | {current} | {previous} | {delta}% | 上升/下降/持平 |
| P1 告警 | {current} | {previous} | {delta}% | 上升/下降/持平 |

## 优化建议

| 建议ID | 建议内容 | 优先级 | 预期收益 | 建议负责人 |
|--------|----------|--------|----------|------------|
| SUG-001 | {suggestion} | H/M/L | {benefit} | {owner} |
| SUG-002 | {suggestion} | H/M/L | {benefit} | {owner} |

## 附件

- {巡检数据报表路径}
- {监控截图路径}
- {日志分析报告路径}

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
