---
name: optimize-performance
description: "Domain skill for optimize-performance execution"
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
# Skill: 性能优化 (Performance Optimization)

## Overview

本 Skill 定义了性能优化的核心知识体系，涵盖性能分析方法论、分层优化策略、各种Profiling技术和性能测试方法，帮助团队系统性地定位和消除性能瓶颈，达成既定的性能SLO目标。

## Core Knowledge

### 性能分析方法论

| 方法论 | 核心维度 | 适用层级 | 核心思想 |
|--------|---------|---------|---------|
| **USE 方法** (Utilization / Saturation / Errors) | 利用率、饱和度、错误数 | 基础设施层（CPU/内存/磁盘/网络） | 对每个资源检查"利用率是否过高？是否饱和？有无错误？" |
| **RED 方法** (Rate / Errors / Duration) | 速率、错误、持续时间 | 服务层（API/微服务） | 对每个服务监控请求速率、错误率、延迟分布 |
| **Four Golden Signals** | 延迟、流量、错误、饱和度 | 整体 SRE | Google SRE 定义的四个核心信号，覆盖服务健康全维度 |

### Profiling 类型

- **CPU Profiling**: 使用 perf / pprof / async-profiler 采集 CPU 热点，生成 Flame Graph（火焰图），定位最耗 CPU 的代码路径
- **Memory Profiling**: 堆转储分析 (Heap Dump)，定位内存泄漏、大对象分配、频繁 GC 问题；分析对象引用链
- **I/O Profiling**: 磁盘读写延迟、IOPS、文件系统缓存命中率分析
- **Network Profiling**: 网络延迟、吞吐量、TCP重传率、连接池耗尽分析

### 优化层次 (自上而下按收益/成本比排序)

```
应用层 (Application Code)
    ↓ 算法优化、缓存引入、连接池调优
数据库层 (Database Queries)
    ↓ 索引优化、慢查询改造、读写分离
缓存层 (Caching)
    ↓ 多级缓存、缓存策略选择、缓存预热
基础设施层 (Infrastructure)
    ↓ 实例规格升级、存储类型优化
网络层 (Network)
    ↓ 链路优化、CDN加速、协议升级
```

### 性能测试类型

| 测试类型 | 目标 | 负载模型 | 成功标准 |
|---------|------|---------|---------|
| **Load Test (负载测试)** | 验证系统在预期负载下的行为 | 预期峰值 QPS × 持续 30min | P95 延迟 < SLO，错误率 < 0.1% |
| **Stress Test (压力测试)** | 找到系统的极限拐点 | 逐步增加 QPS 直到系统过载 | 确定最大可持续吞吐量 |
| **Soak Test (耐久测试)** | 验证长期运行稳定性 | 80% 预期峰值 QPS × 持续 ≥ 4h | 无内存泄漏、延迟无逐级退化 |
| **Spike Test (突发测试)** | 验证突发流量处理能力 | 瞬间 10× 峰值 QPS 持续 2min | 系统不崩溃，恢复后延迟回归基线 |

### PerformanceOptimizer 类

