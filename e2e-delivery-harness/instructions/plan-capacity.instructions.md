---
name: plan-capacity
description: "Detailed technical instructions for plan-capacity scenario execution"
applyTo: "scenarios/plan-capacity/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instruction: 容量规划技术规范

## Overview

This instruction defines the technical methodology and standards for capacity planning across infrastructure, compute, storage, and team resources. It covers workload forecasting models, demand-based scaling strategies, cost-performance optimization, and procurement readiness planning. The instruction ensures systems maintain adequate headroom for growth while avoiding over-provisioning waste. Key focus areas include seasonal pattern analysis, autoscaling policy design, multi-region capacity distribution, and integration with financial planning cycles.


## Capacity Assessment Methods

### 指标采集
- CPU 利用率
- 内存利用率
- 存储利用率
- 网络带宽
- TPS/QPS

### 扩容策略

| 策略 | 适用场景 | 成本 |
|------|----------|------|
| 垂直扩展 | 小规模 | 中 |
| 水平扩展 | 大规模 | 中高 |
| 混合扩展 | 复杂系统 | 高 |

## Associated Assets

- **Scenario**: `scenarios/plan-capacity/SCENARIO.md`
- **Prompt**: `prompts/plan-capacity.prompt.md`
- **Agent**: `agents/plan-capacity.agent.md`
- **Skill**: `skills/plan-capacity/SKILL.md`


## Technical Specifications

> Detailed technical requirements and implementation guidelines for plan-capacity.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for plan-capacity execution.

1. **Practice 1**: Forecast growth based on historical trends and business plans
2. **Practice 2**: Model peak load scenarios including seasonal spikes
3. **Practice 3**: Plan capacity with headroom for unexpected growth


## Multi-Language Code Examples

### Python - Prometheus API Query and Trend Prediction

