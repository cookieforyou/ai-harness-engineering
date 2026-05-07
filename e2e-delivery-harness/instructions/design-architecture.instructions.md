---
name: design-architecture
description: "Detailed technical instructions for design-architecture scenario execution"
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['instruction', 'technical']
---
# Instructions: 架构设计 (Design Architecture)

## Architecture Style Standards

### 主流架构风格对比

| 架构风格 | 特点 | 适用场景 | 复杂度 |
|----------|------|----------|--------|
| 单体架构 | 简单、部署方便 | 小团队、初创产品 | 低 |
| 模块化单体 | 代码隔离、易测试 | 中等规模 | 中 |
| 微服务架构 | 松耦合、独立部署 | 大型复杂系统 | 高 |
| 事件驱动架构 | 解耦、异步通信 | 高并发系统 | 中 |
| CQRS | 读写分离 | 大数据量 | 中 |

### 微服务拆分原则

```yaml
# 微服务拆分原则
decomposition_principles:
  single_responsibility:
    description: "每个服务只负责一项业务能力"
    example: |
      # 好的拆分
      user-service, order-service, payment-service
      
      # 坏的拆分
      user-order-service (承担两个职责)

  domain_driven:
    description: "按业务领域边界拆分"
    example: |
      电商领域:
      - 用户域 (用户、认证、积分)
      - 商品域 (商品、库存、分类)
      - 交易域 (订单、支付、物流)

  team_boundary:
    description: "服务边界与团队边界对齐"
    rule: "2 pizza team 负责 1-2 个服务"

  low_coupling:
    description: "服务间低耦合"
    metrics: "服务间调用依赖 < 3"
```

## Technology Selection Standards

### 后端技术选型

| 场景 | 推荐技术 | 备选技术 |
|------|----------|----------|
| Web API | Java/Spring Boot, Go | Node.js, Python |
| 高性能 | Go, Rust | Java, C++ |
| 实时处理 | Node.js, Go | Java |
| AI/ML | Python | Go |

### 数据库选型

| 场景 | 推荐技术 | 说明 |
|------|----------|------|
| 事务型数据 | PostgreSQL, MySQL | ACID 事务 |
| 文档存储 | MongoDB | 灵活 Schema |
| 缓存 | Redis | 高性能 |
| 搜索引擎 | Elasticsearch | 全文搜索 |
| 时序数据 | InfluxDB, TimescaleDB | 时序优化 |
| 图数据 | Neo4j | 图关系 |

### 消息队列选型

| 队列 | 特点 | 适用场景 |
|------|------|----------|
| Kafka | 高吞吐、低延迟 | 日志、大数据 |
| RabbitMQ | 丰富路由 | 业务消息 |
| RocketMQ | 事务消息 | 电商交易 |
| Redis Stream | 轻量级 | 简单场景 |

## System Topology Standards

### 典型微服务架构

```
┌─────────────────────────────────────────────────────────────────┐
│                        EXTERNAL CLIENTS                          │
│                    (Web, Mobile, Third-party)                    │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                           API GATEWAY                           │
│              (Authentication, Rate Limit, Routing)               │
└─────────────────────────────────────────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ User Service  │    │Order Service  │    │Product Service│
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  MySQL/Redis  │    │PostgreSQL/Kafka│   │  MongoDB/Redis │
└───────────────┘    └───────────────┘    └───────────────┘
```

### High Availability Architecture

```yaml
# 多可用区部署
high_availability:
  regions:
    - "cn-north-1 (主)"
    - "cn-east-1 (备)"
    - "cn-south-1 (灾备)"

  multi_az:
    enabled: true
    min_azs: 2
    max_azs: 3

  failover:
    automatic: true
    rto: "< 5 minutes"
    rpo: "< 1 minute"
```

## Data Architecture Standards

### 数据管理策略