```python
import enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class PerformanceMetrics:
    """性能指标数据模型"""
    p50_latency_ms: float = 0.0
    p95_latency_ms: float = 0.0
    p99_latency_ms: float = 0.0
    throughput_qps: float = 0.0
    error_rate: float = 0.0
    cpu_usage: float = 0.0
    memory_usage: float = 0.0
    cache_hit_rate: float = 0.0
    database_latency_ms: float = 0.0


@dataclass
class Bottleneck:
    """性能瓶颈定义"""
    layer: str
    metric: str
    severity: str  # critical / high / medium / low
    current_value: float
    threshold: float
    recommendation: str = ""


@dataclass
class OptimizationResult:
    """优化结果"""
    before: PerformanceMetrics
    after: PerformanceMetrics
    improvement_pct: float = 0.0
    cost: str = ""


class PerformanceOptimizer:
    """性能优化器，支持Profiling分析、瓶颈定位和优化建议"""

    def __init__(self, baseline: Optional[PerformanceMetrics] = None):
        self.baseline = baseline or PerformanceMetrics()
        self.bottlenecks: List[Bottleneck] = []
        self.profiles: Dict[str, str] = {}  # profile_type -> raw_data_path

    def profile_cpu(self, duration_sec: int = 60) -> str:
        """执行CPU Profiling，返回Flame Graph数据路径"""
        import tempfile
        import time
        output_path = tempfile.mktemp(suffix=".cpuprofile")
        # 实际场景中使用 perf / async-profiler
        start = time.time()
        # ... profiling logic
        elapsed = time.time() - start
        self.profiles["cpu"] = output_path
        print(f"CPU profiling completed in {elapsed:.1f}s, output: {output_path}")
        return output_path

    def analyze_flamegraph(self, profile_path: str) -> List[Tuple[str, float]]:
        """分析Flame Graph，返回热点函数及其CPU占比列表"""
        import re
        hotspots: List[Tuple[str, float]] = []
        # 解析Flame Graph数据，提取CPU占比 > 5% 的热点函数
        # 实际场景解析 folded stack 格式
        with open(profile_path, "r") as f:
            for line in f:
                match = re.match(r"^(?P<func>.+?)\s+(?P<pct>\d+\.?\d*)$", line)
                if match and float(match.group("pct")) > 5.0:
                    hotspots.append((match.group("func"), float(match.group("pct"))))
        return sorted(hotspots, key=lambda x: x[1], reverse=True)

    def identify_bottleneck(self, metrics: PerformanceMetrics) -> Optional[Bottleneck]:
        """基于USE/RED方法识别最严重的性能瓶颈"""
        self.bottlenecks.clear()
        thresholds = {
            "cpu": 80.0,
            "memory": 80.0,
            "database_latency": 100.0,
            "cache_hit_rate": 80.0,
            "error_rate": 1.0,
            "latency_degradation": 200.0,  # % of baseline
        }
        checks = [
            ("CPU", "cpu_usage", metrics.cpu_usage, thresholds["cpu"],
             "优化算法复杂度、引入并行处理或升级实例规格"),
            ("Memory", "memory_usage", metrics.memory_usage, thresholds["memory"],
             "检查内存泄漏、调整JVM/OS内存参数、减少大对象分配"),
            ("Database", "database_latency_ms", metrics.database_latency_ms,
             thresholds["database_latency"], "添加索引、优化SQL、引入读写分离"),
            ("Cache", "cache_hit_rate", metrics.cache_hit_rate * 100,
             thresholds["cache_hit_rate"], "检查缓存过期策略、增加缓存容量、预热缓存"),
        ]
        for layer, metric_name, value, threshold, rec in checks:
            if value > threshold and metric_name != "cache_hit_rate":
                severity = "critical" if value > threshold * 1.5 else "high"
                self.bottlenecks.append(Bottleneck(
                    layer=layer, metric=metric_name, severity=severity,
                    current_value=value, threshold=threshold, recommendation=rec,
                ))
            elif metric_name == "cache_hit_rate" and value < threshold:
                self.bottlenecks.append(Bottleneck(
                    layer="Cache", metric="cache_hit_rate", severity="high",
                    current_value=value, threshold=threshold, recommendation=rec,
                ))

        if not self.bottlenecks:
            return None
        # 按严重程度排序返回最严重的瓶颈
        severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        self.bottlenecks.sort(key=lambda b: severity_order.get(b.severity, 99))
        return self.bottlenecks[0]

    def suggest_optimization(self, bottleneck: Bottleneck) -> List[str]:
        """针对瓶颈生成具体的优化建议列表"""
        layer_optimizations = {
            "CPU": [
                "使用内存缓存/本地缓存减少重复计算",
                "优化热点循环，降低时间复杂度（如 O(n^2) → O(n log n)）",
                "引入异步/并行处理，减少串行等待",
                "使用连接池复用资源",
            ],
            "Memory": [
                "分析堆转储，定位大对象和泄漏点",
                "调整 GC 参数（GC 算法、堆大小、新生代/老年代比例）",
                "减少不必要的对象创建，复用对象实例",
                "检查第三方库的内存占用",
            ],
            "Database": [
                "通过 EXPLAIN 分析慢查询，添加缺失索引或优化索引结构",
                "将复杂 JOIN 拆分为多次简单查询 + 应用层聚合",
                "引入 Redis / Memcached 缓存热点数据",
                "对只读场景实施读写分离，扩展读能力",
                "对单表过大场景实施分库分表",
            ],
            "Cache": [
                "实施 L1 (Caffeine) → L2 (Redis) → L3 (CDN) 三级缓存",
                "调整缓存过期时间，平衡数据新鲜度与命中率",
                "使用缓存预热策略，避免启动后缓存穿透",
                "对写操作实施 Cache-Aside 模式，保证缓存与数据库一致",
            ],
            "Network": [
                "使用 CDN 加速静态资源分发",
                "启用 HTTP/2 多路复用减少连接数",
                "对跨区域调用使用专用网络/专线",
                "压缩传输内容（gzip / brotli）",
            ],
        }
        return layer_optimizations.get(bottleneck.layer, ["分析瓶颈来源后确定优化方向"])

    def run_optimization(self, metrics: PerformanceMetrics) -> Optional[OptimizationResult]:
        """完整优化流程：识别瓶颈 → 生成建议 → 返回优化结果"""
        bottleneck = self.identify_bottleneck(metrics)
        if not bottleneck:
            return None
        suggestions = self.suggest_optimization(bottleneck)
        print(f"Top bottleneck: [{bottleneck.severity}] {bottleneck.layer} - "
              f"{bottleneck.metric} (current: {bottleneck.current_value}, "
              f"threshold: {bottleneck.threshold})")
        for i, s in enumerate(suggestions, 1):
            print(f"  {i}. {s}")
        return OptimizationResult(
            before=metrics,
            after=PerformanceMetrics(),  # placeholder for re-measured metrics
            improvement_pct=0.0,
            cost="TBD",
        )
```