```python
#!/usr/bin/env python3
"""
Prometheus 容量分析工具 - 查询集群资源使用趋势并进行预测

功能:
  1. 从 Prometheus 查询 CPU/内存/存储历史数据
  2. 使用线性回归预测未来 30 天资源需求
  3. 生成容量报告（当前使用率、增长趋势、预计达到阈值的时间）

Requires: pip install requests pandas numpy scikit-learn
"""
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import requests
from sklearn.linear_model import LinearRegression

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")
CAPACITY_WARNING_THRESHOLD = 0.80  # 80% 告警阈值
CAPACITY_CRITICAL_THRESHOLD = 0.90  # 90% 严重阈值


class PrometheusCapacityAnalyzer:
    """
    Prometheus 容量分析器 - 预测基础设施资源需求趋势。

    基于历史监控数据，使用线性回归预测资源使用增长趋势，
    估算资源耗尽时间点，为容量规划提供数据支撑。
    """

    def __init__(self, prometheus_url: str):
        self.base_url = prometheus_url.rstrip("/")

    def query_range(self, query: str, start: datetime, end: datetime,
                    step: str = "1h") -> List[Dict]:
        """
        查询 Prometheus 时间序列数据 (Range Query)。

        Args:
            query: PromQL 查询语句
            start: 查询开始时间
            end: 查询结束时间
            step: 数据点间隔 (e.g., "1h", "5m", "1d")
        """
        params = {
            "query": query,
            "start": start.timestamp(),
            "end": end.timestamp(),
            "step": step,
        }
        resp = requests.get(
            f"{self.base_url}/api/v1/query_range",
            params=params,
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        if data["status"] != "success":
            raise RuntimeError(f"Prometheus query failed: {data}")
        return data["data"]["result"]

    def get_cpu_utilization(self, days: int = 30) -> pd.DataFrame:
        """
        获取集群 CPU 利用率历史数据（过去 N 天）。

        使用 PromQL 聚合所有节点 CPU 使用率的平均值。
        """
        end = datetime.now()
        start = end - timedelta(days=days)
        query = 'avg(node_cpu_seconds_total{mode!="idle"}) by (instance)'
        results = self.query_range(query, start, end, step="1h")

        records = []
        for result in results:
            instance = result["metric"].get("instance", "unknown")
            for timestamp, value in result["values"]:
                records.append({
                    "timestamp": pd.to_datetime(timestamp, unit="s"),
                    "instance": instance,
                    "value": float(value),
                })

        df = pd.DataFrame(records)
        if not df.empty:
            df = df.sort_values("timestamp")
        return df

    def get_memory_utilization(self, days: int = 30) -> pd.DataFrame:
        """获取集群内存利用率。"""
        end = datetime.now()
        start = end - timedelta(days=days)
        query = "100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)"
        results = self.query_range(query, start, end, step="1h")

        records = []
        for result in results:
            instance = result["metric"].get("instance", "unknown")
            for timestamp, value in result["values"]:
                records.append({
                    "timestamp": pd.to_datetime(timestamp, unit="s"),
                    "instance": instance,
                    "value": float(value),
                })

        df = pd.DataFrame(records)
        if not df.empty:
            df = df.sort_values("timestamp")
        return df

    def predict_capacity(self, df: pd.DataFrame,
                         forecast_days: int = 30,
                         target_usage: float = 0.90) -> Dict:
        """
        基于历史数据预测容量趋势。

        使用线性回归建模资源使用增长趋势，预测达到目标使用率的时间。

        Args:
            df: 包含 timestamp 和 value 列的历史数据 DataFrame
            forecast_days: 预测未来天数
            target_usage: 目标使用率 (e.g., 0.90 = 90%)

        Returns:
            预测报告，包含当前使用率、增长率、预计耗尽时间等信息
        """
        if df.empty:
            return {"error": "No historical data available for prediction",
                    "forecast_available": False}

        # 按天聚合取日均值
        df["date"] = df["timestamp"].dt.date
        daily_avg = df.groupby("date")["value"].agg(["mean", "max", "min"]).reset_index()
        daily_avg.columns = ["date", "avg_usage", "max_usage", "min_usage"]

        # 准备回归数据
        daily_avg["days_from_start"] = (pd.to_datetime(daily_avg["date"]) - pd.to_datetime(daily_avg["date"].min())).dt.days

        X = daily_avg["days_from_start"].values.reshape(-1, 1)
        y = daily_avg["avg_usage"].values

        # 线性回归
        model = LinearRegression()
        model.fit(X, y)

        # 预测未来趋势
        last_day = daily_avg["days_from_start"].max()
        future_days = np.arange(last_day + 1, last_day + forecast_days + 1).reshape(-1, 1)
        predictions = model.predict(future_days)

        # 计算当前状态
        current_usage = daily_avg["avg_usage"].iloc[-1]
        growth_rate = model.coef_[0]  # 每日增长率
        growth_rate_pct = growth_rate / current_usage * 100 if current_usage > 0 else 0

        # 估算达到目标使用率的时间
        days_to_target = None
        if growth_rate > 0:
            remaining = target_usage * 100 - current_usage
            if remaining > 0:
                days_to_target = remaining / growth_rate if growth_rate > 0 else None

        # 计算 R² 评估预测置信度
        r2_score = model.score(X, y)

        return {
            "forecast_available": True,
            "current_usage_pct": round(current_usage, 2),
            "peak_usage_pct": round(daily_avg["max_usage"].max(), 2),
            "growth_rate_per_day": round(growth_rate, 4),
            "growth_rate_pct_per_month": round(growth_rate_pct * 30, 2),
            "days_until_critical": round(days_to_target) if days_to_target else None,
            "critical_threshold_pct": target_usage * 100,
            "prediction_confidence": round(r2_score, 3),
            "historical_days": len(daily_avg),
            "next_30_days_peak": round(max(predictions), 2),
            "recommendation": self._generate_recommendation(
                current_usage, growth_rate_pct, days_to_target
            ),
        }

    def _generate_recommendation(self, current_usage: float,
                                  growth_rate_pct: float,
                                  days_to_critical: Optional[float]) -> str:
        """根据分析结果生成容量规划建议。"""
        recommendations = []
        if days_to_critical and days_to_critical < 30:
            recommendations.append("CRITICAL: 容量将在 30 天内耗尽，需要立即扩容！")
        elif days_to_critical and days_to_critical < 60:
            recommendations.append("WARNING: 容量将在 60 天内耗尽，建议 2 周内提交扩容申请")
        elif days_to_critical and days_to_critical < 90:
            recommendations.append("INFO: 容量将在 90 天内耗尽，纳入下期容量规划")
        else:
            recommendations.append("OK: 当前容量充足，继续监控")

        if growth_rate_pct > 10:
            recommendations.append("增长率 > 10%/月，建议优化资源使用效率")
        elif growth_rate_pct > 5:
            recommendations.append("增长率适中，按正常容量规划周期进行")
        else:
            recommendations.append("增长率稳定，保持现有容量规划节奏")

        return " | ".join(recommendations)


# 容量预测执行入口
def generate_capacity_report():
    """生成完整容量规划报告（所有集群维度）。"""
    analyzer = PrometheusCapacityAnalyzer(PROMETHEUS_URL)

    report = {
        "generated_at": datetime.now().isoformat(),
        "cluster": os.getenv("CLUSTER_NAME", "production"),
    }

    # CPU 分析
    print("Fetching CPU data (last 90 days)...")
    cpu_df = analyzer.get_cpu_utilization(days=90)
    report["cpu"] = analyzer.predict_capacity(cpu_df, forecast_days=30)

    # 内存分析
    print("Fetching memory data (last 90 days)...")
    mem_df = analyzer.get_memory_utilization(days=90)
    report["memory"] = analyzer.predict_capacity(mem_df, forecast_days=30)

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return report


if __name__ == "__main__":
    generate_capacity_report()
```

