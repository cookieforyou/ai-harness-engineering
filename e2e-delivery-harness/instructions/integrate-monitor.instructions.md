---
name: integrate-monitor
description: "Detailed technical instructions for integrate-monitor scenario execution"
applyTo: "scenarios/integrate-monitor/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
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

## Multi-Language Code Examples

> Production-grade observability instrumentation and monitoring query examples covering PromQL, Grafana dashboards, and OpenTelemetry across Java, Go, and Node.js SDKs.

### PromQL Query Examples

```promql
// 1. 服务可用性 SLI - 最近 30 天滚动窗口
(
  sum(rate(http_requests_total{status!~"5.."}[30d]))
  /
  sum(rate(http_requests_total[30d]))
) * 100

// 2. P99 延迟趋势 - 按服务分组（用于 SLO 仪表盘）
histogram_quantile(0.99,
  sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)
) * 1000

// 3. 错误预算消耗速率 - 每小时消耗百分比
(
  (1 - (sum(rate(http_requests_total{status!~"5.."}[1h]))
        / sum(rate(http_requests_total[1h]))))
  /
  (1 - 0.999)
) * 100

// 4. 各实例资源使用率 Top 5
topk(5,
  avg by(instance) (rate(node_cpu_seconds_total{mode!="idle"}[5m]))
)

// 5. 熔断器状态 - 所有 OPEN 状态的熔断器
api_circuit_breaker_state{state="open"}

// 6. 慢追踪占比 - 延迟超过 1s 的请求比例
(
  sum(rate(http_request_duration_seconds_bucket{le="1.0"}[5m]))
  / on()
  sum(rate(http_request_duration_seconds_count[5m]))
)

// 7. 错误预算剩余 - 多窗口 burn rate 检测
(
  1 - (1 - (
    sum(rate(http_requests_total{status=~"5.."}[1h]))
    /
    sum(rate(http_requests_total[1h]))
  )) / (1 - 0.99)
) * 100
```

### Grafana Dashboard JSON

```json
{
  "dashboard": {
    "title": "Service Monitoring",
    "tags": ["production", "service", "slo"],
    "timezone": "browser",
    "panels": [
      {
        "title": "RPS by Service",
        "type": "timeseries",
        "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8},
        "targets": [{
          "expr": "sum(rate(http_requests_total[5m])) by (service)",
          "legendFormat": "{{service}}"
        }],
        "fieldConfig": {
          "defaults": { "unit": "reqps", "custom": { "lineWidth": 1 } }
        }
      },
      {
        "title": "Error Rate (%)",
        "type": "timeseries",
        "gridPos": {"x": 12, "y": 0, "w": 6, "h": 8},
        "targets": [{
          "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) by (service) / sum(rate(http_requests_total[5m])) by (service) * 100",
          "legendFormat": "{{service}}"
        }],
        "fieldConfig": {
          "defaults": {
            "unit": "percent",
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
        "title": "Latency P99 / P95 / P50",
        "type": "timeseries",
        "gridPos": {"x": 18, "y": 0, "w": 6, "h": 8},
        "targets": [
          {"expr": "histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le)) * 1000", "legendFormat": "P99"},
          {"expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le)) * 1000", "legendFormat": "P95"},
          {"expr": "histogram_quantile(0.50, sum(rate(http_request_duration_seconds_bucket[5m])) by (le)) * 1000", "legendFormat": "P50"}
        ]
      },
      {
        "title": "Error Budget (30d)",
        "type": "gauge",
        "gridPos": {"x": 0, "y": 8, "w": 6, "h": 6},
        "targets": [{
          "expr": "(1 - (sum(rate(http_requests_total{status=~\"5..\"}[30d])) / sum(rate(http_requests_total[30d])))) / (1 - 0.99) * 100"
        }],
        "fieldConfig": {
          "defaults": {
            "unit": "percent",
            "min": 0, "max": 100,
            "thresholds": {
              "mode": "absolute",
              "steps": [
                {"color": "green", "value": null},
                {"color": "yellow", "value": 50},
                {"color": "red", "value": 20}
              ]
            }
          }
        }
      },
      {
        "title": "Active Alerts by Severity",
        "type": "stat",
        "gridPos": {"x": 6, "y": 8, "w": 6, "h": 6},
        "targets": [{
          "expr": "count(ALERTS{alertstate=\"firing\"}) by (severity)",
          "legendFormat": "{{severity}}"
        }]
      },
      {
        "title": "CPU Usage by Node",
        "type": "bargauge",
        "gridPos": {"x": 12, "y": 8, "w": 6, "h": 6},
        "targets": [{
          "expr": "avg(rate(node_cpu_seconds_total{mode!=\"idle\"}[5m])) by (instance) * 100",
          "legendFormat": "{{instance}}"
        }]
      },
      {
        "title": "Circuit Breaker State",
        "type": "state-timeline",
        "gridPos": {"x": 18, "y": 8, "w": 6, "h": 6},
        "targets": [{
          "expr": "api_circuit_breaker_state",
          "legendFormat": "{{provider}}"
        }]
      }
    ]
  }
}
```

