---
name: plan-capacity
description: "Domain skill for plan-capacity execution"
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
# Skill: 容量规划 (Capacity Planning)

## Overview

本 Skill 定义了容量规划的核心知识和方法，涵盖指标体系、预测方法、自动化扩缩容策略及成本优化实践。适用于基础设施工程师、SRE 团队及架构师进行系统容量评估与规划。

## Core Knowledge

### 容量规划基本公式

#### Little's Law (利特尔法则)
L = &lambda;W
- **L**: 系统中平均请求数（并发数）
- **&lambda;**: 平均到达率（请求/秒）
- **W**: 平均处理时间（秒）

#### 利用率计算
```
Utilization = Arrival Rate / Service Rate
Utilization = ρ = λ / (μ × n)
```
- **μ**: 单节点服务速率
- **n**: 并行节点数
- **ρ < 0.7**: 一般建议目标利用率（预留突发缓冲）

### 容量指标体系

| 指标类别 | 核心指标 | 预警阈值 | 严重阈值 |
|---------|---------|---------|---------|
| CPU | 利用率 / Load Average / 上下文切换 | ≥70% | ≥90% |
| 内存 | 利用率 / Swap使用 / OOM事件 | ≥80% | ≥95% |
| 存储 | 利用率 / IOPS / 吞吐量 / inode | ≥70% | ≥85% |
| 磁盘IO | IOPS利用率 / 延迟(p99) / 队列深度 | ≥75% | ≥90% |
| 网络 | 带宽利用率 / 丢包率 / 连接数 | ≥60% | ≥80% |
| 应用 | TPS/QPS / 响应时间(p99) / 错误率 | 响应时间≥500ms | 响应时间≥2s |

### 预测方法

1. **趋势分析 (Trend Analysis)**: 基于历史时序数据（≥90天），使用移动平均、指数平滑进行短期预测（1-4周）
2. **线性回归 (Linear Regression)**: 建立资源使用量与业务指标（如DAU、订单量）的回归模型，用于中长期预测（1-6个月）
3. **季节分解 (Seasonal Decomposition)**: 将时序数据分解为趋势、季节性和残差分量，识别周/月/季度周期性模式
4. **排队论 (Queuing Theory)**: 使用 M/M/c 队列模型评估不同并发下的系统行为，预测排队延迟和资源饱和点
5. **资源建模 (Resource Modeling)**: 通过压测和性能基准建立资源使用与负载的数学模型，模拟扩容/缩容效果

### 扩容策略

| 策略 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| 垂直扩展 (Scale Up) | 数据库、有状态服务 | 架构不变，操作简单 | 受物理机上限约束，成本非线性增长 |
| 水平扩展 (Scale Out) | 无状态应用、微服务 | 弹性好，无限扩展，成本线性 | 需要负载均衡、分布式架构支持 |
| 混合扩展 (Hybrid) | 复杂分层架构 | 灵活性最高 | 运维复杂度最高 |

### 容量规划自动化：CapacityPlanner

```python
class CapacityPlanner:
    """容量规划自动化工具"""

    def __init__(self, metrics_history: list[dict], service_config: dict):
        """
        初始化容量规划器

        Args:
            metrics_history: 历史指标数据，每项包含 timestamp, cpu, memory, disk, qps
            service_config: 服务配置，含副本数、资源限制、冗余策略
        """
        self.metrics = metrics_history
        self.config = service_config
        self.buffer_ratio = 0.5  # 50% 突发缓冲

    def calculate_headroom(self, current_usage: dict) -> dict:
        """
        计算当前剩余容量（Headroom）

        根据当前资源使用率与峰值容量的差值，评估可承载的额外负载量。

        Args:
            current_usage: 当前资源使用率 {cpu, memory, disk_iops, network}

        Returns:
            headroom: 各维度的剩余容量百分比
        """
        headroom = {}
        max_capacity = self.config.get("max_capacity", {})
        for resource, usage in current_usage.items():
            cap = max_capacity.get(resource, 100)
            headroom[resource] = round((cap - usage) / cap * 100, 2)
        return headroom

    def forecast_demand(self, business_metric: list[tuple[float, float]],
                        days_ahead: int = 30) -> dict:
        """
        基于业务指标预测未来资源需求

        使用线性回归建立业务指标（如DAU、订单量）与资源消耗的关系模型，
        结合历史趋势进行多时间尺度预测。

        Args:
            business_metric: [(timestamp, value)] 业务指标时序数据
            days_ahead: 预测天数

        Returns:
            预测结果，包含每日资源需求预测及置信区间
        """
        import numpy as np

        # 拟合线性模型
        timestamps = np.array([t for t, _ in business_metric])
        values = np.array([v for _, v in business_metric])
        coeffs = np.polyfit(timestamps, values, 1)
        trend = np.poly1d(coeffs)

        # 计算历史资源与业务指标的比例关系
        recent_metrics = self.metrics[-30:]
        avg_cpu_per_unit = np.mean([
            m["cpu"] / m["qps"] for m in recent_metrics if m.get("qps", 0) > 0
        ])

        # 预测未来需求
        future_demand = {}
        for day in range(1, days_ahead + 1):
            predicted_business = trend(timestamps[-1] + day)
            cpu_demand = predicted_business * avg_cpu_per_unit
            future_demand[f"day_{day}"] = {
                "predicted_cpu_pct": round(min(cpu_demand * 100, 100), 1),
                "confidence_95_lower": round(cpu_demand * 0.85 * 100, 1),
                "confidence_95_upper": round(min(cpu_demand * 1.15 * 100, 100), 1),
            }
        return future_demand

    def recommend_scaling(self, current_deployment: dict) -> dict:
        """
        推荐扩缩容决策

        综合当前负载、历史趋势和冗余策略，给出具体扩容/缩容建议。

        Args:
            current_deployment: 当前部署信息 {replicas, instance_type, cpu_usage, mem_usage}

        Returns:
            推荐动作: {action: "scale_out"/"scale_up"/"scale_in"/"none",
                       reason, target_replicas, target_instance_type}
        """
        cpu = current_deployment.get("cpu_usage", 0)
        mem = current_deployment.get("mem_usage", 0)
        replicas = current_deployment.get("replicas", 1)

        # 扩容条件：CPU >= 70% 或 内存 >= 80%
        if cpu >= 70 or mem >= 80:
            new_replicas = replicas + max(1, int((cpu - 50) / 10))
            return {
                "action": "scale_out",
                "reason": f"CPU={cpu}%, Memory={mem}% 超过扩容阈值",
                "target_replicas": new_replicas,
                "target_instance_type": current_deployment.get("instance_type"),
            }

        # 缩容条件：CPU < 30% 且 内存 < 40% 且 replica > min_replicas
        min_replicas = self.config.get("min_replicas", 1)
        if cpu < 30 and mem < 40 and replicas > min_replicas:
            new_replicas = max(min_replicas, replicas - 1)
            return {
                "action": "scale_in",
                "reason": f"CPU={cpu}%, Memory={mem}% 低于缩容阈值",
                "target_replicas": new_replicas,
                "target_instance_type": current_deployment.get("instance_type"),
            }

        return {
            "action": "none",
            "reason": "资源使用率在正常范围内，无需调整",
            "target_replicas": replicas,
            "target_instance_type": current_deployment.get("instance_type"),
        }
```

