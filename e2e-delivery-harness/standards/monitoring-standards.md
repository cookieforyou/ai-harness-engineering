---
name: monitoring-standards
description: "监控标准，定义指标命名规范、基数限制、Dashboard 组织与告警严重级别规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'monitoring', 'observability', 'prometheus', 'alerting']
---

# 监控标准

> 本规范定义 E2E Delivery Harness 中所有服务的监控体系标准，涵盖指标命名、基数限制、Dashboard 组织与告警级别。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. 监控体系架构

```
                    ┌─────────────────────────────────┐
                    │   AlertManager / PagerDuty       │
                    │   （告警聚合 + 路由 + 反掩码）      │
                    └──────────┬──────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   ┌────▼─────┐         ┌─────▼─────┐          ┌────▼─────┐
   │ Prometheus│         │  APM      │          │   ELK    │
   │ (Metrics) │         │ (Traces)  │          │ (Logs)   │
   └────┬─────┘         └─────┬─────┘          └────┬─────┘
        │                     │                     │
   ┌────▼─────┐         ┌─────▼─────┐          ┌────▼─────┐
   │ Service  │         │ Distributed│          │ Log      │
   │ Metrics  │         │ Tracing    │          │ Shippers │
   └──────────┘         └───────────┘          └──────────┘
```

三类可观测数据 (Metrics / Traces / Logs) 必须全部就绪，称为 "三条腿的凳子" (Three Pillars of Observability)。

## 2. 指标命名规范 (Metric Naming)

### 2.1 通用命名模式

```
<namespace>_<subsystem>_<metric_name>_<unit>

示例:
harness_api_requests_total
harness_api_request_duration_seconds
harness_db_query_count
harness_cache_hit_ratio
```

| 组件 | 命名规则 | 示例 |
|------|----------|------|
| **命名空间** | 服务/应用名（单数小写） | `harness`, `payment`, `auth` |
| **子系统** | 模块名 | `api`, `db`, `cache`, `queue` |
| **指标名** | 含义清晰，使用下划线分隔 | `request_duration`, `error_total` |
| **单位** | 标准单位（推荐 Prometheus 惯例） | `_seconds`, `_bytes`, `_total`, `_ratio` |

### 2.2 四类黄金指标命名

参考 [sre-best-practices.md](../standards/sre-best-practices.md) Golden Signals：

| 信号 | 指标示例 | 类型 |
|------|----------|------|
| **Latency** | `{service}_request_duration_seconds{quantile}` | Histogram |
| **Traffic** | `{service}_requests_total{status,method,endpoint}` | Counter |
| **Errors** | `{service}_errors_total{type,code}` | Counter |
| **Saturation** | `{service}_cpu_usage_ratio`, `{service}_memory_bytes` | Gauge |

### 2.3 标签命名规范 (Label Conventions)

| 标签名 | 定义 | 示例值 | 基数 |
|--------|------|--------|------|
| `service` | 服务名 | `payment`, `order-api` | 低 |
| `environment` | 部署环境 | `production`, `staging`, `dev` | 低 (≤ 5) |
| `version` | 应用版本 | `v2.1.3` | 低 |
| `method` | HTTP 方法 | `GET`, `POST`, `PUT` | 低 (≤ 7) |
| `endpoint` | 路由路径 | `/api/orders`, `/healthz` | 中 (≤ 50) |
| `status` | HTTP 状态码 | `200`, `404`, `500` | 低 (≤ 20) |
| `target` | 后端目标 | `primary-db`, `redis-cluster` | 低 |
| `error_type` | 错误类别 | `timeout`, `validation`, `internal` | 中 (≤ 10) |

## 3. 指标基数限制 (Cardinality Limits)

### 3.1 基数控制原则

| 标签类型 | 基数上限 | 示例 | 风险 |
|----------|----------|------|------|
| **低基数** | ≤ 100 | `method`, `status`, `environment` | 安全 |
| **中基数** | ≤ 10,000 | `endpoint`, `error_type`, `region` | 可接受 |
| **高基数** | > 10,000 | `user_id`, `request_id`, `session_id`, `email` | **禁止** |

### 3.2 高基数反模式

| ❌ 禁止 | ✅ 替代方案 |
|---------|-------------|
| `user_id` 作为 metrics label | 使用日志存储用户级数据，保留在 traces/logs 中 |
| `request_id` 作为 metrics label | 使用日志，metrics 聚合到 endpoint 级别 |
| `session_id` 作为 metrics label | 使用日志，metrics 只记录活跃会话总数的 gauge |
| `ip_address` 作为 metrics label | 使用日志，或聚合到 region/city 级别 |
| `error_message` 作为 metrics label | 使用 `error_type` (categorize) + 日志存储详情 |

### 3.3 基数监控