### OpenTelemetry Java SDK (Spring Boot Auto-Instrumentation)

```java
// OpenTelemetry Java SDK - Spring Boot Auto-Instrumentation
//
// build.gradle 依赖:
//   implementation 'io.opentelemetry:opentelemetry-api:1.31.0'
//   implementation 'io.opentelemetry:opentelemetry-sdk:1.31.0'
//   implementation 'io.opentelemetry:opentelemetry-exporter-otlp:1.31.0'
//   implementation 'io.opentelemetry:opentelemetry-sdk-extension-autoconfigure:1.31.0'
//
// JVM 启动参数（零代码侵入）:
//   -javaagent:opentelemetry-javaagent.jar
//   -Dotel.service.name=order-service
//   -Dotel.traces.exporter=otlp
//   -Dotel.metrics.exporter=otlp
//   -Dotel.logs.exporter=otlp
//   -Dotel.exporter.otlp.endpoint=http://otel-collector:4317

import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.api.trace.StatusCode;
import io.opentelemetry.context.Scope;
import io.opentelemetry.api.metrics.LongHistogram;
import io.opentelemetry.api.common.Attributes;
import io.opentelemetry.api.common.AttributeKey;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
@RequestMapping("/api/orders")
public class OrderController {

    @Autowired
    private OpenTelemetry openTelemetry;

    private final Tracer tracer;
    private final LongHistogram orderAmountHistogram;

    public OrderController(OpenTelemetry openTelemetry) {
        this.tracer = openTelemetry.getTracer(
            OrderController.class.getName());
        // 自定义业务指标：订单金额分布
        this.orderAmountHistogram = openTelemetry
            .getMeter("order-service")
            .histogramBuilder("order.amount")
            .setDescription("Order amount distribution")
            .setUnit("CNY")
            .build();
    }

    @PostMapping
    public Order createOrder(@RequestBody CreateOrderRequest request) {
        // 创建自定义 Span 追踪订单创建流程
        Span span = tracer.spanBuilder("createOrder")
            .setAttribute("user.id", request.getUserId())
            .setAttribute("order.items.count",
                          request.getItems().size())
            .startSpan();

        try (Scope scope = span.makeCurrent()) {
            Order order = processOrder(request);

            // 设置 Span 业务属性
            span.setAttribute("order.id", order.getId());
            span.setAttribute("order.amount",
                              order.getTotalAmount());
            span.setStatus(StatusCode.OK);

            // 记录业务指标
            orderAmountHistogram.record(
                (long) order.getTotalAmount(),
                Attributes.of(
                    AttributeKey.stringKey("currency"), "CNY",
                    AttributeKey.stringKey("order.type"),
                    request.getType()
                )
            );

            return order;
        } catch (Exception e) {
            span.setStatus(StatusCode.ERROR,
                           "Failed to create order");
            span.recordException(e);
            throw e;
        } finally {
            span.end();
        }
    }
}
```

### OpenTelemetry Go SDK (Manual Instrumentation)