### SQL - 资源利用率聚合分析

```sql
-- ============================================================
-- capacity_analysis.sql
-- 基础设施容量分析 SQL 查询集
--
-- 适用数据库: PostgreSQL 15+ / TimescaleDB (时序数据)
-- 数据来源: 资源利用监控表 (来自 Prometheus/Telegraf 采集)
-- ============================================================

-- ============================================================
-- 1. 聚合视图: 每日资源使用统计 (过去 90 天)
-- ============================================================
CREATE OR REPLACE VIEW daily_resource_usage AS
SELECT
    date_trunc('day', timestamp) AS day,
    -- CPU 指标
    AVG(cpu_usage_pct) AS avg_cpu_pct,
    MAX(cpu_usage_pct) AS max_cpu_pct,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY cpu_usage_pct) AS p95_cpu_pct,

    -- 内存指标
    AVG(memory_usage_pct) AS avg_memory_pct,
    MAX(memory_usage_pct) AS max_memory_pct,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY memory_usage_pct) AS p95_memory_pct,

    -- 磁盘指标
    AVG(disk_usage_pct) AS avg_disk_pct,
    MAX(disk_usage_pct) AS max_disk_pct,

    -- 网络指标
    AVG(network_bytes_in) AS avg_network_in,
    AVG(network_bytes_out) AS avg_network_out,
    SUM(network_bytes_in + network_bytes_out) AS total_network_traffic,

    -- 数据点统计
    COUNT(*) AS sample_count

FROM resource_metrics
WHERE timestamp >= NOW() - INTERVAL '90 days'
GROUP BY date_trunc('day', timestamp)
ORDER BY day DESC;

-- ============================================================
-- 2. 容量趋势分析: 周同比环比增长
-- ============================================================
WITH weekly_usage AS (
    SELECT
        date_trunc('week', timestamp) AS week,
        AVG(cpu_usage_pct) AS avg_cpu,
        AVG(memory_usage_pct) AS avg_memory,
        AVG(disk_usage_pct) AS avg_disk
    FROM resource_metrics
    WHERE timestamp >= NOW() - INTERVAL '12 weeks'
    GROUP BY date_trunc('week', timestamp)
)
SELECT
    week,
    avg_cpu,
    avg_memory,
    avg_disk,
    -- 环比增长 (与上周比较)
    LAG(avg_cpu) OVER (ORDER BY week) AS prev_week_cpu,
    CASE
        WHEN LAG(avg_cpu) OVER (ORDER BY week) > 0
        THEN ROUND(
            (avg_cpu - LAG(avg_cpu) OVER (ORDER BY week))
            / LAG(avg_cpu) OVER (ORDER BY week) * 100, 2)
        ELSE NULL
    END AS cpu_wow_growth_pct,

    LAG(avg_memory) OVER (ORDER BY week) AS prev_week_memory,
    CASE
        WHEN LAG(avg_memory) OVER (ORDER BY week) > 0
        THEN ROUND(
            (avg_memory - LAG(avg_memory) OVER (ORDER BY week))
            / LAG(avg_memory) OVER (ORDER BY week) * 100, 2)
        ELSE NULL
    END AS memory_wow_growth_pct

FROM weekly_usage
ORDER BY week DESC;

-- ============================================================
-- 3. 容量耗尽预测 (基于简单线性趋势)
-- ============================================================
WITH daily_cpu AS (
    SELECT
        day,
        avg_cpu_pct AS cpu_usage
    FROM daily_resource_usage
    WHERE day >= NOW() - INTERVAL '30 days'
),
-- 计算线性回归斜率 (CPU 每日增长百分点)
stats AS (
    SELECT
        COUNT(*) AS n,
        SUM(EXTRACT(EPOCH FROM day)) AS sum_x,
        SUM(cpu_usage) AS sum_y,
        SUM(EXTRACT(EPOCH FROM day) * cpu_usage) AS sum_xy,
        SUM(EXTRACT(EPOCH FROM day) * EXTRACT(EPOCH FROM day)) AS sum_xx
    FROM daily_cpu
),
slope AS (
    SELECT
        (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x) AS beta
    FROM stats
),
-- 预测达到告警阈值的时间
predictions AS (
    SELECT
        beta,
        -- 当前 CPU 使用率
        (SELECT cpu_usage FROM daily_cpu ORDER BY day DESC LIMIT 1) AS current_usage,
        -- 达到 80% 告警阈值需要的天数
        CASE
            WHEN beta > 0 THEN (80.0 - (SELECT cpu_usage FROM daily_cpu ORDER BY day DESC LIMIT 1)) / beta
            ELSE NULL
        END AS days_to_warning,
        -- 达到 90% 严重阈值需要的天数
        CASE
            WHEN beta > 0 THEN (90.0 - (SELECT cpu_usage FROM daily_cpu ORDER BY day DESC LIMIT 1)) / beta
            ELSE NULL
        END AS days_to_critical
    FROM slope
)
SELECT
    CURRENT_DATE AS report_date,
    ROUND(current_usage, 2) AS current_cpu_pct,
    ROUND(beta * 30, 2) AS monthly_growth_pct,
    CASE
        WHEN days_to_warning IS NULL THEN '下降趋势，无需扩容'
        WHEN days_to_warning < 30 THEN 'CRITICAL - 30天内达告警阈值'
        WHEN days_to_warning < 60 THEN 'WARNING - 60天内达告警阈值'
        ELSE 'OK - 容量充足'
    END AS cpu_status,
    ROUND(days_to_warning, 0) AS days_until_80pct,
    ROUND(days_to_critical, 0) AS days_until_90pct
FROM predictions;
```

