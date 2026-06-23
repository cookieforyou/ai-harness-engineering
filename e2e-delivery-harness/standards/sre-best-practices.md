---
name: sre-best-practices
description: "SRE 最佳实践标准，定义 SLI/SLO/SLA、Error Budget、Golden Signals、Toil 管理与 Incident 生命周期规范"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'sre', 'reliability', 'slo', 'error-budget', 'incident']
---

# SRE 最佳实践

> 本规范定义 E2E Delivery Harness 中所有服务的可靠性工程标准，涵盖 SLI/SLO/SLA、Error Budget、Golden Signals、Toil 管理与 Incident 生命周期。审查基准见 [harness-engineering.md](../harness-engineering.md)。

## 1. SLI / SLO / SLA 定义

### 1.1 核心概念

| 术语 | 定义 | 示例 |
|------|------|------|
| **SLI (Service Level Indicator)** | 服务质量的量化指标 | 请求延迟 P99, 错误率, 吞吐量 |
| **SLO (Service Level Objective)** | SLI 的目标阈值，内部承诺 | P99 ≤ 200ms, 错误率 < 0.1% |
| **SLA (Service Level Agreement)** | 对外客户承诺，通常比 SLO 宽松 | 可用性 ≥ 99.9%, 月度赔付 |

**铁三角关系**: SLA ≤ SLO ≤ SLI 实际表现。SLO 应比 SLA 严格 30-50% 以留出 Error Budget 缓冲。

### 1.2 SLI 指标体系

每个服务必须定义至少以下三类 SLI：

| 类别 | SLI 指标 | 测量方式 | 采集源 |
|------|----------|----------|--------|
| **可用性** | 请求成功率 (HTTP 2xx/4xx/5xx) | (successful / total) × 100% | 反向代理 / API Gateway |
| **延迟** | P50 / P95 / P99 响应时间 | 毫秒级分位数 | APM / 服务 metrics |
| **吞吐量** | 每秒请求数 (RPS/TPS) | count / window | 入口 metrics |
| **饱和度** | CPU / 内存 / 连接池使用率 | resource used / total | 基础设施 metrics |
| **错误率** | 5xx + 业务异常 / 总请求 | (error / total) × 100% | 服务 + 业务日志 |

### 1.3 SLO 分级

| 级别 | 可用性目标 | 月度不可用时间 | 适用服务类型 |
|------|-----------|----------------|--------------|
| **Tier 0 (Critical)** | 99.99% (Four 9s) | ≤ 4.3 分钟 | 支付、认证、核心交易 |
| **Tier 1 (High)** | 99.95% (Three 9s) | ≤ 21.6 分钟 | 核心业务 API、用户数据 |
| **Tier 2 (Standard)** | 99.9% (Three 9s) | ≤ 43.2 分钟 | 非核心业务、后台服务 |
| **Tier 3 (Best Effort)** | 99.0% (Two 9s) | ≤ 7.3 小时 | 内部工具、辅助服务 |
| **Tier 4 (No SLO)** | 无承诺 | N/A | 开发实验、原型 |

## 2. Error Budget (错误预算)

### 2.1 基本原理

Error Budget = (1 - SLO) × 总时间窗口。例如 99.9% SLO → 月度 Error Budget = 43.2 分钟。

### 2.2 Error Budget 消耗与决策

| Error Budget 消耗 | 行动 | 说明 |
|-------------------|------|------|
| < 50% | 正常发布 | 常规变更流程 |
| 50% - 80% | 减速发布 | 高风险变更需特批，增加金丝雀观察时间 |
| 80% - 100% | 冻结发布 | 仅允许紧急修复 (hotfix)，其他变更冻结 |
| > 100% | 强制回滚 + 复盘 | 触发 [incident-management.md](../standards/incident-management.md) P0 流程 |

### 2.3 Error Budget 跟踪

- 每月初重置 Error Budget
- 以周为单位跟踪消耗趋势（避免月底集中耗尽）
- 多服务共享 Error Budget：每个服务独立计算，不跨服务共享
- Spikes 处理：单次 incident 消耗超过月度 20% 时自动告警

## 3. Golden Signals (黄金信号)

Google SRE 定义的四个黄金信号，每个服务必须暴露并监控：

### 3.1 延迟 (Latency)

- 区分成功请求与失败请求的延迟（失败可能很快但也意味着异常）
- 测量口径：P50(基线), P95(警示), P99(告警), P999(紧急)
- 客户端侧与服务器侧延迟均需采集

### 3.2 流量 (Traffic)

- HTTP: RPS (每秒请求数)
- 数据库: QPS (每秒查询数), TPS (每秒事务数)
- 消息队列: 每秒发布/消费消息数
- 存储: IOPS, 吞吐量 MB/s

