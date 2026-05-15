---
name: design-architecture
description: "架构设计技能包，提供架构模式、微服务拆分、技术选型的专业知识和最佳实践"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [skill, knowledge, architecture]
---
# Architecture Design Skill

## Skill Overview

本技能包提供架构设计的专业知识、最佳实践和常见陷阱，指导AI高质量地完成从需求到架构设计的转换。

### Core Competencies

- **架构模式**: 掌握微服务、事件驱动、六边形架构等多种架构风格
- **微服务拆分**: 基于DDD和业务边界进行合理的服务拆分
- **技术选型**: 平衡技术先进性、团队技能和长期维护成本
- **容量规划**: 估算QPS、实例数、数据库容量等关键指标
- **可用性设计**: 设计高可用系统，满足SLA要求
- **架构评估**: 系统化评估架构方案的可行性和风险

## Use When

使用此技能的场景：

- 新项目启动，需要进行系统架构设计
- 现有系统需要重构或迁移到新架构
- 业务规模扩大，需要评估架构扩展性
- 技术栈升级，需要重新评估架构方案

## Instructions

### 步骤 1：业务需求分析

**目标**: 理解业务用例、核心功能域和质量属性要求

**操作方法**:
1. **业务用例识别**: 从需求规格中提取核心用户角色和业务流程
2. **功能域划分**: 识别主要业务能力（如用户管理、订单处理、支付等）
3. **质量属性提取**: 明确性能、可用性、安全性、可扩展性等要求
4. **约束条件整理**: 记录技术约束、预算限制、时间要求

**检查点**:
- [ ] 核心业务能力已识别（至少3-5个）
- [ ] 质量属性指标明确（QPS、延迟、可用率等）
- [ ] 约束条件完整记录

---

### 步骤 2：架构风格选择

**目标**: 根据业务规模和复杂度选择合适的架构风格

**操作方法**:
1. **评估业务规模**: 用户量、交易量、数据量
2. **评估团队规模**: 开发团队人数、运维能力
3. **评估复杂度**: 业务逻辑复杂度、集成复杂度
4. **选择架构风格**: 
   - 小型项目 → 单体架构
   - 中大型项目 → 微服务架构
   - 高并发异步场景 → 事件驱动架构
   - 弹性需求强 → Serverless架构

**架构风格对比**:
| 风格 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| 单体 | 小型项目、MVP | 简单、易部署 | 扩展性差、耦合高 |
| 微服务 | 大型复杂系统 | 独立扩展、技术多样 | 分布式复杂度高 |
| 事件驱动 | 高并发异步 | 解耦、弹性好 | 调试困难、一致性挑战 |
| Serverless | 弹性需求强 | 按需付费、免运维 | 冷启动、供应商锁定 |

**检查点**:
- [ ] 架构风格与业务规模匹配
- [ ] 架构风格与团队能力匹配
- [ ] 已记录选择理由（ADR）

---

### 步骤 3：微服务拆分

**目标**: 基于业务能力和领域边界进行合理的服务拆分

**操作方法**:
1. **业务能力映射**: 将业务能力映射到候选服务
2. **DDD限界上下文**: 使用DDD方法识别限界上下文
3. **服务粒度评估**: 
   - 粗粒度（按业务域）→ 适合初期
   - 中粒度（按子域）→ 平衡复杂度
   - 细粒度（按聚合根）→ 高度解耦
4. **服务依赖分析**: 绘制服务依赖图，识别循环依赖
5. **服务边界验证**: 确保低耦合、高内聚

**拆分原则**:
- **单一职责**: 每个服务只负责一个业务能力
- **独立部署**: 服务可以独立部署和扩展
- **数据隔离**: 每个服务有自己的数据存储
- **API契约**: 服务间通过明确的API交互

**检查点**:
- [ ] 服务边界清晰，无职责重叠
- [ ] 服务间耦合度低（依赖数<5）
- [ ] 每个服务可独立部署
- [ ] 无循环依赖

---

### 步骤 4：技术栈选型

**目标**: 为每个技术层级选择合适的技术方案

**操作方法**:
1. **前端技术选型**: 
   - Web框架：React/Vue/Angular
   - 移动端：React Native/Flutter/Native
2. **后端技术选型**:
   - 语言：Java/Go/Node.js/Python
   - 框架：Spring Boot/Gin/Express/Django
3. **数据技术选型**:
   - 关系型：MySQL/PostgreSQL
   - NoSQL：MongoDB/Cassandra
   - 缓存：Redis/Memcached