### Grafana Capacity Dashboard JSON Model

```json
{
  "title": "Cluster Capacity Planning Dashboard",
  "description": "容量规划专用 Dashboard，展示集群资源使用趋势、增长预测和容量耗尽预警",
  "schemaVersion": 38,
  "panels": [
    {
      "title": "CPU 利用率与预测",
      "type": "timeseries",
      "gridPos": {"x": 0, "y": 0, "w": 12, "h": 8},
      "targets": [
        {
          "expr": "avg(node_cpu_seconds_total{mode!=\"idle\"}) by (instance)",
          "legendFormat": "{{instance}} - Actual",
          "refId": "A"
        },
        {
          "expr": "predict_linear(node_cpu_seconds_total{mode!=\"idle\"}[30d], 86400 * 30)",
          "legendFormat": "{{instance}} - Predicted (30d)",
          "refId": "B"
        }
      ],
      "thresholds": [
        {"value": 80, "color": "orange"},
        {"value": 90, "color": "red"}
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {"value": -Infinity, "color": "green"},
              {"value": 80, "color": "orange"},
              {"value": 90, "color": "red"}
            ]
          }
        },
        "overrides": []
      },
      "options": {
        "legend": {"displayMode": "table", "placement": "right", "showLegend": true},
        "tooltip": {"mode": "multi"},
        "alertThreshold": true
      }
    },
    {
      "title": "内存利用率与预测",
      "type": "timeseries",
      "gridPos": {"x": 12, "y": 0, "w": 12, "h": 8},
      "targets": [
        {
          "expr": "100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)",
          "legendFormat": "Memory Usage - Actual",
          "refId": "A"
        },
        {
          "expr": "predict_linear(100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100)[30d], 86400 * 30)",
          "legendFormat": "Memory Usage - Predicted (30d)",
          "refId": "B"
        }
      ],
      "thresholds": [
        {"value": 80, "color": "orange"},
        {"value": 90, "color": "red"}
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100
        }
      },
      "options": {
        "legend": {"displayMode": "table"},
        "tooltip": {"mode": "multi"}
      }
    },
    {
      "title": "容量耗尽预测 (本日视图)",
      "type": "stat",
      "gridPos": {"x": 0, "y": 8, "w": 4, "h": 4},
      "targets": [
        {
          "expr": "avg(node_cpu_seconds_total{mode!=\"idle\"})",
          "legendFormat": "Current CPU",
          "refId": "A"
        }
      ],
      "options": {
        "colorMode": "background",
        "graphMode": "sparkline",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "values": false
        },
        "textMode": "value_and_name"
      },
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {"color": "green", "value": null},
              {"color": "orange", "value": 80},
              {"color": "red", "value": 90}
            ]
          }
        }
      }
    },
    {
      "title": "存储增长趋势 (TiB)",
      "type": "timeseries",
      "gridPos": {"x": 4, "y": 8, "w": 8, "h": 4},
      "targets": [
        {
          "expr": "sum(node_filesystem_size_bytes{mountpoint=\"/data\"} - node_filesystem_free_bytes{mountpoint=\"/data\"}) / (1024^4)",
          "legendFormat": "Used Storage (TiB)",
          "refId": "A"
        }
      ],
      "fieldConfig": {
        "defaults": {
          "unit": "tib",
          "min": 0
        }
      }
    },
    {
      "title": "容量规划评分卡",
      "type": "table",
      "gridPos": {"x": 12, "y": 8, "w": 12, "h": 4},
      "targets": [
        {
          "expr": "avg(node_cpu_seconds_total{mode!=\"idle\"})",
          "format": "table",
          "instant": true,
          "refId": "CPU"
        }
      ],
      "transformations": [
        {
          "id": "organize",
          "options": {
            "excludeByName": {},
            "indexByName": {},
            "renameByName": {
              "Time": "时间",
              "Value": "当前值"
            }
          }
        }
      ]
    },
    {
      "title": "Pod 资源请求 vs 节点容量",
      "type": "bargauge",
      "gridPos": {"x": 0, "y": 12, "w": 24, "h": 6},
      "targets": [
        {
          "expr": "sum(kube_pod_resource_request{resource=\"cpu\"}) / sum(node_cpu_capacity) * 100",
          "legendFormat": "CPU Request %",
          "refId": "A"
        },
        {
          "expr": "sum(kube_pod_resource_request{resource=\"memory\"}) / sum(node_memory_capacity_bytes) * 100",
          "legendFormat": "Memory Request %",
          "refId": "B"
        }
      ],
      "options": {
        "orientation": "horizontal",
        "displayMode": "gradient",
        "showUnfilled": true,
        "minVizWidth": 0,
        "minVizHeight": 10
      },
      "fieldConfig": {
        "defaults": {
          "unit": "percent",
          "min": 0,
          "max": 100,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {"color": "green", "value": null},
              {"color": "yellow", "value": 60},
              {"color": "orange", "value": 80},
              {"color": "red", "value": 90}
            ]
          }
        }
      }
    }
  ],
  "time": {
    "from": "now-30d",
    "to": "now"
  },
  "refresh": "5m",
  "tags": ["capacity", "infrastructure", "sre"],
  "timezone": "browser",
  "editable": false
}
```