```go
// OpenTelemetry Go SDK - Manual Instrumentation
package main

import (
	"context"
	"log"
	"net/http"
	"time"

	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
	"go.opentelemetry.io/otel"
	"go.opentelemetry.io/otel/attribute"
	"go.opentelemetry.io/otel/codes"
	"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
	"go.opentelemetry.io/otel/sdk/resource"
	sdktrace "go.opentelemetry.io/otel/sdk/trace"
	semconv "go.opentelemetry.io/otel/semconv/v1.21.0"
	"go.opentelemetry.io/otel/trace"
)

// initTracer 初始化 OTLP gRPC Exporter
func initTracer() (*sdktrace.TracerProvider, error) {
	ctx := context.Background()
	exporter, err := otlptracegrpc.New(ctx,
		otlptracegrpc.WithEndpoint("otel-collector:4317"),
		otlptracegrpc.WithInsecure(),
	)
	if err != nil {
		return nil, err
	}

	res := resource.NewWithAttributes(
		semconv.SchemaURL,
		semconv.ServiceName("payment-service"),
		semconv.ServiceVersion("1.0.0"),
		attribute.String("deployment.environment", "production"),
	)

	tp := sdktrace.NewTracerProvider(
		sdktrace.WithBatcher(exporter),
		sdktrace.WithResource(res),
		// 采样策略：高流量服务使用 10% 采样
		sdktrace.WithSampler(sdktrace.TraceIDRatioBased(0.1)),
	)

	otel.SetTracerProvider(tp)
	return tp, nil
}

// PaymentHandler 带链路追踪的 HTTP Handler
func PaymentHandler(w http.ResponseWriter, r *http.Request) {
	tracer := otel.Tracer("payment-service")
	ctx := r.Context()

	// 创建业务 Span，携带支付属性
	ctx, span := tracer.Start(ctx, "processPayment",
		trace.WithAttributes(
			attribute.String("payment.method",
				r.URL.Query().Get("method")),
			attribute.Float64("payment.amount",
				parseAmount(r)),
		),
	)
	defer span.End()

	// 调用下游服务（自动传播 Trace Context）
	paymentResult, err := callPaymentGateway(ctx)
	if err != nil {
		span.SetStatus(codes.Error, err.Error())
		span.RecordError(err)
		http.Error(w, err.Error(),
			http.StatusInternalServerError)
		return
	}

	span.SetAttributes(
		attribute.String("payment.id",
			paymentResult.TransactionID),
		attribute.String("payment.status",
			paymentResult.Status),
	)
	span.SetStatus(codes.Ok, "payment processed successfully")
	w.Write([]byte(`{"status":"ok"}`))
}

func main() {
	tp, err := initTracer()
	if err != nil {
		log.Fatal(err)
	}
	defer tp.Shutdown(context.Background())

	// 使用 otelhttp 自动包装 HTTP Handler
	handler := otelhttp.NewHandler(
		http.HandlerFunc(PaymentHandler),
		"payment",
		otelhttp.WithSpanNameFormatter(
			func(operation string, r *http.Request) string {
				return r.Method + " " + r.URL.Path
			}),
	)

	http.Handle("/api/payments", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
```

### OpenTelemetry JS/Node.js SDK (Express Middleware)

```javascript
// OpenTelemetry JS/Node.js SDK - Express Middleware Integration
const { NodeSDK } = require('@opentelemetry/sdk-node');
const {
  getNodeAutoInstrumentations,
} = require('@opentelemetry/auto-instrumentations-node');
const {
  OTLPTraceExporter,
} = require('@opentelemetry/exporter-trace-otlp-grpc');
const {
  OTLPMetricExporter,
} = require('@opentelemetry/exporter-metrics-otlp-grpc');
const {
  PeriodicExportingMetricReader,
} = require('@opentelemetry/sdk-metrics');
const { Resource } = require('@opentelemetry/resources');
const {
  SemanticResourceAttributes,
} = require('@opentelemetry/semantic-conventions');

// 初始化 OTel SDK（在应用入口文件最顶部调用）
const otelSDK = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'user-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: '2.1.0',
    'deployment.environment': 'staging',
  }),
  traceExporter: new OTLPTraceExporter({
    url: 'http://otel-collector:4317',
  }),
  metricReader: new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({
      url: 'http://otel-collector:4317',
    }),
    exportIntervalMillis: 60000, // 每分钟导出一次
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      // 选择性启用埋点，降低性能开销
      '@opentelemetry/instrumentation-fs': { enabled: false },
      '@opentelemetry/instrumentation-net': { enabled: false },
      '@opentelemetry/instrumentation-dns': { enabled: false },
    }),
  ],
});

otelSDK.start();

// ---- Express 应用集成 ----
const express = require('express');
const {
  trace,
  context,
  SpanStatusCode,
} = require('@opentelemetry/api');

const app = express();
const tracer = trace.getTracer('user-service');

// 自定义业务埋点中间件
app.post('/api/users', express.json(), async (req, res) => {
  // 创建自定义 Span 追踪用户创建流程
  const span = tracer.startSpan('createUser', {
    attributes: {
      'user.email': req.body.email,
      'user.role': req.body.role || 'viewer',
    },
  });

  // 将 Span 注入当前 Context
  const ctx = trace.setSpan(context.active(), span);
  await context.with(ctx, async () => {
    try {
      const user = await createUser(req.body);

      // 添加业务属性
      span.setAttribute('user.id', user.id);
      span.setStatus({ code: SpanStatusCode.OK });

      res.status(201).json(user);
    } catch (err) {
      span.setStatus({
        code: SpanStatusCode.ERROR,
        message: err.message,
      });
      span.recordException(err);
      res.status(500).json({ error: 'Failed to create user' });
    } finally {
      span.end();
    }
  });
});

// 带追踪的健康检查端点
app.get('/health', (req, res) => {
  const span = tracer.startSpan('healthCheck');
  span.setAttribute('http.method', 'GET');
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
  span.end();
});
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

> 监控集成过程中的异常处理策略与自动恢复流程，涵盖告警风暴抑制、指标采集中断、日志管道阻塞三大核心场景。

### Error Scenario 1: 告警风暴抑制 (P1)

**触发条件**: 同一时间窗口内（5 分钟）告警数量超过 100 条，或同一种告警的重复率超过 80%

**处理流程**:
```
IF alert_count > 100 IN 5m
   OR duplicate_alert_rate > 80%
