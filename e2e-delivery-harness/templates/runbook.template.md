---
name: runbook
type: deliverable-template
version: "1.0.0"
status: active
language: "zh-CN"
---

# 运维 Runbook 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 服务概述

- **服务名称**: {service_name}
- **服务类型**: {微服务 / 单体 / 批处理 / 前端}
- **技术栈**: {tech_stack}
- **部署环境**: {production/staging/dev}
- **负责人**: {owner}
- **SLA**: {availability_target}

## 架构概览

### 服务拓扑

```
{描述服务拓扑或引用架构图}
```

### 关键依赖

| 依赖项 | 类型 | 重要性 | 备用方案 |
|--------|------|--------|----------|
| {dependency} | 内部/外部 | 高/中/低 | {fallback} |

## 日常运维操作

### 服务启停

```
# 启动服务
{command}

# 停止服务
{command}

# 重启服务
{command}

# 查看状态
{command}
```

### 日志查看

```
# 应用日志
{command}

# 错误日志
{command}

# 访问日志
{command}
```

## 常见告警及响应

### 告警: {告警名称}

| 属性 | 值 |
|------|----|
| 告警级别 | P0/P1/P2/P3 |
| 监控指标 | {metric_name} |
| 触发条件 | {condition} (阈值: {threshold}) |
| 影响范围 | {impact} |

**响应步骤**:
1. {step 1}
2. {step 2}
3. {step 3}

**快速诊断命令**:
```
{diagnostic_commands}
```

### 告警: {告警名称}

| 属性 | 值 |
|------|----|
| 告警级别 | P0/P1/P2/P3 |
| 监控指标 | {metric_name} |
| 触发条件 | {condition} (阈值: {threshold}) |
| 影响范围 | {impact} |

**响应步骤**:
1. {step 1}
2. {step 2}

**快速诊断命令**:
```
{diagnostic_commands}
```

## 诊断流程

### 健康检查

```
{health_check_command}
```

### 性能诊断

```
{performance_diagnostic_steps}
```

### 错误排查

```
{error_troubleshooting_steps}
```

## 应急联系人

| 角色 | 姓名 | 联系方式 | 备用联系 |
|------|------|----------|----------|
| On-call 工程师 | {name} | {phone} | {slack} |
| 服务负责人 | {name} | {phone} | {slack} |
| DBA | {name} | {phone} | {slack} |
| 安全负责人 | {name} | {phone} | {slack} |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