### 3.3 错误 (Errors)

- HTTP 5xx: 服务器端错误
- HTTP 4xx: 客户端错误（关注比例变化）
- 业务异常: 自定义错误码（关注总占比）
- 隐式错误: 响应 200 但业务处理失败（需业务日志分析）

### 3.4 饱和度 (Saturation)

- 资源使用率: CPU(%), 内存(%), 磁盘(%)
- 连接池: 活跃连接 / 最大连接
- 队列深度: 消息积压数, 任务队列长度
- 限流率: 被限流的请求比例（次/分钟）

## 4. Toil 管理 (Toil Management)

### 4.1 Toil 定义

Toil 是手动、重复、可自动化、无长期价值的运维操作。特征：
- **手动执行**: 需要人工介入而非自动化
- **重复性**: 以规律性（每日/每周）频率发生
- **可自动化**: 存在明确的规则可转化为代码
- **无长期价值**: 操作完成没有改进系统状态

### 4.2 Toil 跟踪与目标

| 指标 | 当前目标 | 长期目标 |
|------|----------|----------|
| 每人每周 Toil 时间 | < 8 小时 | < 4 小时 |
| Toil 自动化解锁率 | 每月 ≥ 2 项 | 持续递减 |
| 新告警产生 Toil 比例 | < 10% 告警需要操作 | < 5% |

### 4.3 反模式 (Anti-patterns)

- **英雄主义**: 依赖特定个人手动处理重复操作
- **Runbook 从未执行**: 写了文档但没有人实际跟着做
- **半自动化**: 脚本需要人工参数调整（完全自动化 vs 不可自动化）
- **告警疲劳**: 告警太多导致忽略重要告警（参见 [alerting-guidelines.md](../standards/alerting-guidelines.md)）

## 5. Incident 管理生命周期 (Incident Management Lifecycle)

参见 [incident-management.md](../standards/incident-management.md) 完整流程。

### 5.1 生命周期阶段

```
Detection → Response → Mitigation → Resolution → Follow-up
    ↑                                             |
    └─────────────────────────────────────────────┘
```

### 5.2 关键时间节点

| 阶段 | 目标时间 | 职责 |
|------|----------|------|
| **Detection (检测)** | ≤ 1 分钟 (自动) / ≤ 5 分钟 (人工) | 监控系统 / 用户 |
| **Response (响应)** | ≤ 5 分钟 (P0) / ≤ 15 分钟 (P1) | On-call 工程师 |
| **Mitigation (缓解)** | ≤ 15 分钟 (P0) / ≤ 30 分钟 (P1) | Incident Commander |
| **Resolution (解决)** | ≤ 60 分钟 (P0) / ≤ 4 小时 (P1) | 技术团队 |
| **Follow-up (复盘)** | T+ 72 小时内 | 全体参与团队 |

### 5.3 事后复盘 (Postmortem) 模板要点

- 时间线 (Timeline): 所有事件的精确时间戳
- 影响范围: 用户数、请求量、收入影响
- 根因 (Root Cause): 5 Whys 分析法
- 行动项: 每个项指定 DRI + 截止日期，分为缓解/预防/检测三类
- 无指责文化: 复盘聚焦系统改进，不追责个人

## 6. 服务等级协议对照表 (SLA → SLO → SLI Mapping)

| 服务 | SLA | SLO | 关键 SLI | Burn Rate 告警阈值 |
|------|-----|-----|----------|-------------------|
| API Gateway | 99.95% | 99.99% | 延迟 P99 < 100ms, 错误率 < 0.05% | 5%/10m, 2%/1h |
| 支付服务 | 99.99% | 99.995% | 成功率 > 99.99%, P99 < 500ms | 2%/5m |
| 用户认证 | 99.9% | 99.99% | 登录成功率 > 99.99%, P99 < 1s | 5%/10m |
| 消息推送 | 99.0% | 99.5% | 投递成功率 > 99.5%, P95 < 5s | 10%/1h |

## 7. DC-* 映射项

本标准中关键决策点可映射为 Scenario DC-*:

- `DC-SRE-001` — SLO 类型与阈值选择有效
- `DC-SRE-002` — Error Budget 消耗在安全范围内
- `DC-SRE-003` — Golden Signals 已全部暴露与监控
- `DC-SRE-004` — Incident 响应时间满足分级要求

## 相关资产

- [asset-model.md](../standards/asset-model.md)
- [authoring-checklist.md](../standards/authoring-checklist.md)
- [monitoring-standards.md](../standards/monitoring-standards.md)
- [alerting-guidelines.md](../standards/alerting-guidelines.md)
- [incident-management.md](../standards/incident-management.md)