### 性能分析方法（传统分析器）

```python
class PerformanceAnalyzer:
    """性能分析器"""

    def analyze_bottleneck(self, metrics):
        """分析瓶颈"""
        bottlenecks = []

        if metrics.cpu_usage > 80:
            bottlenecks.append(("CPU", "High CPU usage"))

        if metrics.memory_usage > 80:
            bottlenecks.append(("Memory", "High memory usage"))

        if metrics.database_latency > 100:
            bottlenecks.append(("Database", "Slow queries"))

        if metrics.cache_hit_rate < 0.8:
            bottlenecks.append(("Cache", "Low cache hit rate"))

        return bottlenecks

    def suggest_optimization(self, bottleneck):
        """建议优化方案"""
        if bottleneck.type == "CPU":
            return [
                "优化算法复杂度",
                "使用并行处理",
                "减少不必要计算"
            ]
        elif bottleneck.type == "Database":
            return [
                "添加合适索引",
                "优化 SQL",
                "使用缓存"
            ]
```

### 性能测试方法

```python
class PerformanceTest:
    """性能测试"""

    @staticmethod
    def load_test(target_qps, duration):
        """负载测试"""
        results = []
        for t in range(duration):
            response = make_request(target_qps)
            results.append(response)
        return analyze_results(results)

    @staticmethod
    def stress_test(start_qps, increment, duration):
        """压力测试"""
        qps = start_qps
        while True:
            results = load_test(qps, duration)
            if results.error_rate > 0.01:
                break
            qps += increment
        return qps
```

## Associated Assets

- **Scenario**: `../../scenarios/optimize-performance/SCENARIO.md`
- **Instruction**: `../../instructions/optimize-performance.instructions.md`
- **Prompt**: `../../prompts/optimize-performance.prompt.md`
- **Agent**: `../../agents/optimize-performance.agent.md`

## Best Practices

> 性能优化的行业最佳实践，确保优化过程系统化、可量化、可验证。

