---
name: integrate-monitor
description: Detailed technical instructions for integrate-monitor scenario execution
type: instruction
version: "1.1.0"
stage: integrate-monitor
---

# Instructions: 监控集成 (Integrate Monitor)

## Overview

This instruction defines the comprehensive technical specifications for integrating observability and monitoring capabilities into systems across the E2E delivery lifecycle. It covers instrumentation strategies using OpenTelemetry, Prometheus, or cloud-native monitoring services; metric definition standards (naming, labeling, cardinality); alerting rule design with signal-to-noise optimization; and dashboard creation best practices. The instruction ensures systems are observable from day one, with actionable alerts, meaningful SLIs/SLOs, and comprehensive tracing for distributed systems.


## Monitoring Methodology

### RED 方法 (Rate, Errors, Duration)

适用于面向用户的服务：

```python
RED_METHOD = {
    "Rate": {
        "description": "每秒请求数",
        "unit": "req/s",
        "calculation": "rate(http_requests_total[5m])"
    },
    "Errors": {
        "description": "错误率",
        "unit": "percentage",
        "calculation": "rate(http_requests_total{status=~\"5..\"}[5m]) / rate(http_requests_total[5m]) * 100"
    },
    "Duration": {
        "description": "响应延迟",
        "unit": "milliseconds",
        "calculation": "histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) * 1000"
    }
}
```

### USE 方法 (Utilization, Saturation, Errors)

适用于系统资源：

```python
USE_METHOD = {
    "CPU": {
        "Utilization": "rate(node_cpu_seconds_total{mode!=\"idle\"}[5m])",
        "Saturation": "rate(node_cpu_seconds_total{mode=\"steal\"}[5m])"
    },
    "Memory": {
        "Utilization": "node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100",
        "Saturation": "rate(node_vmstat_pgscank[5m]) + rate(node_vmstat_pgscand[5m])"
    },
    "Disk": {
        "Utilization": "node_filesystem_usage_bytes / node_filesystem_size_bytes * 100",
        "Saturation": "rate(node_disk_io_time_seconds_total[5m])"
    },
    "Network": {
        "Utilization": "rate(node_network_receive_bytes_total[5m])",
        "Saturation": "rate(node_network_transmit_drop_total[5m])"
    }
}
```

## Prometheus 集成

### Python 应用埋点

```python
# prometheus_client 示例
from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry, push_to_gateway

# 创建 Registry
REGISTRY = CollectorRegistry()

# Counter: 累计计数
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status'],
    registry=REGISTRY
)

# Histogram: 分布统计
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5),
    registry=REGISTRY
)

# Gauge: 当前值
ACTIVE_CONNECTIONS = Gauge(
    'active_connections',
    'Number of active connections',
    ['service'],
    registry=REGISTRY
)

# 使用示例
@app.middleware
async def track_metrics(request, call_next):
    start_time = time.time()

    response = await call_next(request)

    # 记录请求
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    # 记录延迟
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(time.time() - start_time)

    return response
```

### Kubernetes 埋点

```yaml
# kubernetes-observability.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
      evaluation_interval: 15s

    scrape_configs:
      - job_name: 'kubernetes-pods'
        kubernetes_sd_configs:
          - role: pod
        relabel_configs:
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
            action: keep
            regex: true
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
            action: replace
            target_label: __metrics_path__
            regex: (.+)
          - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
            action: replace
            regex: ([^:]+)(?::\d+)?;(\d+)
            replacement: $1:$2
            target_label: __address__
          - action: labelmap
            regex: __meta_kubernetes_pod_label_(.+)
```

## Grafana Dashboard 配置

### Dashboard 结构

```json
{
  "dashboard": {
    "title": "服务监控面板",
    "panels": [
      {
        "title": "请求量 (QPS)",
        "type": "timeseries",
        "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} - {{endpoint}}"
          }
        ]
      },
      {
        "title": "错误率",
        "type": "gauge",
        "gridPos": {"x": 12, "y": 0, "w": 6, "h": 8},
        "targets": [
          {
            "expr": "rate(http_requests_total{status=~\"5..\"}[5m]) / rate(http_requests_total[5m]) * 100"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {"color": "green", "value": null},
                {"color": "yellow", "value": 1},
                {"color": "red", "value": 5}
              ]
            }
          }
        }
      },
      {
        "title": "延迟 P99",
        "type": "timeseries",
        "gridPos": {"x": 18, "y": 0, "w": 6, "h": 8},
        "targets": [
          {
            "expr": "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le)) * 1000"
          }
        ]
      }
    ]
  }
}
```

## Alert Configuration

### Prometheus Alert Rules

