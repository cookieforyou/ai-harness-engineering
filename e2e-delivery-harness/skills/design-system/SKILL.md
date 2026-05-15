---
name: design-system
description: "系统设计技能包，提供架构设计、技术选型、模块划分的专业知识和最佳实践"
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [skill, knowledge, design]
---
# System Design Skill

## Skill Overview

本技能包提供系统设计的专业知识、最佳实践和常见陷阱，指导AI高质量地完成从需求规格到系统架构设计的转换。

### Core Competencies

- **架构设计**: 掌握单体、微服务、事件驱动等多种架构风格
- **技术选型**: 平衡技术先进性、团队技能和长期维护成本
- **模块划分**: 遵循单一职责原则，实现高内聚低耦合
- **接口设计**: 设计稳定、可扩展的API契约
- **风险评估**: 识别技术风险并制定应对策略

## Use When

使用此技能的场景：

- 需求分析完成后，需要进行技术架构设计
- 系统需要重构或重大技术升级
- 新技术选型需要评估和决策
- 跨系统集成需要架构层面的规划
- 性能瓶颈需要架构级优化

## Instructions

### 步骤 1：需求理解与分析

**目标**: 深入理解业务需求和技术约束

**操作方法**:
1. **功能需求提取**
   - 从需求规格说明书中提取所有功能需求（FR）
   - 为每个FR编号并分类（核心/重要/一般）
   - 识别功能间的依赖关系

2. **非功能性需求量化**
   - 性能指标：响应时间（P50/P95/P99）、吞吐量（QPS/TPS）
   - 可用性指标：SLA目标（99%/99.9%/99.99%）
   - 安全性要求：认证授权、数据加密、合规标准
   - 可扩展性：预期用户增长、数据量增长

3. **约束条件识别**
   - 技术约束：必须使用的技术栈、云平台限制
   - 资源约束：预算上限、团队规模、时间要求
   - 合规要求：GDPR、ISO 27001、行业标准

4. **业务流程梳理**
   - 绘制核心业务流程图
   - 识别关键路径和瓶颈点
   - 确定业务优先级

**检查点**:
- [ ] 所有FR已提取并编号
- [ ] 所有NFR已量化
- [ ] 核心业务流程清晰
- [ ] 约束条件完整记录

---

### 步骤 2：架构风格选择

**目标**: 评估并选择适合项目特点的架构风格

**操作方法**:
1. **调研可选架构风格**
   - **单体架构（Monolithic）**: 简单、易部署，适合小型项目
   - **微服务架构（Microservices）**: 独立扩展、技术多样，适合大型复杂系统
   - **事件驱动架构（Event-Driven）**: 解耦、异步处理，适合高并发场景
   - **分层架构（Layered）**: 清晰分层，适合传统企业应用
   - **六边形架构（Hexagonal）**: 业务逻辑与基础设施分离，易于测试

2. **评估各风格与项目的匹配度**
   - 业务复杂度适配性
   - 团队规模适配性
   - 扩展性需求匹配度
   - 运维成本和复杂度

3. **考虑团队能力和运维成本**
   - 团队现有技术栈和经验
   - 学习曲线和培训成本
   - 运维团队能力

4. **做出决策并记录理由**
   - 选择最优方案
   - 记录备选方案和权衡分析
   - 编写ADR（Architecture Decision Record）

**架构风格对比表**:
| 标准 | 单体 | 微服务 | 事件驱动 |
|------|------|--------|----------|
| 业务复杂度适配 | 低-中 | 高 | 中-高 |
| 团队规模要求 | 小（<10人） | 大（>15人） | 中（10-15人） |
| 扩展性 | 有限 | 优秀 | 良好 |
| 运维成本 | 低 | 高 | 中 |
| 开发效率 | 高（初期） | 中 | 中 |

**检查点**:
- [ ] 至少评估了3种架构风格
- [ ] 决策矩阵完整
- [ ] ADR已编写
- [ ] 备选方案已记录

---

### 步骤 3：模块划分与组件设计

**目标**: 划分系统组件并定义各组件的职责

**操作方法**:
1. **按业务领域划分模块**
   - 识别核心业务域（用户、订单、商品等）
   - 应用DDD（领域驱动设计）方法
   - 定义限界上下文（Bounded Context）

2. **按层次划分组件**
   - **表现层（Presentation）**: API网关、Web界面
   - **业务逻辑层（Business Logic）**: 核心业务逻辑
   - **数据访问层（Data Access）**: DAO/Repository
   - **基础设施层（Infrastructure）**: 日志、监控、配置

3. **识别共享组件和基础组件**
   - 认证授权服务
   - 日志监控服务
   - 配置管理服务
   - 消息队列服务

4. **定义模块的边界和职责**
   - 单一职责原则（SRP）
   - 明确输入输出
   - 定义依赖关系

5. **设计模块间的协作关系**
   - 同步调用（REST/gRPC）
   - 异步消息（Message Queue）
   - 事件通知（Event Bus）