```yaml
# 分布式数据管理
data_management:
  database_per_service:
    description: "每个服务拥有独立数据库"
    benefits:
      - "服务独立扩展"
      - "故障隔离"
      - "技术自由"

  shared_database:
    description: "多个服务共享数据库"
    use_case: "强相关数据"
    example: "用户和权限共享同一数据库"

  saga_pattern:
    description: "分布式事务处理"
    implementations:
      - "Choreography ( choreography-based saga)"
      - "Orchestration (orchestrator-based saga)"

  cqrs:
    description: "命令查询职责分离"
    command_side: "写入优化"
    query_side: "读取优化"
```

### 数据同步策略

```yaml
data_sync:
  event_sourcing:
    description: "事件溯源"
    storage: "Event Store"
    replay: true

  change_data_capture:
    description: "变更数据捕获"
    tools:
      - "Debezium"
      - "Maxwell"
      - "Canal"

  data_replication:
    description: "数据复制"
    types:
      - "同步复制"
      - "异步复制"
```

## Scalability Design

### 扩展策略

```yaml
scaling_strategies:
  horizontal_scaling:
    description: "水平扩展"
    applicable: "无状态服务"
    metrics:
      - "CPU > 70%"
      - "Memory > 80%"

  vertical_scaling:
    description: "垂直扩展"
    applicable: "数据库"
    limitations: "有上限"

  auto_scaling:
    enabled: true
    metrics:
      - "HPA (Horizontal Pod Autoscaler)"
      - "VPA (Vertical Pod Autoscaler)"
      - "KEDA (Event-driven Scaling)"
```

### 负载均衡策略

```yaml
load_balancing:
  algorithms:
    - "Round Robin"
    - "Least Connections"
    - "IP Hash"
    - "Weighted"

  health_check:
    types:
      - "TCP Check"
      - "HTTP Check"
      - "HTTPS Check"
    interval: "10 seconds"
    timeout: "5 seconds"
```

## Security Design

### 安全架构

```yaml
security_architecture:
  authentication:
    methods:
      - "OAuth 2.0"
      - "JWT"
      - "API Key"

  authorization:
    models:
      - "RBAC"
      - "ABAC"
      - "Zero Trust"

  network_security:
    - "VPC 隔离"
    - "安全组"
    - "网络 ACL"
    - "WAF"

  data_security:
    - "传输加密 (TLS)"
    - "存储加密 (AES-256)"
    - "密钥管理 (KMS)"
```

## Cost Optimization

### 成本评估模型

```yaml
cost_optimization:
  infrastructure:
    - "计算成本 (EC2/ECS)"
    - "存储成本 (EBS/S3)"
    - "网络成本 (数据传输)"
    - "数据库成本 (RDS)"

  optimization_strategies:
    - "使用 Reserved Instance"
    - "使用 Spot Instance"
    - "自动启停"
    - "生命周期策略"
    - "CDN 优化"
```


## Overview

> High-level description of the design-architecture execution process.
>
> This instruction defines the technical approach, key activities, and success criteria for the design-architecture scenario.


## Technical Specifications

> Detailed technical requirements and implementation guidelines for design-architecture.

### Required Tools
- [List required tools and frameworks]

### Environment Requirements
- [List environment prerequisites]

### Configuration Parameters
- [List key configuration parameters]


## Best Practices

> Industry-standard best practices for design-architecture execution.

1. **Practice 1**: Define architecture decision records (ADRs) for key choices
2. **Practice 2**: Model quality attribute scenarios for critical requirements
3. **Practice 3**: Validate architecture against organizational constraints


## Error Handling

> Common error scenarios and resolution strategies for design-architecture.

### Error Category 1
**Symptom**: Architecture does not satisfy key quality attributes
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]

### Error Category 2
**Symptom**: Stakeholders reject architecture due to misalignment
**Cause**: [Root cause]
**Resolution**: [Steps to resolve]


## Quality Standards

> Acceptance criteria and quality gates for design-architecture deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | All quality attributes have verifiable scenarios | Automated check |
| Standard 2 | ADRs are complete with rationale and trade-offs | Automated check |
| Standard 3 | Architecture review achieves stakeholder consensus | Automated check |
