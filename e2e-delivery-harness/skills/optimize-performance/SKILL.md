---
name: optimize-performance
description: "Domain skill for optimize-performance execution"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 性能优化 (Performance Optimization)

## Overview

本 Skill 定义了性能优化的核心知识体系。

## Core Knowledge

### 性能分析方法

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


## Core Knowledge

> Essential knowledge domain for optimize-performance execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for optimize-performance excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during optimize-performance execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
