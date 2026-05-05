---
name: performance-testing
description: "Domain skill for performance-testing execution"
type: skill
version: "1.1.0"
stage: "performance-testing"
---

# Skill: 性能测试 (Performance Testing)

## Overview

本 Skill 定义了性能测试领域的核心知识、工具使用和最佳实践，用于指导 AI Agent 执行专业的性能测试工作。

## Core Knowledge

### 1. 性能测试基础

#### 性能测试目标
- **响应时间**: 用户感知速度
- **吞吐量**: 系统处理能力
- **资源利用率**: 资源使用效率
- **稳定性**: 长时间运行可靠性

#### Performance Test Types
| 类型 | 描述 | 适用场景 |
|------|------|----------|
| 基准测试 | 单用户性能基线 | 新系统上线 |
| 负载测试 | 正常负载性能 | 版本发布 |
| 压力测试 | 极限负载 | 容量规划 |
| 稳定性测试 | 长时间运行 | SLA 验证 |
| 峰值测试 | 峰值负载 | 活动保障 |

### 2. 性能指标体系

#### 黄金指标 (RED Method)
- **Rate**: 请求率/吞吐量
- **Errors**: 错误率
- **Duration**: 响应时间

#### USE 方法
- **Utilization**: 利用率
- **Saturation**: 饱和度
- **Errors**: 错误

### 3. 响应时间分析

#### 响应时间组成
```
RT = TTI + NWT + ST + BWT + PWT + ETT

TTI: Think Time (思考时间)
NWT: Network Time (网络时间)
ST: Server Time (服务器处理时间)
BWT: Database Time (数据库时间)
PWT: Processing Time (进程时间)
ETT: End-to-End Time (端到端时间)
```

#### 响应时间分布
- **P50 (Median)**: 50% 请求的响应时间
- **P90**: 90% 请求的响应时间
- **P95**: 95% 请求的响应时间
- **P99**: 99% 请求的响应时间
- **P999**: 99.9% 请求的响应时间

## Tool Usage

### JMeter

#### 常用组件
| 组件 | 用途 |
|------|------|
| Thread Group | 模拟用户并发 |
| HTTP Request | 发送 HTTP 请求 |
| Response Assertion | 验证响应结果 |
| Duration Assertion | 验证响应时间 |
| Summary Report | 聚合报告 |
| View Results Tree | 详细结果 |

#### 常用函数
```jmeter
${__time()}              # 当前时间戳
${__UUID()}             # UUID
${__Random()}           # 随机数
${__V(var${i})}        # 变量引用
```

### Locust

#### 常用装饰器
```python
@task(weight)           # 任务权重
@task_pool             # 任务池
@events                # 事件钩子
```

#### 常用类
```python
HttpUser              # HTTP 用户
TaskSet              # 任务集
between(a, b)        # 等待时间范围
constant(a)          # 固定等待时间
```

### Prometheus + Grafana

#### 常用查询
```promql
# QPS
rate(http_requests_total[5m])

# 延迟
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# 错误率
rate(http_requests_total{status=~"5.."}[5m])
```

## Best Practices

### 测试设计
1. **真实模拟**: 模拟真实用户行为
2. **数据准备**: 准备充分的测试数据
3. **预热**: 测试前进行预热
4. **监控**: 全程监控关键指标

### 测试执行
1. **隔离**: 避免外部干扰
2. **重复**: 多次执行取稳定值
3. **记录**: 详细记录测试过程
4. **监控**: 全程监控系统状态

### Consequences分析
1. **对比**: 与基线和目标对比
2. **分解**: 分解响应时间组成
3. **关联**: 关联系统指标分析
4. **验证**: 验证分析结论

## Performance Optimization Guide

### 优化层次

```
┌─────────────────────────────────────┐
│  架构层优化                          │
│  ├── 微服务拆分                      │
│  ├── 读写分离                        │
│  └── 异步处理                        │
├─────────────────────────────────────┤
│  应用层优化                          │
│  ├── 代码优化                        │
│  ├── 算法优化                        │
│  └── 缓存使用                        │
├─────────────────────────────────────┤
│  中间件优化                          │
│  ├── 数据库调优                      │
│  ├── 缓存优化                        │
│  └── 队列优化                        │
├─────────────────────────────────────┤
│  基础设施优化                        │
│  ├── 资源扩容                        │
│  ├── 网络优化                        │
│  └── CDN 使用                        │
└─────────────────────────────────────┘
```

### 优化优先级

| 优先级 | 优化项 | 收益 | 成本 |
|--------|--------|------|------|
| 1 | 数据库索引 | 高 | 低 |
| 2 | 缓存 | 高 | 低 |
| 3 | 异步处理 | 中 | 中 |
| 4 | 代码优化 | 中 | 高 |
| 5 | 架构调整 | 高 | 高 |

## FAQ

### Q1: 如何确定并发用户数？

```python
# 公式: 并发用户 = 日活用户 × 峰值系数 / 日内峰值小时数 / 平均操作次数
并发用户 = DAU × Peak_Load_因子 × Sessions_Per_User / Hours_of_Peak
```

### Q2: 如何选择测试持续时间？

```python
# 负载测试: 30-60 分钟
# 稳定性测试: 8-24 小时
# 压力测试: 20-30 分钟
```

### Q3: 如何处理测试结果波动？

```python
# 方法:
# 1. 增加预热时间
# 2. 增加测试时长
# 3. 多次执行取平均
# 4. 排除异常值
```

## Associated Assets

| 资产类型 | 文件路径 |
|----------|----------|
| Scenario | `../../scenarios/performance-testing/SCENARIO.md` |
| Instruction | `../../instructions/performance-testing.instructions.md` |
| Prompt | `../../prompts/performance-testing.prompt.md` |
| Agent | `../../agents/verify-test.agent.md` |


## Core Knowledge

> Essential knowledge domain for performance-testing execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for performance-testing excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Common Pitfalls

> Frequent mistakes to avoid during performance-testing execution.

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