**检查点**:
- [ ] 模块划分符合单一职责原则
- [ ] 模块间耦合度低
- [ ] 依赖关系清晰
- [ ] 组件图已绘制

---

### 步骤 4：技术栈选型

**目标**: 为每个技术层级选择合适的技术方案

**操作方法**:
1. **后端技术选型**
   - 编程语言：Java/Go/Node.js/Python
   - Web框架：Spring Boot/Gin/Express/Django
   - RPC框架：gRPC/Thrift

2. **前端技术选型**
   - Web框架：React/Vue/Angular
   - 移动端：React Native/Flutter/Native
   - 状态管理：Redux/MobX/Vuex

3. **数据技术选型**
   - 关系型数据库：MySQL/PostgreSQL
   - NoSQL数据库：MongoDB/Cassandra
   - 缓存：Redis/Memcached
   - 搜索引擎：Elasticsearch

4. **基础设施选型**
   - 容器化：Docker + Kubernetes
   - 云服务：AWS/阿里云/华为云
   - CI/CD：Jenkins/GitLab CI/GitHub Actions

5. **评估和决策**
   - 对比备选方案（功能、性能、成本、风险）
   - 进行POC验证关键技术
   - 记录技术选型理由（ADR）

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

### 步骤 5：数据模型设计

**目标**: 设计核心数据实体和关系

**操作方法**:
1. **实体识别**
   - 从业务流程中提取核心实体
   - 定义实体属性（基本属性、业务属性、系统属性）
   - 确定主键候选字段

2. **关系建模**
   - 确定实体间关系类型：1:1、1:N、M:N
   - 绘制ER图
   - 标注关系的基数（Cardinality）

3. **数据存储策略**
   - 关系型数据库：结构化数据、事务要求高
   - NoSQL数据库：半结构化数据、高扩展性
   - 缓存层：热点数据、高频读取
   - 对象存储：文件、图片、视频

4. **数据流设计**
   - 数据写入流程
   - 数据读取流程
   - 数据同步机制（主从复制、CDC）

**检查点**:
- [ ] 核心实体已识别
- [ ] 关系已定义
- [ ] ER图已绘制
- [ ] 存储策略合理

---

### 步骤 6：接口设计规范

**目标**: 定义模块间和对外的接口

**操作方法**:
1. **API设计原则**
   - RESTful规范：资源命名、HTTP方法、状态码
   - 版本控制：URL版本（/v1/）、Header版本
   - 幂等性：GET/PUT/DELETE天然幂等，POST需特殊处理

2. **接口契约定义**
   - 请求格式：参数类型、必填项、默认值
   - 响应格式：数据结构、错误码、分页
   - 异常处理：错误码规范、错误消息

3. **通信协议选择**
   - **REST**: 外部API、简单易用
   - **gRPC**: 内部服务、高性能
   - **GraphQL**: 灵活查询、前端友好
   - **消息队列**: 异步处理、解耦

4. **接口文档编写**
   - OpenAPI/Swagger规范
   - 示例请求和响应
   - 认证授权说明

**检查点**:
- [ ] API设计规范
- [ ] 接口文档完整
- [ ] 版本兼容性已考虑
- [ ] 错误码规范统一

---

### 步骤 7：部署架构设计

**目标**: 设计部署拓扑和安全策略

**操作方法**:
1. **部署拓扑设计**
   - 开发环境：单机或轻量级集群
   - 测试环境：模拟生产环境
   - 生产环境：高可用集群

2. **高可用设计**
   - 多副本部署
   - 负载均衡
   - 故障转移
   - 健康检查

3. **安全策略设计**
   - 认证授权：OAuth2/JWT
   - 数据加密：TLS传输加密、AES存储加密
   - 访问控制：RBAC/ABAC
   - 审计日志：记录所有操作

4. **CI/CD流程设计**
   - 代码提交触发构建
   - 自动化测试
   - 镜像构建和推送
   - 自动化部署

**检查点**:
- [ ] 部署拓扑满足高可用要求
- [ ] 安全策略完整
- [ ] CI/CD流程清晰
- [ ] 监控和告警已设计

---

### 步骤 8：风险分析与应对

**目标**: 识别技术风险并制定应对措施

**操作方法**:
1. **风险识别**
   - 技术风险：新技术不确定性、性能瓶颈
   - 运维风险：复杂性增加、监控挑战
   - 安全风险：数据泄露、未授权访问
   - 依赖风险：第三方服务、开源项目

2. **风险评估**
   - 概率：高/中/低
   - 影响：高/中/低
   - 风险等级：概率 × 影响

3. **应对策略**
   - **规避**: 改变计划以消除风险
   - **转移**: 将风险转嫁给第三方
   - **缓解**: 降低风险概率或影响
   - **接受**: 接受风险并准备应急计划

4. **风险监控**
   - 定期审查风险状态
   - 更新风险登记册
   - 触发应急预案

**检查点**:
- [ ] 所有风险已识别
- [ ] 风险评估完整
- [ ] 应对策略可行
- [ ] 风险监控机制已建立