4. **基础设施选型**:
   - 容器：Docker/Kubernetes
   - 云服务：AWS/阿里云/华为云
   - CI/CD：Jenkins/GitLab CI/GitHub Actions

**选型标准**:
- **成熟度**: 社区活跃度、生产案例
- **团队熟悉度**: 学习曲线、培训成本
- **性能**: 基准测试结果
- **成本**: 许可证费用、运维成本
- **长期支持**: 厂商支持、版本迭代

**检查点**:
- [ ] 每个技术选型都有明确理由
- [ ] 备选方案已评估
- [ ] 团队具备实施能力或培训计划
- [ ] 技术风险已识别

---

### 步骤 5：容量规划

**目标**: 估算系统容量需求，确定资源配额

**操作方法**:
1. **QPS估算**:
   ```
   QPS = (峰值用户数 × 每用户请求数) / 峰值持续时间
   例如：10000用户 × 10请求/用户 / 60秒 = 1667 QPS
   ```
2. **实例数估算**:
   ```
   实例数 = (目标QPS / 单实例容量) × 冗余系数(1.5)
   例如：(1667 / 500) × 1.5 = 5实例
   ```
3. **数据库容量估算**:
   ```
   年增长率 = 当前数据量 × 月增长率 × 12
   3年容量 = (当前数据 + 年增长 × 3) × 1.5余量
   ```
4. **存储容量估算**: 考虑日志、备份、临时文件

**检查点**:
- [ ] QPS估算有依据（历史数据或行业基准）
- [ ] 实例数考虑了冗余和弹性
- [ ] 数据库容量规划覆盖3年
- [ ] 成本估算在预算范围内

---

### 步骤 6：可用性设计

**目标**: 设计高可用系统，满足SLA要求

**操作方法**:
1. **SLA目标设定**:
   - 99% → 3.65天停机/年
   - 99.9% → 8.76小时停机/年
   - 99.99% → 52.6分钟停机/年
   - 99.999% → 5.26分钟停机/年
2. **冗余策略**:
   - 多副本部署
   - 多可用区（AZ）
   - 多区域（Region）
3. **故障转移**:
   - 自动健康检查
   - 快速故障检测
   - 自动切换
4. **降级策略**:
   - 熔断器保护
   - 优雅降级
   - 限流保护

**检查点**:
- [ ] SLA目标与业务需求匹配
- [ ] 无单点故障
- [ ] 故障转移机制已设计
- [ ] 降级策略已定义

---

### 步骤 7：架构文档输出

**目标**: 生成完整的架构设计文档

**操作方法**:
1. **架构图绘制**:
   - 系统上下文图
   - 容器图（服务列表）
   - 组件图（内部结构）
   - 部署图（基础设施）
2. **接口契约定义**:
   - REST API规范
   - gRPC proto定义
   - 事件模式（Event Schema）
3. **ADR编写**:
   - Context（背景）
   - Decision（决策）
   - Rationale（理由）
   - Alternatives（备选方案）
   - Consequences（后果）
4. **风险评估**:
   - 技术风险
   - 运维风险
   - 安全风险

**检查点**:
- [ ] 架构图清晰，符合C4模型
- [ ] 接口契约完整
- [ ] ADR文档规范
- [ ] 风险评估全面

## Core Knowledge

### Architecture Patterns

**Microservices Architecture**:
- **Characteristics**: Independent deployment, loose coupling, technology diversity
- **Benefits**: Independent scaling, fault isolation, team autonomy
- **Challenges**: Distributed complexity, service governance, data consistency

**Event-Driven Architecture**:
- **Components**: Event Producer, Event Channel (MQ), Event Consumer
- **Patterns**: Publish-Subscribe, Event Sourcing, CQRS
- **Benefits**: Decoupling, scalability, real-time processing

**Hexagonal Architecture**:
- **Layers**: Domain (core business), Application (use cases), Infrastructure (adapters)
- **Benefits**: Business logic isolation, testability, technology agnostic

### Service Decomposition Methods

**By Business Capability**:
- Identify core business capabilities
- Map each capability to a service
- Example: E-commerce → User Service, Product Service, Order Service, Payment Service

**By Domain-Driven Design**:
- Identify Bounded Contexts
- Define Context Maps
- Implement Anti-Corruption Layers

**By Team Structure**:
- Two Pizza Rule (6-10 people per team)
- 1-2 services per team
- Independent deployment capability

### Capacity Planning Formulas

**QPS Estimation**:
```
QPS = (Peak Users × Requests per User) / Peak Duration (seconds)
```

**Instance Count**:
```
Instances = (Target QPS / Capacity per Instance) × Redundancy Factor (1.5)
```