## Error Handling

### Error Scenario 1: 历史数据不足无法预测 (P2)

**触发条件**: Prometheus 或监控系统中可用的历史数据少于 7 天，导致容量预测模型无法生成可靠的趋势预测

**处理流程**:
```
IF 历史监控数据 < 7 天
THEN
  1. 检查数据缺失原因:
     a. Prometheus 存储配置过期时间太短 (retentionTime < 30d)
     b. 近期新增集群/服务，尚未积累足够数据
     c. 监控 Agent 故障导致数据采集中断
  2. 容量预测降级策略:
     a. 使用行业基准估算 (基于服务器规格标称容量)
     b. 根据业务增长计划（QPS 预期增长 × 资源系数）推算
     c. 使用简单线性外推而非机器学习模型
  3. 立即修复数据采集:
     a. 延长 Prometheus 数据保留期至 90 天
     b. 检查 node_exporter 等 Agent 健康状态
     c. 配置数据备份避免再次丢失
  4. 在报告中标注：
     a. "置信度: 低" 或 "基于有限数据"
     b. 建议 30 天后重新生成预测
     c. 缩小预测范围 (建议不超过 14 天)
  5. 实施主动监控:
     a. 设置 "数据采集健康" 告警
     b. 如果数据中断超过 1 小时触发告警
     c. 数据恢复后自动补采
END
```

**降级方案**: 采用保守的手动估算，基于峰值流量 × 1.5 安全系数规划资源

**升级条件**: 核心集群连续 7 天无监控数据，升级至 SRE Team Lead 修复监控基础设施

### Error Scenario 2: 突发流量超过模型预测 (P1)

**触发条件**: 实际流量峰值超过容量预测的 P95 值 50% 以上，导致资源使用率达到 95%+，触发自动扩缩容但仍然不足

