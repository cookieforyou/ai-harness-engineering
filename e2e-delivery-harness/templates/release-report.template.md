---
name: release-report
type: deliverable-template
version: "1.0.0"
status: active
---

# 发布报告 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 发布摘要

- **发布版本**: {version}
- **发布日期**: {ISO8601}
- **发布负责人**: {release_manager}
- **发布状态**: {成功 / 部分成功 / 失败 / 回滚}
- **发布类型**: {常规发布 / 紧急修复 / 里程碑发布}

## 部署统计

### 部署范围

| 组件/服务 | 部署前版本 | 部署后版本 | 部署方式 | 部署结果 |
|-----------|------------|------------|----------|----------|
| {component} | {v1.0} | {v1.1} | {滚动/蓝绿} | 成功/失败 |
| {component} | {v1.0} | {v1.1} | {滚动/蓝绿} | 成功/失败 |

### 部署耗时

| 阶段 | 计划耗时 | 实际耗时 | 偏差 |
|------|----------|----------|------|
| 数据库变更 | {plan} | {actual} | {delta} |
| 应用部署 | {plan} | {actual} | {delta} |
| 部署验证 | {plan} | {actual} | {delta} |

## 验证结果

### 冒烟测试

| 测试项 | 结果 | 备注 |
|--------|------|------|
| {test_item} | PASS/FAIL | {notes} |
| {test_item} | PASS/FAIL | {notes} |

### 监控指标

| 指标 | 发布前基线 | 发布后值 | 状态 |
|------|-----------|----------|------|
| {metric} | {baseline} | {current} | 正常/异常 |
| {metric} | {baseline} | {current} | 正常/异常 |
| {metric} | {baseline} | {current} | 正常/异常 |

## 发布问题

| 问题ID | 问题描述 | 严重级别 | 状态 | 解决方案 |
|--------|----------|----------|------|----------|
| {issue_id} | {description} | P0-P3 | {已解决/待处理} | {solution} |

## 监控状态

| 监控项 | 状态 | 告警级别 | 处理人 |
|--------|------|----------|--------|
| 应用健康检查 | 正常/异常 | {level} | {owner} |
| 错误率 | 正常/异常 | {level} | {owner} |
| 响应时间 | 正常/异常 | {level} | {owner} |
| CPU/内存 | 正常/异常 | {level} | {owner} |

## 干系人确认

| 干系人 | 角色 | 确认状态 | 确认时间 |
|--------|------|----------|----------|
| {name} | 产品经理 | 已确认/待确认 | {time} |
| {name} | 开发负责人 | 已确认/待确认 | {time} |
| {name} | 测试负责人 | 已确认/待确认 | {time} |
| {name} | 运维负责人 | 已确认/待确认 | {time} |

## 经验教训

### 做得好

1. {success_experience_1}
2. {success_experience_2}

### 待改进

1. {improvement_item_1}
2. {improvement_item_2}

### Action Items

| 任务 | 负责人 | 截止日期 |
|------|--------|----------|
| {action_item} | {owner} | {deadline} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
