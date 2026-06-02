---
name: optimize-performance
description: "Detailed technical instructions for optimize-performance scenario execution"
applyTo: "scenarios/optimize-performance/**"
phase: operations
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 性能优化 (Optimize Performance)

## Performance Optimization Layers

### 优化层次结构

```
┌─────────────────────────────────────┐
│           架构层优化                  │
│  (异步、缓存、读写分离、分库分表)      │
├─────────────────────────────────────┤
│           服务层优化                  │
│  (连接池、线程池、并发优化)           │
├─────────────────────────────────────┤
│           数据库优化                  │
│  (索引、SQL、架构)                   │
├─────────────────────────────────────┤
│           代码层优化                  │
│  (算法、数据结构、资源管理)            │
└─────────────────────────────────────┘
```

## Code Optimization Standards

### 算法优化

| 场景 | 优化前 | 优化后 |
|------|--------|--------|
| 列表查找 | O(n) 遍历 | O(1) Map |
| 嵌套循环 | O(n²) | O(n) 单循环 |
| 重复计算 | 每次计算 | 缓存结果 |

### 并发优化

```python
# 连接池优化
pool_config = {
    "min_size": 10,
    "max_size": 100,
    "idle_timeout": 300,
    "max_lifetime": 3600
}

# 线程池优化
executor_config = {
    "core_pool_size": 10,
    "max_pool_size": 100,
    "queue_capacity": 1000,
    "keep_alive_time": 60
}
```

## Database Optimization Standards

### 索引优化

```sql
-- 覆盖索引优化
-- 创建覆盖索引
CREATE INDEX idx_user_cover ON users(id, name, email);

-- 查询使用覆盖索引
SELECT id, name, email FROM users WHERE id = ?;
```

### SQL 优化

```sql
-- 避免 SELECT *
SELECT id, name FROM users WHERE id = 1;

-- 使用 LIMIT 限制
SELECT * FROM logs WHERE created_at > ? LIMIT 100;

-- 使用 EXPLAIN 分析
EXPLAIN SELECT * FROM orders WHERE user_id = 1;
```

## Cache Optimization Standards

### 多级缓存

```yaml
cache_levels:
  l1:
    type: "本地缓存 (Caffeine/Guava)"
    capacity: "1000 items"
    ttl: "5 minutes"

  l2:
    type: "Redis 分布式缓存"
    capacity: "无限制"
    ttl: "30 minutes"

  strategy: "Cache-Aside"
```

### 缓存策略

| 策略 | 适用场景 | 实现难度 |
|------|----------|----------|
| Cache-Aside | 读多写少 | 低 |
| Write-Through | 数据一致性 | 中 |
| Write-Behind | 高写入性能 | 高 |

## Performance Monitoring Metrics

```yaml
metrics:
  latency:
    p50: "< 50ms"
    p95: "< 200ms"
    p99: "< 500ms"

  throughput:
    qps: "> 1000"

  error_rate:
    percentage: "< 0.1%"
```


## Overview

> High-level description of the optimize-performance execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the optimize-performance scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for optimize-performance.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for optimize-performance execution.

1. **Practice 1**: Profile applications to identify actual bottlenecks
2. **Practice 2**: Optimize at the code, database, and infrastructure layers
3. **Practice 3**: Validate improvements do not regress other metrics


## Error Handling

> Common error scenarios and resolution strategies for optimize-performance.

### Error Category 1
**Symptom**: Performance bottlenecks are not clearly identified
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Optimization causes regression in other areas
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for optimize-performance deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Target metric improves by 20% or more | Automated check |
| Standard 2 | No regression in non-target metrics | Automated check |
| Standard 3 | Optimization cost does not exceed resource budget | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
