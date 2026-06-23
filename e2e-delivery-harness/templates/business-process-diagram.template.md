---
name: business-process-diagram
type: deliverable-template
version: "1.0.0"
status: active
---

# 业务流程图 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 流程概述

- **流程名称**: {process_name}
- **流程编号**: BP-{number}
- **所属领域**: {business_domain}
- **版本**: {version}
- **创建人**: {author}
- **最后更新**: {ISO8601}

## 流程目标

{描述此业务流程的业务目标和价值}

## 参与角色

| 角色 | 角色类型 | 职责 | 系统/工具 |
|------|----------|------|-----------|
| {role} | {人工/系统/外部} | {responsibility} | {system} |
| {role} | {人工/系统/外部} | {responsibility} | {system} |
| {role} | {人工/系统/外部} | {responsibility} | {system} |

## 流程步骤

### 主流程

| 步骤 | 活动名称 | 执行角色 | 输入 | 输出 | 所需时间 |
|------|----------|----------|------|------|----------|
| 1 | {activity} | {role} | {input} | {output} | {duration} |
| 2 | {activity} | {role} | {input} | {output} | {duration} |
| 3 | {activity} | {role} | {input} | {output} | {duration} |
| 4 | {activity} | {role} | {input} | {output} | {duration} |
| 5 | {activity} | {role} | {input} | {output} | {duration} |

### 决策点

| 步骤 | 决策 | 条件 | 是(分支) | 否(分支) |
|------|------|------|----------|----------|
| {step} | {decision} | {condition} | {yes_branch} | {no_branch} |

### 异常流程

| 步骤 | 异常条件 | 处理方式 | 恢复步骤 |
|------|----------|----------|----------|
| {step} | {condition} | {handling} | {recovery} |

## 泳道图 (Swimlane) 描述

### 泳道划分

| 泳道 | 角色 | 包含活动 |
|------|------|----------|
| {swimlane} | {role} | {activities} |
| {swimlane} | {role} | {activities} |
| {swimlane} | {role} | {activities} |

### 泳道交互流程

```
{描述跨泳道的流程流转}
```

## 流程规则

### 业务规则

| 规则ID | 规则描述 | 触发条件 | 优先级 |
|--------|----------|----------|--------|
| BR-001 | {rule_description} | {trigger_condition} | {priority} |

### 约束条件

- {constraint_1}
- {constraint_2}

## BPMN 符号指南

| 符号 | 名称 | 含义 |
|------|------|------|
| 圆角矩形 | 活动/任务 | 表示一个业务活动或任务 |
| 菱形 | 决策/网关 | 表示分支、合并或决策点 |
| 圆形 | 事件 | 表示流程中的事件(开始/结束/中间) |
| 箭头 | 顺序流 | 表示活动之间的流转顺序 |
| 矩形带波浪 | 子流程 | 表示可展开的子流程 |
| 池/泳道 | 泳道 | 表示不同参与者或角色的责任区 |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