## Best Practices

1. **基于历史数据的容量预测**：收集 ≥90 天的资源使用趋势数据，使用线性回归和季节性分解进行容量预测，避免依赖单一数据点。预测报告应包含 P50/P95/P99 三个分位值，以便评估不同风险等级下的容量需求。月度 Review 预测准确率（MAPE ≤ 15%），持续优化预测模型。

2. **N+1 冗余规划**：所有关键服务至少保留 N+1 容量冗余，确保单点故障时剩余容量可承载全部负载（冗余度 ≥30%）。冗余规划需覆盖可用区级别（AZ-level）和实例级别（Instance-level）两个维度。对于跨AZ部署，每个AZ应独立满足N+1要求。

3. **弹性伸缩自动化**：配置基于 CPU ≥70%、内存 ≥80%、请求队列 ≥1000 的自动扩容触发规则，缩容冷却时间 ≥10 分钟防止抖动。使用步进扩容（Step Scaling）而非简单阈值，如 CPU≥70% +1副本，≥85% +2副本。定期（每月）进行弹性伸缩演练，验证扩容至 2倍负载的响应时间 ≤5 分钟。

## Common Pitfalls

### Pitfall 1: 忽视突发流量

- **Risk**：仅按平均负载规划容量，峰值时服务降级甚至雪崩。流量突发（如促销活动、热点事件）可在数秒内将负载推至平均值的 5-10 倍，导致系统过载、响应时间飙升、级联故障。
- **Prevention**：使用 P95/P99 峰值而非平均值进行容量基线评估，预留突发缓冲 ≥50%。对已知的大流量事件（如双11、秒杀）提前进行容量预估和压测验证。部署熔断（Circuit Breaker）和限流（Rate Limiting）机制作为最后防线。
- **Impact**：P0 级生产事故，用户大规模不可用，可能导致业务收入损失和品牌声誉损害。恢复时间取决于扩容速度，每延长 1 分钟影响范围扩大 10 倍。

### Pitfall 2: 过度预留资源

- **Risk**：为保险起见大量超额预留资源，"just in case" 思维导致云成本超出预算 ≥200%。云环境中未充分利用的闲置资源持续产生费用，且增加了运维复杂度。
- **Prevention**：使用 FinOps 方法论，建立成本可视化仪表板。定期（月度）审查资源利用率，闲置 ≥30% 的实例自动回收或降配。对预留实例（RI/ Savings Plans）采用"按需先行+预留补充"策略，预留覆盖率控制在 60-70%。
- **Impact**：年度预算严重超支，资源浪费可能导致其他创新项目资金不足。过度预留还会造成"资源囤积"效应，真正需要资源的服务反而无法获取。

### Pitfall 3: 垂直扩展惯性

- **Risk**：问题出现时一味升级实例规格（vCPU/内存）而非水平扩展。垂直扩展受限于单机最大规格，且大型实例的成本并非线性增长（如 2x 规格可能是 3x 价格），同时存在迁移停机时间。
- **Prevention**：优先考虑水平扩展架构（≥3 副本），仅在单机瓶颈（如许可证限制、有状态服务）时才垂直扩展。建立"先水平，后垂直"的决策树：先检查是否可以增加副本，再考虑升级规格。架构评审中明确记录扩展策略决策。
- **Impact**：扩展上限受限于物理机最大规格，当业务增长超过最大规格时需重新架构，导致重大重构。成本效率低下，大型实例的单价高于同容量的小型实例组合。

## 相关资产

- **标准**: `../../standards/sre-standard.md`
- **标准**: `../../standards/ops-standard.md`
- **评估**: `../../evaluations/capacity-planning-quality.json`
- **评估**: `../../evaluations/cloud-cost-optimization.json`
