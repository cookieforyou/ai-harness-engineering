---
name: integrate-monitor
description: "Domain skill for integrate-monitor execution"
category: operations
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 监控集成 (Integrate Monitor)

## Overview

本 Skill 定义了监控集成的核心知识体系，涵盖可观测性三大支柱（Metrics / Logs / Traces）、SLO/SLI/SLA 框架、告警策略设计、Dashboard 构建方法论，帮助团队为企业级系统搭建标准化、高可用的可观测性平台。

## Core Knowledge

### 可观测性三大支柱 (Three Pillars of Observability)

#### 指标 (Metrics)

Prometheus 数据模型是当前业界标准，核心概念包括：

- **Counter**: 累计计数器（如 HTTP 请求总数），只能增加或重置
- **Gauge**: 可增可减的瞬时值（如 CPU 使用率、内存占用量）
- **Histogram**: 分位数分布（如请求延迟 P50/P95/P99），支持分桶统计
- **Summary**: 预计算的分位数（与 Histogram 类似，但由客户端计算）

PromQL 是 Prometheus 的数据查询语言，常用模式：

```promql
# RED 核心指标
rate(http_requests_total{status="5xx"}[5m]) / rate(http_requests_total[5m]) * 100  # 错误率
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))  # P95 延迟

# USE 核心指标
avg(node_cpu_seconds_total{mode="idle"}[5m])  # CPU 利用率
rate(node_disk_io_time_seconds_total[5m])      # 磁盘饱和度
```

#### 日志 (Logs)

结构化日志是最佳实践，推荐使用 JSON 格式，包含以下标准字段：

```json
{
  "timestamp": "2026-06-23T10:30:00.123Z",
  "level": "ERROR",
  "service": "order-service",
  "trace_id": "abc123def456",
  "span_id": "span001",
  "message": "Order processing failed",
  "error": {
    "type": "ValidationError",
    "message": "Invalid payment amount"
  },
  "metadata": {
    "order_id": "ORD-20260623-001",
    "user_id": "usr_78901"
  }
}
```

ELK (Elasticsearch + Logstash + Kibana) 或 Loki + Grafana 是主流的日志管道，关键配置：

- Logstash 解析规则：grok / dissect / json 过滤器
- Elasticsearch 索引策略：按天分索引，ILM 管理生命周期
- Kibana 可视化：基于日志创建 Dashboard 和告警

#### 链路追踪 (Traces)

OpenTelemetry 是工业标准的分布式追踪框架，核心概念：

- **Trace**: 一次请求的完整调用链，由多个 Span 组成
- **Span**: 调用链中的一个操作单元，包含名称、开始/结束时间、状态、属性
- **Context Propagation**: 通过 W3C TraceContext 或 B3 传播协议，在服务间传递 Trace 上下文

Span 最少属性要求：

```
service.name     — 所属服务名
trace.id         — 追踪ID
span.id          — 当前Span ID
parent.span.id   — 父Span ID
duration         — 执行耗时 (ms)
status           — OK / ERROR
```

### SLO / SLI / SLA 框架

| 术语 | 定义 | 示例 |
|------|------|------|
| **SLI** (Service Level Indicator) | 服务质量的可量化指标 | 可用性 = `成功请求数 / 总请求数` |
| **SLO** (Service Level Objective) | SLI 的目标值 | 月度可用性 ≥ 99.9% |
| **SLA** (Service Level Agreement) | 对外承诺的 SLO + 处罚条款 | 月度可用性 < 99.9% 赔偿 10% 月费 |

**Error Budget (错误预算)**: 1 - SLO，即允许的不达标时间。当月错误预算 = 30天 × 24小时 × 60分钟 × (1 - 0.999) ≈ 43分钟。当 Error Budget 消耗超过 50% 时触发告警，超过 100% 时阻止新功能发布。

### 告警体系设计

RED 方法用于告警：每个服务至少配置四个核心告警规则：