- Prometheus 等服务端应设置 `--storage.tsdb.retention.time=30d`
- 启用 `--storage.tsdb.max-block-duration=2h`
- 每个 prometheus 实例识别标签上限：`while true; do curl localhost:9090/api/v1/label/__name__/values; sleep 3600; done`
- 定期检查：`topk(10, count by (__name__) ({__name__=~".+"}))` 查看高基数指标

## 4. Dashboard 组织标准 (Dashboard Organization)

### 4.1 分层 Dashboard 体系

| 层级 | 受众 | 内容 | 更新频率 |
|------|------|------|----------|
| **L0 — Executive Summary** | VP/总监 | 系统总体健康、SLO 达标率、收入影响 | 实时 + 日报 |
| **L1 — Service Overview** | Team Lead/SRE | 所有微服务的 Golden Signals | 实时 |
| **L2 — Service Detail** | 开发工程师 | 单服务的详细指标、依赖关系 | 实时 |
| **L3 — Resource View** | 运维工程师 | 基础设施资源（CPU/内存/磁盘/网络） | 实时 |
| **L4 — Debugging** | On-call 工程师 | 按需的深度调试图表 | 按需 |

### 4.2 Dashboard 设计规范

| 规范 | 说明 |
|------|------|
| **左到右、上到下** | 按照数据流方向排列图表（入口→逻辑→存储） |
| **统一时间范围** | 所有面板默认使用相同时间范围（建议 1h/6h/24h/7d） |
| **红色优先** | 异常状态使用红色，正常用绿色，警告用黄色 |
| **单位标注** | 每个图表 Y 轴标注单位（ms, %, req/s, bytes） |
| **辅助线** | 标注 SLO 阈值线（红色虚线）、基线（灰色虚线） |
| **模板变量** | 提供 service / endpoint / environment 等变量 |
| **最少图表** | 每行不超过 4 个图表，单个 Dashboard ≤ 20 行 |

### 4.3 必含 Dashboard 清单

每个服务至少需要以下 Dashboard：

- [ ] **Overview**: 4 Golden Signals + SLO Burn Rate
- [ ] **Dependencies**: 上下游服务健康状态 + 延迟
- [ ] **Resources**: CPU, Memory, Disk, 网络, 连接池
- [ ] **Business**: 关键业务指标（订单量、注册量、转化率）
- [ ] **Errors**: 错误类型分布 + 错误日志样本
- [ ] **Deployments**: 部署历史、回滚事件、版本变更

## 5. 告警严重级别 (Alert Severity Levels)

| 级别 | 标签 | 响应时间 | 通知方式 | 适用场景 |
|------|------|----------|----------|----------|
| **P0 (Critical)** | `severity: critical` | ≤ 5 分钟 | 电话 + Slack + 邮件 | 服务宕机、数据丢失、支付失败 |
| **P1 (High)** | `severity: high` | ≤ 15 分钟 | Slack + 邮件 | 高错误率、P99 超标、核心依赖异常 |
| **P2 (Medium)** | `severity: warning` | ≤ 1 小时 | Slack | 错误率轻微上升、资源水位告警 |
| **P3 (Low)** | `severity: info` | 下一个工作日 | Email | 证书即将过期、磁盘趋势上升 |
| **P4 (None)** | `severity: none` | 不通知 | Dashboard 显示 | 调试指标、审计计数 |

参见 [alerting-guidelines.md](../standards/alerting-guidelines.md) 获取告警路由与通知策略。

## 6. 指标保留策略 (Data Retention)

| 数据粒度 | 保留时长 | 存储引擎 |
|----------|----------|----------|
| 原始指标 (Raw, 每 15s) | 7 天 | Prometheus TSDB |
| 聚合指标 (5min avg) | 30 天 | Prometheus + Thanos |
| 日聚合 (1h avg) | 1 年 | Thanos / 对象存储 |
| 告警事件 | 2 年 | 告警管理平台 |
| 审计日志 | 3 年 | 对象存储 / 日志归档 |

## 7. 监控合规清单 (Monitoring Compliance Checklist)

- [ ] 每个服务暴露 Prometheus `/metrics` 或兼容端点
- [ ] 指标命名遵循 `<namespace>_<subsystem>_<name>_<unit>` 模式
- [ ] 所有指标标签基数 ≤ 10,000（无 user_id/request_id 等高基数标签）
- [ ] Dashboard 至少包含 L1 层级的 Overview 页面
- [ ] 告警规则定义了 P0-P3 级别并有对应通知方式
- [ ] 指标保留策略满足审计合规要求（≥ 1 年）
- [ ] Monitoring 组件自身也有健康检查 (Prometheus Alertmanager 自身告警)

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [sre-best-practices.md](../standards/sre-best-practices.md)
- [alerting-guidelines.md](../standards/alerting-guidelines.md)
- [health-check-guidelines.md](../standards/health-check-guidelines.md)