**处理流程**:
```
IF 突发流量超过模型预测上限
THEN
  1. 立即评估容量缺口:
     a. 当前资源使用率 (%) vs 可用容量
     b. 自动扩缩容是否已生效？是否达到上限？
     c. 预计流量持续时间和增长趋势
  2. 紧急扩容措施:
     a. 手动扩容: 临时增加实例数 (超过 ASG 上限)
     b. 降低非关键服务的资源配额
     c. 启用请求排队/限流保护核心服务
  3. 流量管理:
     a. 启用 CDN 缓存减轻源站压力
     b. 启用响应压缩和资源合并
     c. 如果可能，将非核心流量降级或限流
  4. 模型改进:
     a. 识别突发流量模式（促销活动、热点事件、DDoS）
     b. 将突发模型纳入容量预测算法
     c. 增加突发流量的告警和自动扩容响应
  5. 事后复盘:
     a. 分析模型预测失败的原因
     b. 是否需要增加弹性缓冲容量
     c. 更新容量规划模型的输入特征
END
```

**降级方案**: 启动优雅降级，关闭非核心功能（功能开关），保障核心服务稳定

**升级条件**: 资源使用率持续 100% 超过 15 分钟，启动事件响应流程

### Error Scenario 3: 成本预算超限 (P1)

**触发条件**: 月初预测资源成本已经超过当月预算的 80%，或在月中实际成本已达到当月预算的 100%

**处理流程**:
```
IF 成本超预算 80% (月初预警) OR 成本超预算 100% (紧急)
THEN
  1. 立即进行成本审计:
     a. 分析超预算的资源类型和原因
     b. 按服务/部门/项目分解成本构成
     c. 识别异常增长的资源（新服务、配置变更）
  2. 短期降本措施:
     IF 预算超限 < 15%:
       a. 暂停非关键资源的创建和扩容
       b. 将开发/测试环境定时关闭 (非工作时间)
       c. 审查是否有未使用的资源可释放
     ELIF 预算超限 >= 15%:
       a. 立即转换可用的按需实例为 Spot/预留实例
       b. 缩减非生产环境的规格
       c. 检查并清理孤立的存储卷和快照
     ELSE 严重超限:
       a. 申请紧急预算追加
       b. 启动成本优化专项小组
       c. 考虑使用不同定价层级的服务
  3. 长期优化:
     a. 实施 FinOps 实践，按团队拆分成本
     b. 设置成本告警 (50% / 75% / 90% / 100%)
     c. 定期执行资源 Right-Sizing (每月)
  4. 更新容量规划模型:
     a. 将成本约束作为容量规划的硬限制
     b. 增加预算预测模块
     c. 实施 "Greenfield" 架构评审
END
```

**降级方案**: 申请临时预算追加 + 停止所有非必要资源变更，直到成本回落到预算内

**升级条件**: 成本超限导致财务审批拒绝，需要 CTO 和 CFO 联合决策

### Error Scenario 4: 多区域容量不均衡 (P2)

**触发条件**: 同一服务在不同区域的资源使用率差异超过 30%（如 us-east-1 CPU 90% vs eu-west-1 CPU 45%），导致某些区域过载而其他区域资源闲置

**处理流程**:
```
IF 区域间资源使用率差异 > 30%
THEN
  1. 分析流量分布原因:
     a. 用户流量区域性集中
     b. DNS 路由策略不合理
     c. 某些功能仅在特定区域部署
  2. 短期平衡措施:
     a. 调整 DNS 权重，将更多流量导向低负载区域
     b. 在低负载区域临时扩容，高负载区域暂停扩容
     c. 实施区域性限流，保护高负载区域
  3. 长期平衡策略:
     a. 实施基于延迟的 DNS 路由 (Latency-based Routing)
     b. 配置 Auto Scaling 策略按区域独立扩缩容
     c. 部署全局负载均衡器 (GLB)
  4. 容量规划调整:
     a. 按区域独立做容量预测和规划
     b. 建立区域级容量预算
     c. 定期审查区域间容量分布
END
```

**降级方案**: 跨区域资源共享：高负载区域临时使用低负载区域的备用资源

**升级条件**: 单区域使用率持续超过 95% 而其他区域闲置超过 7 天，需要架构评审

## Quality Standards

> Acceptance criteria and quality gates for plan-capacity deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Forecast accuracy is within 15% of actual | Automated check |
| Standard 2 | Headroom maintained at 20% or higher | Automated check |
| Standard 3 | Cost prediction accuracy is within 20% of actual | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