**Database Capacity**:
```
Yearly Growth = Current Size × Monthly Growth Rate × 12
3-Year Capacity = (Current + Yearly Growth × 3) × 1.5 Buffer
```

### Availability Levels

| SLA Target | Downtime/Year | Required Strategies |
|------------|---------------|---------------------|
| 99% | 3.65 days | Basic redundancy |
| 99.9% | 8.76 hours | Multi-AZ, health checks |
| 99.99% | 52.6 minutes | Multi-region, auto-failover |
| 99.999% | 5.26 minutes | Active-active, instant failover |

## Best Practices

### 1. Start Simple, Evolve Gradually

**Practice Description**: Begin with a simpler architecture and evolve as needed, avoiding premature optimization.

**Rationale**: Over-engineering increases complexity and cost without immediate benefits.

**How to Apply**:
- Start with modular monolith for MVP
- Extract services when clear boundaries emerge
- Monitor and measure before scaling

---

### 2. Design for Failure

**Practice Description**: Assume components will fail and design resilience mechanisms.

**Rationale**: Distributed systems inevitably experience failures; designing for them improves reliability.

**How to Apply**:
- Implement circuit breakers
- Design retry mechanisms with exponential backoff
- Use bulkheads to isolate failures
- Plan graceful degradation

---

### 3. Document Architecture Decisions (ADR)

**Practice Description**: Record all significant architecture decisions with context and rationale.

**Rationale**: ADRs provide historical context and prevent repeating past mistakes.

**ADR Template**:
```markdown
# ADR-XXX: [Decision Title]

## Context
[What is the issue that we're seeing?]

## Decision
[What is the change that we're proposing?]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Consequences
[What becomes easier or more difficult to do?]
```

---

### 4. Validate with POC

**Practice Description**: Prove critical technical assumptions through Proof of Concept before full implementation.

**Rationale**: Reduces risk of choosing inappropriate technologies.

**POC Checklist**:
- Performance benchmarks
- Integration feasibility
- Team learning curve
- Cost implications

---

### 5. Consider Operational Complexity

**Practice Description**: Evaluate the operational burden of architectural choices.

**Rationale**: Complex architectures require sophisticated monitoring, logging, and debugging tools.

**Operational Considerations**:
- Monitoring and alerting strategy
- Logging aggregation
- Distributed tracing
- Deployment automation
- Incident response procedures

---

### 6. Plan for Data Consistency

**Practice Description**: Choose appropriate consistency models for distributed data.

**Rationale**: Strong consistency impacts performance; eventual consistency requires careful design.

**Consistency Strategies**:
- Saga pattern for distributed transactions
- Event sourcing for audit trails
- CQRS for read-write separation
- Compensation transactions for rollback

## Common Pitfalls

### Pitfall 1: Over-Engineering with Microservices

**Risk**: Splitting into too many microservices too early, creating unnecessary complexity.

**Prevention**:
- Start with modular monolith
- Extract services only when clear boundaries exist
- Ensure team can handle distributed complexity

**Impact**: Increased operational overhead, debugging difficulty, higher costs

---

### Pitfall 2: Ignoring Network Latency

**Risk**: Not accounting for network latency in distributed systems, leading to poor performance.

**Prevention**:
- Measure actual latency between services
- Minimize synchronous calls
- Use async communication where possible
- Implement caching strategies

**Impact**: Slow response times, poor user experience, cascading failures

---

### Pitfall 3: Shared Database Anti-Pattern

**Risk**: Multiple services sharing the same database, creating tight coupling.

**Prevention**:
- Each service owns its data
- Use API for cross-service data access
- Implement event-driven data synchronization
- Avoid database joins across services

**Impact**: Tight coupling, deployment dependencies, data integrity issues

---

### Pitfall 4: Insufficient Observability

**Risk**: Deploying distributed systems without proper monitoring, logging, and tracing.

**Prevention**:
- Implement centralized logging (ELK/Splunk)
- Use distributed tracing (Jaeger/Zipkin)
- Set up comprehensive metrics (Prometheus/Grafana)
- Define clear alerting thresholds

**Impact**: Difficult debugging, slow incident response, unknown system state

## Related Assets

- **Scenario**: [../scenarios/design-architecture/SCENARIO.md](../scenarios/design-architecture/SCENARIO.md)
- **Agent**: [../agents/design-architecture.agent.md](../agents/design-architecture.agent.md)
- **Prompt**: [../prompts/design-architecture.prompt.md](../prompts/design-architecture.prompt.md)
- **Instruction**: [../instructions/design-architecture.instructions.md](../instructions/design-architecture.instructions.md)