| 告警 | 指标 | 阈值 | 严重级别 | 通知渠道 |
|------|------|------|---------|---------|
| 高错误率 | `error_rate > 1%` | 1% 持续 5min | P0 | PagerDuty + 电话 |
| 高延迟 | `p95_latency > 500ms` | 500ms 持续 5min | P1 | Slack + IM |
| 低可用性 | `availability < 99.9%` | 99.9% 持续 10min | P0 | PagerDuty + 电话 |
| 饱和度 | `saturation > 80%` | 80% 持续 15min | P2 | Email |

告警路由矩阵：

- **P0 (Critical)**: PagerDuty + 电话 → 值班工程师，15min 响应
- **P1 (High)**: Slack / 企业微信 → 服务 Owner，30min 响应
- **P2 (Warning)**: Email / Ticket → 相关团队，8h 内处理
- **P3 (Info)**: Dashboard 展示，不主动通知

### Dashboard 设计原则

- **基础设施 Dashboard**: USE 方法组织，每行一个资源类型（CPU / 内存 / 磁盘 / 网络），每列展示 Utilization / Saturation / Errors
- **服务 Dashboard**: RED 方法组织，每行一个服务，每列展示 Rate / Errors / Duration
- **SRE Dashboard**: Four Golden Signals，全局视角展示延迟、流量、错误、饱和度
- **业务 Dashboard**: 按用户旅程组织（登录 → 搜索 → 下单 → 支付 → 完成），展示业务级 SLI

### MonitoringIntegrator 类

```python
import enum
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


class AlertSeverity(enum.Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


@dataclass
class SLI:
    """服务级别指标定义"""
    name: str
    description: str
    numerator_metric: str
    denominator_metric: str
    target_ratio: float  # e.g. 0.999 for 99.9%


@dataclass
class SLO:
    """服务级别目标"""
    sli: SLI
    target: float        # e.g. 0.999
    window: str          # e.g. "30d"
    error_budget: float  # computed: (1 - target) * window_seconds
    consumed: float = 0.0


@dataclass
class AlertRule:
    """告警规则"""
    name: str
    metric: str
    condition: str       # e.g. "> 0.01"
    duration: str        # e.g. "5m"
    severity: AlertSeverity
    channel: str
    runbook_url: str = ""


@dataclass
class DashboardPanel:
    """仪表盘面板"""
    title: str
    metric: str
    panel_type: str  # "graph" / "stat" / "table"
    query: str


@dataclass
class TracingConfig:
    """链路追踪配置"""
    sampling_rate: float = 0.1          # 生产环境 10% 固定采样
    error_sampling_rate: float = 1.0    # 错误 100% 采样
    exporter_endpoint: str = "http://otel-collector:4318"
    service_name: str = ""


class MonitoringIntegrator:
    """监控集成器，支持 SLI 定义、Dashboard 创建、告警配置和链路追踪设置"""

    def __init__(self, service_name: str):
        self.service_name = service_name
        self.slis: List[SLI] = []
        self.slos: List[SLO] = []
        self.alert_rules: List[AlertRule] = []
        self.dashboards: Dict[str, List[DashboardPanel]] = {}
        self.tracing: Optional[TracingConfig] = None

    def define_sli(self, name: str, description: str, numerator: str,
                   denominator: str, target_ratio: float) -> SLI:
        """定义服务级别指标 (SLI)"""
        sli = SLI(
            name=name,
            description=description,
            numerator_metric=numerator,
            denominator_metric=denominator,
            target_ratio=target_ratio,
        )
        self.slis.append(sli)
        return sli

    def create_slo(self, sli: SLI, target: float, window: str) -> SLO:
        """基于 SLI 创建服务级别目标 (SLO) 并计算 Error Budget"""
        window_seconds = self._parse_window(window)
        error_budget = (1.0 - target) * window_seconds
        slo = SLO(
            sli=sli,
            target=target,
            window=window,
            error_budget=error_budget,
        )
        self.slos.append(slo)
        return slo

    def create_dashboard(self, name: str, panels: List[DashboardPanel]) -> str:
        """创建 Grafana Dashboard，返回 dashboard JSON UID"""
        dashboard = {
            "title": name,
            "panels": [self._build_panel(p) for p in panels],
            "time": {"from": "now-6h", "to": "now"},
        }
        self.dashboards[name] = panels
        # 实际场景调用 Grafana API 创建 Dashboard
        import json
        dashboard_json = json.dumps(dashboard, indent=2)
        print(f"Dashboard '{name}' created with {len(panels)} panels.")
        return name  # placeholder for UID

    def configure_alert(self, name: str, metric: str, condition: str,
                        duration: str, severity: AlertSeverity,
                        channel: str) -> AlertRule:
        """配置告警规则，包含 Runbook 链接"""
        rule = AlertRule(
            name=name,
            metric=metric,
            condition=condition,
            duration=duration,
            severity=severity,
            channel=channel,
            runbook_url=f"https://runbooks.internal/{self.service_name}/{name}",
        )
        self.alert_rules.append(rule)
        return rule

    def setup_tracing(self, sampling_rate: float = 0.1,
                      error_sampling_rate: float = 1.0) -> TracingConfig:
        """配置 OpenTelemetry 分布式追踪"""
        config = TracingConfig(
            sampling_rate=sampling_rate,
            error_sampling_rate=error_sampling_rate,
            service_name=self.service_name,
        )
        self.tracing = config
        print(f"Tracing configured for '{self.service_name}': "
              f"sampling_rate={sampling_rate}, "
              f"error_sampling_rate={error_sampling_rate}")
        return config

    def _parse_window(self, window: str) -> int:
        """解析时间窗口字符串为秒数"""
        units = {"d": 86400, "h": 3600, "m": 60, "s": 1}
        import re
        match = re.match(r"^(\d+)([dhms])$", window)
        if match:
            return int(match.group(1)) * units[match.group(2)]
        return 2592000  # 默认 30 天

    def _build_panel(self, panel: DashboardPanel) -> Dict[str, Any]:
        """构建 Dashboard 面板定义"""
        return {
            "title": panel.title,
            "type": panel.panel_type,
            "targets": [{"expr": panel.query, "legendFormat": "{{service}}"}],
        }
```