1. **数据驱动优化**：优化前必须建立性能基线（P50 / P95 / P99 延迟、吞吐量、错误率），使用 APM 工具（如 Prometheus + Grafana / Jaeger）采集 ≥7 天的基线数据。禁止凭直觉优化——每项优化必须有 Before / After 对比数据证明效果，优化目标要求可量化的改善（如 P95 延迟降低 ≥30%）

2. **自顶向下分层优化**：按收益 / 成本比排序优化优先级——应用层（算法复杂度、缓存引入）→ 数据库层（索引、查询优化、读写分离）→ 基础设施层（实例规格、网络带宽）。每层优化后重新测量，如果上层优化已达标则停止下层优化（避免过早优化和过度工程）

3. **缓存金字塔策略**：构建 L1（进程内 Caffeine / Guava，TTL ≤5min）→ L2（分布式 Redis / Memcached，TTL ≤30min）→ L3（CDN / 边缘缓存，TTL ≤24h）三级缓存体系。每级缓存命中率目标：L1 ≥80%，L2 ≥95%，L3 ≥99%。缓存缺失向下穿透，写操作实时同步避免过期数据

## Common Pitfalls

> 性能优化中常见错误及其防范措施。

### Pitfall 1: 过早优化

**Risk**: 未建立性能基线和瓶颈证据即开始优化，优化了非热点代码（<5% 请求路径）。根据 Amdahl 定律，优化非瓶颈部分对整体性能提升几乎无影响。

**Prevention**: 使用 Profiler（如 async-profiler / pprof）和 APM（如 Datadog / SkyWalking）定位瓶颈，遵循 90/10 法则——90% 的时间花在 10% 的热点代码上。优化前必须回答："这个优化会影响百分之几的请求？"

**Impact**: 开发时间浪费在非热点代码上，代码复杂度增加但性能无实质改善，反而可能引入新的 Bug。

### Pitfall 2: 过度缓存导致数据不一致

**Risk**: 为降低数据库压力将所有查询都缓存，缓存失效策略不完善（如 TTL 过长、未及时淘汰脏数据），导致用户看到过期 / 错误数据。最典型的是 Cache-Aside 模式下先更新数据库再删缓存的顺序错误。

**Prevention**: 区分缓存策略——静态数据用 Cache-Aside，高一致性需求用 Write-Through / Read-Through，实时数据用 Refresh-Ahead，敏感数据（余额、库存）禁止缓存或仅允许 TTL ≤1s。

**Impact**: 数据不一致可能引发业务决策错误（如显示错误库存导致超卖、展示过时价格引发客诉），需要数据回滚和业务补偿。

### Pitfall 3: 忽视数据库层优化

**Risk**: 应用层优化到极致（如引入多级缓存、异步化），但数据库查询仍全表扫描、N+1 查询问题未解决、缺少必要索引。瓶颈从应用转移至数据库，总体延迟无明显改善。

**Prevention**: 使用 EXPLAIN 分析所有 SQL 执行计划，确保 type = ALL（全表扫描）的表占比 < 5%，慢查询（>100ms）占比 < 1%。对所有 JOIN 和 WHERE 字段建立合适索引，使用 ORM 的懒加载/预加载策略解决 N+1 问题。

**Impact**: 上层优化红利被数据库瓶颈抵消，总体延迟无明显改善，数据库服务器成为新的单点瓶颈，扩展成本极高。

## 相关资产

以下标准和评估清单与本技能直接相关，执行性能优化时应一并参考：

- [SRE 最佳实践](../../standards/sre-best-practices.md) — 服务可靠性工程方法论与性能 SLI/SLO 定义
- [监控标准](../../standards/monitoring-standards.md) — 性能指标采集规范与 Dashboard 设计原则
- [性能基线评估](../../evaluations/performance-baseline.md) — 性能基线采集和对比分析模板
- [响应时间分析](../../evaluations/response-time-analysis.md) — 延迟分布分析和优化追踪模版
- [查询性能基准](../../evaluations/query-performance-benchmark.md) — SQL 执行计划分析和索引优化评估
