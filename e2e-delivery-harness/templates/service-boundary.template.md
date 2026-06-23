---
name: service-boundary
type: deliverable-template
version: "1.0.0"
status: active
---

# 服务边界定义 模板

> 复制本模板到 `docs/` 对应路径，由 Agent 按 [standards/harness-engineering.md](../standards/harness-engineering.md) 填充。

## 元数据

- 项目: {project_name}
- 版本: {version}
- 作者: {author}
- 日期: {ISO8601}

## 正文

## 服务概览

- **服务名称**: {service_name}
- **服务ID**: SVC-{number}
- **所属领域**: {bounded_context}
- **服务类型**: {业务服务 / 基础设施服务 / 边缘服务}
- **技术栈**: {tech_stack}
- **服务负责人**: {owner}
- **服务等级**: {核心服务 / 非核心服务}

## 有界上下文 (Bounded Context)

### 上下文定义

{描述此服务的有界上下文边界}

### 领域模型

{描述核心领域实体和聚合根}

### 上下文映射

| 集成方式 | 合作方 | 方向 | 协议 |
|----------|--------|------|------|
| {合作/防腐层/开放服务} | {context_name} | {上游/下游/双向} | {protocol} |

## 数据所有权

### 拥有数据

| 数据实体 | 存储方式 | 数据敏感度 | 保留策略 |
|----------|----------|------------|----------|
| {entity} | {database/table} | {高/中/低} | {retention} |

### 引用数据

| 数据实体 | 数据来源 | 同步方式 | 缓存策略 |
|----------|----------|----------|----------|
| {entity} | {source_service} | {API/Event/DB} | {cache_strategy} |

## 对外 API

| API 名称 | 方法 | 路径 | 消费者 | 版本 |
|----------|------|------|--------|------|
| {api} | GET/POST/PUT/DELETE | {/api/v1/} | {consumer} | v1 |
| {api} | GET/POST/PUT/DELETE | {/api/v1/} | {consumer} | v1 |

## 依赖服务

| 依赖服务 | 调用方式 | 通信协议 | SLA 要求 | 熔断策略 |
|----------|----------|----------|----------|----------|
| {service} | {sync/async} | {REST/gRPC/Event} | {sla} | {circuit_breaker} |

## 事件

### 发布事件

| 事件名称 | 触发条件 | 负载内容 | 消费者 |
|----------|----------|----------|--------|
| {event_name} | {trigger} | {payload} | {consumer} |

### 订阅事件

| 事件名称 | 发布者 | 处理逻辑 | 响应时间要求 |
|----------|--------|----------|--------------|
| {event_name} | {publisher} | {handler} | {latency} |

## SLO 目标

| 指标 | 目标值 | 测量方法 | 告警阈值 | 测量周期 |
|------|--------|----------|----------|----------|
| 可用性 | {target}% | {method} | {alert_threshold} | {period} |
| 响应时间(P95) | {target}ms | {method} | {alert_threshold} | {period} |
| 错误率 | < {target}% | {method} | {alert_threshold} | {period} |
| 吞吐量 | {target} req/s | {method} | {alert_threshold} | {period} |

## 修订历史

| 版本 | 日期 | 作者 | 变更内容 | 评审人 |
|------|------|------|----------|--------|
| v1.0 | {ISO8601} | {author} | 初稿 | {reviewer} |

## 验证

- [ ] 已通过 [evaluations/output-validation-checklist.md](../evaluations/output-validation-checklist.md)