```yaml
# alertrules.yml
groups:
  - name: service_alerts
    rules:
      # 高错误率告警
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) /
          sum(rate(http_requests_total[5m])) > 0.01
        for: 5m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "服务错误率过高"
          description: "服务 {{ $labels.service }} 错误率超过 1%，当前值: {{ $value | printf \"%.2f\" }}%"

      # 高延迟告警
      - alert: HighLatency
        expr: |
          histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)) > 1
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "服务延迟过高"
          description: "服务 {{ $labels.service }} P99 延迟超过 1s，当前值: {{ $value | printf \"%.0f\" }}ms"

      # 服务宕机告警
      - alert: ServiceDown
        expr: up{job="services"} == 0
        for: 1m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "服务不可用"
          description: "服务 {{ $labels.instance }} 已宕机超过 1 分钟"

      # 资源告警
      - alert: HighCPUUsage
        expr: rate(node_cpu_seconds_total{mode!="idle"}[5m]) > 0.8
        for: 10m
        labels:
          severity: warning
          team: ops
        annotations:
          summary: "CPU 使用率过高"
          description: "节点 {{ $labels.instance }} CPU 使用率超过 80%"
```

### 告警路由配置

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'default-receiver'
  routes:
    # Critical 告警直接通知
    - match:
        severity: critical
      receiver: 'critical-receiver'
      group_wait: 10s
      repeat_interval: 1h

    # 按团队路由
    - match:
        team: platform
      receiver: 'platform-team'

    - match:
        team: ops
      receiver: 'ops-team'

receivers:
  - name: 'default-receiver'
    email_configs:
      - to: 'oncall@example.com'

  - name: 'critical-receiver'
    pagerduty_configs:
      - service_key: 'YOUR_SERVICE_KEY'
        severity: critical

  - name: 'platform-team'
    slack_configs:
      - api_url: 'YOUR_WEBHOOK_URL'
        channel: '#platform-alerts'

  - name: 'ops-team'
    slack_configs:
      - api_url: 'YOUR_WEBHOOK_URL'
        channel: '#ops-alerts'
```

## OpenTelemetry 链路追踪

### 链路追踪配置

```python
# otel_tracing.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource

# 配置 Tracer Provider
trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({
            "service.name": "my-service",
            "service.version": "1.0.0",
            "deployment.environment": "production"
        })
    )
)

# 配置 Jaeger Exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger-collector",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# 获取 Tracer
tracer = trace.get_tracer(__name__)

# 使用示例
@app.get("/api/users/{user_id}")
async def get_user(user_id: str):
    with tracer.start_as_current_span("get_user") as span:
        span.set_attribute("user.id", user_id)

        # 业务逻辑
        user = await fetch_user(user_id)

        span.set_attribute("user.found", user is not None)

        return user
```

## SLO 监控

### SLO 配置

```yaml
# slo.yaml
slos:
  - name: "api-availability"
    target: 99.9
    description: "API 可用性"
    indicator:
      type: availability
      good:
        total: http_requests_total
        good: http_requests_total{status!~"5.."}
      window: 30d

  - name: "api-latency"
    target: 99.0
    description: "API 延迟 P99 < 500ms"
    indicator:
      type: latency
      total: http_requests_total
      good: http_requests_total{le="0.5"}
      window: 30d

  - name: "error-budget"
    description: "错误预算"
    burn_rate_threshold: 14.4
    window: 1h
```

## Best Practices

### DO

1. **全面覆盖**: 基础设施、应用、业务三层监控
2. **告警分级**: Critical/Warning/Info 清晰分级
3. **保留周期**: 根据需求设置合理的保留周期
4. **采样策略**: 高流量场景使用采样
5. **告警收敛**: 避免告警风暴

### DON'T

1. **不要过度监控**: 只监控关键指标
2. **不要敏感告警**: 避免误报扰动
3. **不要硬编码**: 监控配置应可配置
4. **不要忽视性能**: 监控本身也有开销
5. **不要孤立**: 指标之间应有关联

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `../../scenarios/integrate-monitor/SCENARIO.md` |
| PROMPT | `../../prompts/integrate-monitor.prompt.md` |
| AGENT | `../../agents/integrate-monitor.agent.md` |
| SKILL | `../../skills/integrate-monitor/SKILL.md` |


## Technical Specifications

> Detailed technical requirements and implementation guidelines for integrate-monitor.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Error Handling

> Common error scenarios and resolution strategies for integrate-monitor.

### Error Category 1
**Symptom**: Monitoring integration fails or produces inconsistent metrics
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Instrumentation overhead exceeds acceptable performance impact
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for integrate-monitor deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Metric coverage for critical components is 90% or higher | Review dashboard completeness |
| Standard 2 | Instrumentation overhead is 5% or lower | Performance benchmark comparison |
| Standard 3 | Dashboard utilization is 70% or higher | Access analytics review |
