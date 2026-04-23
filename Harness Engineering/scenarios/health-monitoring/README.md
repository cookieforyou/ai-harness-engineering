# 健康监控场景 / Health Monitoring Scenario

> **阶段**: P6 — 健康监控
> **核心 Agent**: `agents/devops-engineer`
> **目标输出**: 可观测性方案（监控指标、告警规则、健康检查、仪表盘、Oncall 手册）
> **效力等级**: P0（强制）

---

## 场景概述

本场景基于 P5 阶段部署上线的服务，设计完整的可观测性方案。输出物包含核心监控指标、告警规则、健康检查端点、Grafana 仪表盘布局及 Oncall 响应手册，确保服务持续健康运行，并将监控数据作为反馈输入 P1，形成持续改进闭环。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `service_name` | `string` | 是 | 服务名称 |
| `tech_stack` | `string` | 是 | 技术栈 |
| `slo` | `string` | 是 | 服务级别目标（可用性、延迟、错误率） |
| `alert_channels` | `string` | 否 | 告警渠道（slack, pagerduty, email） |
| `existing_monitoring` | `string` | 否 | 现有监控体系（如 Prometheus, Datadog） |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "monitoring_spec": {
    "service_name": "...",
    "slo": {
      "availability": 0.999,
      "latency_p99_ms": 200,
      "error_rate": 0.001
    },
    "metrics": [
      {
        "name": "http_requests_total",
        "type": "counter",
        "description": "HTTP 请求总数",
        "labels": ["method", "status", "path"]
      }
    ],
    "alert_rules": [
      {
        "name": "HighErrorRate",
        "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) > 0.01",
        "severity": "critical",
        "for": "2m",
        "annotations": {
          "summary": "服务 {{service_name}} 错误率过高",
          "description": "5 分钟内错误率超过 1%"
        }
      }
    ],
    "health_checks": [
      {
        "name": "readiness",
        "endpoint": "/health/ready",
        "expected_status": 200,
        "timeout_seconds": 5
      }
    ],
    "dashboards": [
      {
        "title": "服务概览",
        "panels": [
          { "title": "QPS", "query": "sum(rate(http_requests_total[1m]))" }
        ]
      }
    ],
    "runbook": [
      {
        "alert_name": "HighErrorRate",
        "steps": [
          "1. 检查近期部署记录",
          "2. 查看错误日志分布",
          "3. 若确认是部署引入，执行回滚"
        ],
        "escalation": "5 分钟内未恢复则联系架构师"
      }
    ]
  }
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **DevOps Engineer (SRE)** | 监控指标设计、告警规则生成、仪表盘布局、Oncall 手册编写 | 可观测性方案 JSON |
| **人类 SRE 负责人** | 审阅告警阈值合理性、确认 Oncall 升级路径、批准监控上线 | 已批准的监控方案 |

---

## 质量检查要点

- [ ] 所有告警包含 `for` 持续时间，避免瞬时抖动导致误报
- [ ] Critical 级别告警附带明确的升级路径与责任人
- [ ] 仪表盘设计遵循「5 秒原则」：核心指标应在 5 秒内定位问题
- [ ] 告警规则定义抑制条件（如维护窗口、已知故障期间）
- [ ] 业务指标定义已与产品经理确认（如订单转化率、支付成功率）
- [ ] 输出通过 `evaluations/monitoring-checkpoint.yaml` 质量门禁

---

## 上游衔接

接收 `scenarios/deployment-pipeline/` 的输出（部署清单中的健康检查端点与 SLO）。
衔接规范详见 `standards/scenario-integration.md#P5→P6`。

## 下游衔接（反馈闭环）

本场景产生的以下数据应作为 `scenarios/requirements-analysis/` 的输入：

- **性能瓶颈报告** → 转化为非功能性需求优化项
- **错误模式分析** → 转化为可靠性需求或验收标准补充
- **用户行为监控** → 转化为新功能需求或现有功能改进

衔接规范详见 `standards/scenario-integration.md#P6→P1`。