### 可观测性三大支柱（传统定义）

```python
class ObservabilitySkill:
    """可观测性技能"""

    def __init__(self):
        self.three_pillars = {
            "metrics": {
                "description": "指标 - 聚合的数值数据",
                "tools": ["Prometheus", "Datadog"],
                "types": ["Counter", "Gauge", "Histogram"]
            },
            "logs": {
                "description": "日志 - 事件的时间序列",
                "tools": ["ELK", "Loki", "Splunk"],
                "formats": ["JSON", "Plain Text"]
            },
            "traces": {
                "description": "链路 - 请求的完整路径",
                "tools": ["Jaeger", "Zipkin", "Tempo"],
                "concepts": ["Span", "Trace", "Context Propagation"]
            }
        }

    def implement_metrics(self, service):
        """
        实现指标监控
        """
        # 1. 选择采集方式
        # 2. 定义指标
        # 3. 配置导出

    def implement_tracing(self, service):
        """
        实现链路追踪
        """
        # 1. 集成 SDK
        # 2. 配置采样
        # 3. 配置导出
```

## Associated Assets

- **Scenario**: `../../scenarios/integrate-monitor/SCENARIO.md`
- **Instruction**: `../../instructions/integrate-monitor.instructions.md`
- **Prompt**: `../../prompts/integrate-monitor.prompt.md`
- **Agent**: `../../agents/integrate-monitor.agent.md`

## Best Practices

> 监控集成的最佳实践，确保可观测性平台有效、高效、可持续。

1. **USE + RED 双维度监控**：基础设施层使用 USE 方法论（Utilization / Saturation / Errors），服务层使用 RED 方法论（Rate / Errors / Duration）。每个服务必须暴露 ≥4 个核心指标——请求速率、错误率、P95 延迟（或 P99）、饱和度。Dashboard 按 USE/RED 维度组织，确保运维人员能够在 30 秒内完成健康评估