THEN
  1. 触发告警风暴检测机制，将新到达的告警归入风暴分组
  2. 对所有非 Critical 级别告警执行静默（Silence）操作，静默时间 30 分钟
  3. 对 Critical 告警执行聚合（Grouping），按根因标签（service、error_code）压缩为一条聚合告警
  4. 发送告警风暴通知，附带聚合摘要和受影响的服务列表
  5. 启动告警降噪分析，识别根本原因并自动生成事件工单
END
```

**降级方案**: 暂停非关键告警的通知通道（Slack、Email）；启用告警聚合发送（5 分钟合并一次）；将告警风暴信息自动写入事件管理平台（PagerDuty / OpsGenie）

**升级条件**: 告警风暴持续超过 15 分钟或涉及 Critical 级别服务超过 3 个，升级为 P0 事件，启动 War Room 应急响应

### Error Scenario 2: 指标采集中断 (P1)

**触发条件**: Prometheus 对某个 Target 的 Scrape 连续 3 次失败，或活跃 Time Series 数量在 5 分钟内下降超过 50%

**处理流程**:
```
IF scrape_failure_count >= 3
   OR active_time_series_drop > 50% IN 5m
THEN
  1. 检查 Target 服务健康状态（调用 /health 端点）
  2. 检查 Prometheus 与 Target 之间的网络连通性（ping / traceroute）
  3. 检查 Target 的 Metrics 端点（/metrics）是否正常响应 HTTP 200
  4. 如果 Target 正常但 Scrape 失败，重启 Prometheus Scrape 循环
  5. 如果 Target 异常，触发服务恢复流程（重新调度 Pod 或重启进程）
END
```

**降级方案**: 使用 Prometheus 本地存储的缓存数据填补短时间数据缺口；临时延长 Scrape Interval（从 15s 调整为 30s）降低采集压力；切换到备用监控系统（CloudWatch / Datadog）临时替代

**升级条件**: 指标采集中断超过 10 分钟或影响 SLO 监控面板的数据完整性，升级为 P0 事件，启动监控系统容灾

### Error Scenario 3: 日志管道阻塞 (P2)

**触发条件**: 日志生产者（Fluent Bit / Filebeat）上报队列积压超过 10000 条，或日志消费者（Elasticsearch / Loki）写入延迟超过 30 秒

**处理流程**:
```
IF log_queue_backlog > 10000
   OR log_write_latency > 30s
THEN
  1. 触发日志管道反压机制，通知生产者降低日志输出速率
  2. 对 DEBUG 和 INFO 级别日志执行降级采样（采样率降至 10%）
  3. 保留 WARN 和 ERROR 级别日志的完整记录
  4. 检查下游存储系统（Elasticsearch / Loki）的健康状态和磁盘使用率
  5. 如果存储系统不可用，将日志临时切换到本地文件缓冲（最大 1GB 轮转）
END
```

**降级方案**: 非关键日志直接丢弃（DEBUG、TRACE 级别）；开启日志缓冲队列（最大 500MB）；临时关闭非核心服务的日志采集

**升级条件**: 日志管道阻塞持续超过 30 分钟或 WARN / ERROR 级别日志也开始丢失，升级为 P1 事件，触发日志系统扩容


## Quality Standards

> Acceptance criteria and quality gates for integrate-monitor deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Metric coverage for critical components is 90% or higher | Review dashboard completeness |
| Standard 2 | Instrumentation overhead is 5% or lower | Performance benchmark comparison |
| Standard 3 | Dashboard utilization is 70% or higher | Access analytics review |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