## Core Knowledge

### Architecture Patterns

**Monolithic Architecture**:
- **Characteristics**: Single codebase, unified deployment
- **Benefits**: Simple development, easy debugging, low ops cost
- **Challenges**: Scaling limitations, tight coupling, long build times
- **Best For**: Small teams, simple applications, MVPs

**Microservices Architecture**:
- **Characteristics**: Independent services, decentralized data management
- **Benefits**: Independent scaling, technology diversity, fault isolation
- **Challenges**: Distributed complexity, service governance, data consistency
- **Best For**: Large teams, complex applications, high scalability needs

**Event-Driven Architecture**:
- **Characteristics**: Asynchronous communication, event sourcing
- **Benefits**: Loose coupling, scalability, real-time processing
- **Challenges**: Debugging difficulty, eventual consistency, event ordering
- **Best For**: High concurrency, real-time systems, complex workflows

### SOLID Principles

**Single Responsibility Principle (SRP)**:
- Each module should have one reason to change
- Apply to modules, classes, and functions

**Open/Closed Principle (OCP)**:
- Open for extension, closed for modification
- Use interfaces and abstraction

**Liskov Substitution Principle (LSP)**:
- Subtypes must be substitutable for their base types
- Ensure behavioral compatibility

**Interface Segregation Principle (ISP)**:
- Many specific interfaces are better than one general-purpose interface
- Avoid fat interfaces

**Dependency Inversion Principle (DIP)**:
- Depend on abstractions, not concretions
- Use dependency injection

### API Design Best Practices

**RESTful Design**:
- Use nouns for resources (/users, /orders)
- Use HTTP methods correctly (GET, POST, PUT, DELETE)
- Use appropriate status codes (200, 201, 400, 404, 500)
- Version your APIs (/v1/users)

**Error Handling**:
- Consistent error response format
- Meaningful error messages
- Appropriate HTTP status codes
- Error codes for programmatic handling

**Security**:
- Authentication (OAuth2, JWT)
- Authorization (RBAC, ABAC)
- Rate limiting
- Input validation

## Best Practices

### 1. Start Simple, Evolve Gradually

**Practice Description**: Begin with a simpler architecture and evolve as needed, avoiding premature optimization.

**Rationale**: Over-engineering increases complexity and cost without immediate benefits.

**How to Apply**:
- Start with modular monolith for MVP
- Extract services when clear boundaries emerge
- Monitor and measure before scaling

---

### 2. Document All Architecture Decisions (ADR)

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

### 3. Design for Failure

**Practice Description**: Assume components will fail and design resilience mechanisms.

**Rationale**: Distributed systems inevitably experience failures; designing for them improves reliability.

**How to Apply**:
- Implement circuit breakers
- Design retry mechanisms with exponential backoff
- Use bulkheads to isolate failures
- Plan graceful degradation

---

### 4. Prioritize Observability

**Practice Description**: Build monitoring, logging, and tracing into the architecture from day one.

**Rationale**: You can't improve what you can't measure; observability is critical for operational success.

**How to Apply**:
- Centralized logging (ELK/Splunk)
- Distributed tracing (Jaeger/Zipkin)
- Comprehensive metrics (Prometheus/Grafana)
- Clear alerting thresholds

---

### 5. Validate with POC

**Practice Description**: Prove critical technical assumptions through Proof of Concept before full implementation.

**Rationale**: Reduces risk of choosing inappropriate technologies.

**POC Checklist**:
- Performance benchmarks
- Integration feasibility
- Team learning curve
- Cost implications

---

### 6. Consider Operational Complexity

**Practice Description**: Evaluate the operational burden of architectural choices.

**Rationale**: Complex architectures require sophisticated monitoring, logging, and debugging tools.

**Operational Considerations**:
- Monitoring and alerting strategy
- Logging aggregation
- Distributed tracing
- Deployment automation
- Incident response procedures

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

### Pitfall 3: Insufficient API Versioning Strategy

**Risk**: Breaking changes in APIs cause client failures and deployment coordination issues.

**Prevention**:
- Implement API versioning from day one
- Use semantic versioning
- Maintain backward compatibility
- Deprecate old versions gracefully

**Impact**: Client breakage, deployment complexity, customer dissatisfaction

---

### Pitfall 4: Neglecting Security in Early Design

**Risk**: Adding security later is much harder and often results in vulnerabilities.

**Prevention**:
- Design authentication and authorization from the start
- Encrypt sensitive data at rest and in transit
- Implement input validation and sanitization
- Regular security audits

**Impact**: Data breaches, compliance violations, reputation damage

## Related Assets

- **Scenario**: [../scenarios/design-system/SCENARIO.md](../scenarios/design-system/SCENARIO.md)
- **Agent**: [../agents/design-system.agent.md](../agents/design-system.agent.md)
- **Prompt**: [../prompts/design-system.prompt.md](../prompts/design-system.prompt.md)
- **Instruction**: [../instructions/design-system.instructions.md](../instructions/design-system.instructions.md)