2. **SLO 驱动的告警策略**：定义关键用户旅程的 SLI（如 "支付成功率" = 成功支付次数 / 发起支付次数），设置 SLO（如 ≥99.9% / 月），基于 Error Budget 燃尽速率触发告警（而非简单的静态阈值）。区分告警（需人工干预）和通知（仅记录），告警疲劳度目标 ≤5 次 / 周，每条告警必须附带 Runbook 链接

3. **分布式追踪全覆盖**：所有服务间调用集成 OpenTelemetry SDK，采样策略——生产环境 10% 固定采样 + 100% 错误采样，开发环境 100% 采样。Span 至少包含 service.name / trace.id / span.id / parent.span.id / duration / status 六个属性，确保跨服务调用链可完整还原

## Common Pitfalls

> 监控集成中常见错误及其防范措施。

### Pitfall 1: 告警疲劳

**Risk**: 配置过多低价值告警（如 CPU > 50%、磁盘使用率 > 60%），运维团队每天收到 ≥50 条告警，真正 P0 告警被淹没在噪音中。团队成员对告警逐渐脱敏，PagerDuty 告警被忽略或确认后不处理。

**Prevention**: 每条告警必须满足三个条件——可操作（有人能实际处理）、有 Runbook 链接（写明处理步骤和预期）、有明确的严重等级标签（P0/P1/P2/P3）。非可操作告警转为 Dashboard 监控指标而非告警，设置告警疲劳度目标 ≤5 次 / 周。

**Impact**: MTTR (Mean Time to Resolve) 大幅增加（从 15min 延长至数小时），真实故障被延迟发现，团队对告警系统失去信任，最终导致可观测性投资浪费。

### Pitfall 2: 指标收集无保留策略

**Risk**: 收集所有可用指标无差别存储，30 天内存储成本超过计算成本。Prometheus TSDB 或 Datadog 费用指数级增长，但 90% 以上的历史指标从未被查询。

**Prevention**: 实施指标分层保留——原始数据（raw）保留 7 天，1 分钟聚合保留 30 天，1 小时聚合保留 365 天。非关键指标（如开发环境指标、调试日志级别指标）不进入长期存储。定期审计指标使用率，清理无人使用的指标。

**Impact**: 可观测性平台成本失控，可能导致预算超支被迫降低采样率或缩短保留周期，反而丢失关键的故障复盘数据。

### Pitfall 3: 监控与业务脱节

**Risk**: 只监控技术指标（CPU / Memory / QPS），未监控业务指标（订单成功率 / 支付转化率 / 用户登录成功率）。技术指标全绿（服务器健康、延迟正常），但实际用户无法完成支付、无法登录，故障持续数小时才被发现。

**Prevention**: 每个服务定义 ≥2 个业务级 SLI（如 "订单创建成功率"、"搜索返回非空率"），技术告警与业务影响关联（如 "数据库延迟 > 500ms → 订单成功率预计下降至 <95%"，触发 P0 告警的升级流程）。

**Impact**: 技术指标全绿但用户投诉不断，故障发现靠用户反馈而非监控系统，严重违背可观测性的初衷。MTTD (Mean Time to Detect) 可能延长至数小时甚至数天。

## 相关资产

以下标准和评估清单与本技能直接相关，执行监控集成时应一并参考：

- [监控标准](../../standards/monitoring-standards.md) — 指标命名规范、采集配置标准、Dashboard 模板
- [告警指南](../../standards/alerting-guidelines.md) — 告警规则设计规范、通知路由矩阵、告警疲劳控制
- [SRE 最佳实践](../../standards/sre-best-practices.md) — SLO/SLI 定义框架、Error Budget 计算方法
- [监控质量检查清单](../../evaluations/monitoring-quality-checklist.md) — 监控覆盖面评估和告警质量审计
- [SLO 合规评估](../../evaluations/slo-compliance.md) — SLO 达成情况追踪和 Error Budget 消耗分析
