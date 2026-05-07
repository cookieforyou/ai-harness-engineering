---
name: design-system
description: 将需求规格转换为技术架构设计方案，包括组件设计、接口设计、数据设计和部署架构
category: design
version: "1.2.0"
type: skill
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [design, architecture, technical]
---

# System Design Skill

## Use When

使用此技能的场景：

- ✅ 需求分析完成后，需要进行技术架构设计
- ✅ 系统需要重构或重大技术升级
- ✅ 新技术选型需要评估和决策
- ✅ 跨系统集成需要架构层面的规划
- ✅ 性能瓶颈需要架构级优化

**前置条件**:
- 需求规格说明书已完成并评审通过
- 明确了技术约束和业务目标
- 有足够的时间进行架构设计（通常 4-8 小时）

## Expected Input

### Required Inputs

| Input | Type | Format | Description | Validation |
|-------|------|--------|-------------|------------|
| `requirements_spec` | File | Markdown | 来自需求分析阶段的输出 | 包含功能和非功能需求 |
| `design_constraints` | Text | String | 技术约束和标准 | 明确具体 |

### Optional Inputs

| Input | Type | Format | Description |
|-------|------|--------|-------------|
| `team_capabilities` | Text | List | 团队的技术栈和能力情况 |
| `resource_limits` | Text | Object | 时间和人力的限制条件 |
| `historical_designs` | File | Markdown | 相关的历史设计文档 |
| `integration_requirements` | Text | List | 外部系统集成要求 |

## Instructions

> **AI 必须严格按照以下步骤执行**，每步完成后进行自我验证

### Step 1: Requirements Understanding & Decomposition

**Objective**: 深入理解业务需求和技术约束

**Actions**:
1. 阅读需求规格说明书
   - 提取所有功能需求 (FR)
   - 提取所有非功能需求 (NFR)
   - 识别业务优先级
2. 梳理核心业务流程
   - 绘制业务流程图
   - 识别关键路径
3. 识别关键性能指标
   - 响应时间要求
   - 并发用户数
   - 可用率目标
4. 理解数据处理需求
   - 数据类型和规模
   - 数据一致性要求
   - 数据安全要求
5. 确定设计边界和假设
   - 明确系统边界
   - 列出所有假设条件

**Validation Checklist**:
- [ ] 所有 FR 已提取并编号
- [ ] 所有 NFR 已量化
- [ ] 核心业务流程清晰
- [ ] 性能指标可测量
- [ ] 设计边界明确

**Output**: Requirements Analysis Summary

---

### Step 2: Architecture Style Selection

**Objective**: 评估并选择适合项目特点的架构风格

**Actions**:
1. 调研可选架构风格
   - 单体架构 (Monolithic)
   - 微服务架构 (Microservices)
   - 事件驱动架构 (Event-Driven)
   - 分层架构 (Layered)
   - 六边形架构 (Hexagonal)
2. 评估各风格与项目的匹配度
   - 业务复杂度适配性
   - 团队规模适配性
   - 扩展性需求匹配度
3. 考虑团队能力和运维成本
   - 团队现有技术栈
   - 学习曲线
   - 运维复杂度
4. 做出决策并记录理由
   - 选择最优方案
   - 记录备选方案
   - 编写 ADR (Architecture Decision Record)

**Decision Matrix**:

| Criteria | Monolith | Microservices | Event-Driven |
|----------|----------|---------------|--------------|
| Complexity Fit | Low-Medium | High | Medium-High |
| Team Size | Small | Large | Medium |
| Scalability | Limited | Excellent | Good |
| Ops Cost | Low | High | Medium |

**Validation Checklist**:
- [ ] 至少评估了 3 种架构风格
- [ ] 决策矩阵完整
- [ ] ADR 已编写
- [ ] 备选方案已记录

**Output**: Architecture Style Decision Document

---

### Step 3: Component Design

**Objective**: 划分系统组件并定义各组件的职责

**Actions**:
1. 按业务领域划分组件
   - 识别核心业务域
   - 应用 DDD (Domain-Driven Design)
   - 定义限界上下文 (Bounded Context)
2. 按层次划分组件
   - 表现层 (Presentation)
   - 业务逻辑层 (Business Logic)
   - 数据访问层 (Data Access)
   - 基础设施层 (Infrastructure)
3. 识别共享组件和基础组件
   - 认证授权服务
   - 日志监控服务
   - 配置管理服务
4. 定义组件的边界和职责
   - 单一职责原则
   - 明确输入输出
   - 定义依赖关系
5. 设计组件间的协作关系
   - 同步调用 (REST/gRPC)
   - 异步消息 (Message Queue)
   - 事件通知 (Event Bus)

**Component Diagram Example**:
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ API Gateway  │────▶│ User Service │────▶│   Database   │
└──────────────┘     └──────────────┘     └──────────────┘
        │                    │
        ▼                    ▼
┌──────────────┐     ┌──────────────┐
│ Order Service│────▶│ Payment Svc  │
└──────────────┘     └──────────────┘
```

**Validation Checklist**:
- [ ] 组件划分符合单一职责原则
- [ ] 组件间耦合度低
- [ ] 依赖关系清晰
- [ ] 组件图已绘制

**Output**: Component Design Document + Diagram

---

### Step 4: Data Architecture Design

**Objective**: 设计数据模型和存储方案

**Actions**:
1. 设计核心数据模型
   - 识别实体 (Entity)
   - 定义属性 (Attribute)
   - 建立关系 (Relationship)
   - 绘制 ER 图
2. 确定数据存储策略
   - 关系型数据库 (MySQL/PostgreSQL)
   - NoSQL (MongoDB/Cassandra)
   - 缓存 (Redis/Memcached)
   - 对象存储 (S3/OSS)
3. 设计数据流和处理流程
   - 数据写入流程
   - 数据读取流程
   - 数据同步机制
4. 考虑数据安全和隐私保护
   - 敏感数据加密
   - 访问控制
   - 审计日志
5. 设计数据迁移和同步方案
   - 增量同步
   - 全量同步
   - 冲突解决

**ER Diagram Example**:
```
┌──────────┐       ┌──────────┐
│  User    │1    *│  Order   │
├──────────├───────┼──────────┤
│ id       │       │ id       │
│ username │       │ user_id  │
│ email    │       │ total    │
└──────────┘       │ status   │
                   └──────────┘
```

**Validation Checklist**:
- [ ] ER 图完整且规范
- [ ] 存储方案合理
- [ ] 数据安全策略完善
- [ ] 数据流清晰

**Output**: Data Architecture Document + ER Diagram

---

### Step 5: Interface Design

**Objective**: 设计组件间的接口和数据交互

**Actions**:
1. 识别对外接口和内部接口
   - 对外 API (面向客户端)
   - 内部 API (服务间调用)
2. 确定接口协议
   - RESTful API
   - gRPC
   - GraphQL
   - Message Queue (RabbitMQ/Kafka)
3. 设计接口规范和数据格式
   - URL 命名规范
   - HTTP 方法使用
   - 请求/响应格式
   - 错误码定义
4. 定义错误码和异常处理
   - 成功响应 (2xx)
   - 客户端错误 (4xx)
   - 服务端错误 (5xx)
5. 绘制接口交互图
   - 时序图 (Sequence Diagram)
   - 流程图 (Flow Chart)

**API Specification Example**:
```yaml
POST /api/v1/orders
Content-Type: application/json

Request:
{
  "userId": 123,
  "items": [
    {"productId": 456, "quantity": 2}
  ],
  "shippingAddress": "..."
}

Response (201):
{
  "orderId": "ORD-2026-001",
  "status": "created",
  "totalAmount": 199.99
}
```

**Validation Checklist**:
- [ ] 所有接口已识别
- [ ] 协议选择合理
- [ ] 规范文档完整
- [ ] 错误码定义清晰

**Output**: API Specification Document

---

### Step 6: Technology Stack Selection

**Objective**: 确定各组件的技术选型

**Actions**:
1. 根据组件需求选择技术栈
   - 前端框架 (React/Vue/Angular)
   - 后端框架 (Spring Boot/Django/Express)
   - 数据库 (MySQL/PostgreSQL/MongoDB)
   - 缓存 (Redis/Memcached)
   - 消息队列 (RabbitMQ/Kafka)
2. 评估技术的成熟度和风险
   - 社区活跃度
   - 版本稳定性
   - 长期支持 (LTS)
   - 已知问题
3. 考虑团队的技能储备
   - 现有经验
   - 学习成本
   - 培训需求
4. 做出选型决策并记录理由
   - 编写技术选型报告
   - 记录备选方案
   - 评估迁移成本

**Technology Evaluation Matrix**:

| Technology | Maturity | Community | Learning Curve | Risk Level |
|-----------|----------|-----------|----------------|------------|
| Spring Boot | High | Very High | Low | Low |
| Django | High | High | Low | Low |
| Express | High | High | Medium | Low |

**Validation Checklist**:
- [ ] 技术栈覆盖所有组件
- [ ] 评估矩阵完整
- [ ] 选型理由充分
- [ ] 风险已评估

**Output**: Technology Stack Document

---

### Step 7: Deployment Architecture Design

**Objective**: 设计系统的部署拓扑和策略

**Actions**:
1. 设计部署拓扑结构
   - 开发环境
   - 测试环境
   - 预发布环境
   - 生产环境
2. 确定部署策略
   - 滚动部署 (Rolling)
   - 蓝绿部署 (Blue-Green)
   - 灰度发布 (Canary)
3. 设计容灾和备份方案
   - 多可用区部署
   - 数据备份策略
   - 灾难恢复计划
4. 规划扩容和缩容机制
   - 水平扩容 (Horizontal Scaling)
   - 垂直扩容 (Vertical Scaling)
   - 自动扩缩容 (Auto-scaling)
5. 考虑基础设施需求
   - 服务器配置
   - 网络带宽
   - 存储容量

**Deployment Topology Example**:
```
Production Environment:
┌─────────────┐
│ Load Balancer│
└──────┬──────┘
       │
  ┌────┴────┐
  │         │
▼           ▼
┌─────┐  ┌─────┐
│App-1│  │App-2│  (Application Servers)
└──┬──┘  └──┬──┘
   │        │
   └───┬────┘
       ▼
┌──────────┐
│ Database │  (Master-Slave Cluster)
└──────────┘
```

**Validation Checklist**:
- [ ] 部署拓扑清晰
- [ ] 部署策略合理
- [ ] 容灾方案完善
- [ ] 扩容机制可行

**Output**: Deployment Architecture Document

---

### Step 8: Risk Analysis & Mitigation

**Objective**: 识别技术风险并制定应对策略

**Actions**:
1. 识别技术风险
   - 新技术学习曲线
   - 第三方依赖稳定性
   - 性能瓶颈
   - 安全漏洞
   - 集成复杂性
2. 评估风险发生概率和影响
   - 概率: Low/Medium/High
   - 影响: Low/Medium/High
   - 风险等级 = 概率 × 影响
3. 制定风险缓解措施
   - 预防措施 (Preventive)
   - 检测措施 (Detective)
   - 纠正措施 (Corrective)
4. 制定风险应急预案
   - 触发条件
   - 响应流程
   - 责任人

**Risk Register Example**:

| Risk ID | Description | Probability | Impact | Level | Mitigation |
|---------|-------------|-------------|--------|-------|------------|
| RISK-001 | New tech learning curve | Medium | Medium | Medium | Training + PoC |
| RISK-002 | Third-party API instability | Low | High | Medium | Backup provider |

**Validation Checklist**:
- [ ] 所有主要风险已识别
- [ ] 风险评估准确
- [ ] 缓解措施可行
- [ ] 应急预案完善

**Output**: Risk Analysis Report

---

### Step 9: Design Review & Finalization

**Objective**: 评审架构设计方案并完成最终版本

**Actions**:
1. 准备评审材料
   - 架构设计文档
   - 架构图和数据流图
   - 技术选型报告
   - 风险分析报告
2. 组织评审会议
   - 邀请相关人员（架构师、开发、运维）
   - 演示设计方案
   - 收集问题和反馈
3. 收集评审反馈
   - 记录所有问题
   - 分类整理（阻塞/非阻塞）
   - 确定修改优先级
4. 根据反馈修订方案
   - 修复阻塞性问题
   - 优化建议性问题
   - 更新文档
5. 获得评审通过
   - 确认所有问题已解决
   - 获取签字批准
   - 归档最终版本

**Review Checklist**:
- [ ] 评审材料准备完整
- [ ] 所有干系人参与
- [ ] 反馈已记录
- [ ] 问题已修复
- [ ] 评审通过

**Output**: Final Architecture Design Package

---

## Expected Output

### Deliverables

| Artifact | Format | Location | Validation Criteria |
|----------|--------|----------|---------------------|
| Architecture Design Document | Markdown | `docs/architecture-design.md` | All sections complete |
| Component Diagram | Mermaid/PNG | `docs/diagrams/component-diagram.md` | Clear and accurate |
| Data Model (ER Diagram) | Mermaid/PNG | `docs/diagrams/er-diagram.md` | Normalized and complete |
| API Specification | OpenAPI/YAML | `docs/api-spec.yaml` | Follows REST standards |
| Technology Stack Report | Markdown | `docs/tech-stack.md` | Justified selections |
| Deployment Architecture | Markdown + Diagram | `docs/deployment.md` | Production-ready |
| Risk Analysis Report | Markdown | `docs/risk-analysis.md` | All major risks covered |
| Architecture Decision Records | Markdown | `docs/adrs/` | One file per decision |

### Output Structure

```markdown
# System Architecture Design Document

## 1. Executive Summary
- Project overview
- Architecture style selected
- Key technologies

## 2. Design Scope & Objectives
- Business requirements
- Technical constraints
- Success criteria

## 3. Architecture Overview
- Architecture diagram
- Module decomposition
- Design principles

## 4. Component Design
- Component responsibilities
- Interaction patterns
- Dependency graph

## 5. Data Architecture
- Data model (ER diagram)
- Storage strategy
- Data flow

## 6. Interface Design
- API specifications
- Protocol selection
- Error handling

## 7. Technology Stack
- Selected technologies
- Evaluation matrix
- Rationale

## 8. Deployment Architecture
- Deployment topology
- Scaling strategy
- Disaster recovery

## 9. Security Design
- Authentication & authorization
- Data encryption
- Audit logging

## 10. Risk Analysis
- Identified risks
- Mitigation strategies
- Contingency plans

## 11. Implementation Plan
- Milestones
- Timeline
- Resource allocation

## 12. Appendix
- Glossary
- References
- ADRs
```

## Quality Criteria

### Quantitative Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Requirements Coverage | 100% | Traceability matrix |
| Design Completeness | ≥95% | Section checklist |
| Review Pass Rate | ≥90% | Review feedback score |
| Risk Identification | All major risks | Risk register completeness |

### Qualitative Standards

| Dimension | Standard | Verification |
|-----------|----------|--------------|
| Clarity | Easy to understand by team members | Peer review |
| Consistency | Terminology and style uniform | Document review |
| Feasibility | Implementable within constraints | Technical assessment |
| Maintainability | Easy to update and extend | Architecture review |

## Related Assets

- **Scenario**: [../../scenarios/design-system/SCENARIO.md](../../scenarios/design-system/SCENARIO.md)
- **Agent**: [../../agents/design-system.agent.md](../../agents/design-system.agent.md)
- **Instruction**: [../../instructions/design-system.instructions.md](../../instructions/design-system.instructions.md)
- **Prompt**: [../../prompts/design-system.prompt.md](../../prompts/design-system.prompt.md)

## Core Knowledge

### Architecture Patterns

1. **Monolithic Architecture**
   - Single codebase and deployment unit
   - Simple to develop and deploy
   - Limited scalability

2. **Microservices Architecture**
   - Independent services with own databases
   - High scalability and flexibility
   - Complex operations

3. **Event-Driven Architecture**
   - Asynchronous communication via events
   - Loose coupling between components
   - Complex debugging

4. **Layered Architecture**
   - Separation of concerns by layers
   - Clear boundaries
   - Potential performance overhead

### Design Principles

1. **Single Responsibility Principle (SRP)**
   - Each component has one reason to change
   - Improves maintainability

2. **Open-Closed Principle (OCP)**
   - Open for extension, closed for modification
   - Enables safe evolution

3. **Dependency Inversion Principle (DIP)**
   - Depend on abstractions, not concretions
   - Facilitates testing and flexibility

4. **Interface Segregation Principle (ISP)**
   - Many specific interfaces better than one general
   - Reduces unnecessary dependencies

## Best Practices

### Practice 1: Start Simple, Scale Later

**Description**: Begin with the simplest architecture that meets current needs, design for future scalability but don't over-engineer.

**Rationale**: 
- Reduces initial complexity
- Faster time to market
- Easier to understand and maintain
- Can evolve as requirements grow

**Example**: Start with a modular monolith, extract microservices when scaling becomes necessary.

---

### Practice 2: Document Decisions with ADRs

**Description**: Use Architecture Decision Records (ADRs) to document all significant architectural decisions.

**Rationale**:
- Provides historical context
- Helps future team members understand rationale
- Prevents repeating past mistakes
- Facilitates knowledge transfer

**Template**:
```markdown
# ADR-001: [Decision Title]

## Status
Accepted/Rejected/Superseded

## Context
[What is the issue we're addressing?]

## Decision
[What did we decide?]

## Consequences
[What are the positive and negative outcomes?]
```

---

### Practice 3: Design for Failure

**Description**: Assume components will fail and design resilience into the system.

**Rationale**:
- Failures are inevitable in distributed systems
- Resilient systems provide better user experience
- Reduces operational burden

**Techniques**:
- Circuit breakers
- Retry mechanisms with backoff
- Fallback responses
- Graceful degradation

---

### Practice 4: Validate with Prototypes

**Description**: Build small prototypes to validate risky or uncertain architectural decisions.

**Rationale**:
- Reduces uncertainty
- Provides real-world data
- Identifies issues early
- Builds team confidence

**When to Use**:
- New technology adoption
- Complex integrations
- Performance-critical paths
- Unproven architectural patterns

## Common Pitfalls

### Pitfall 1: Over-Engineering

**Risk**: Designing for hypothetical future requirements that may never materialize.

**Symptoms**:
- Excessive abstraction layers
- Premature optimization
- Complex configurations
- Long development time

**Prevention**:
- Focus on current requirements
- Apply YAGNI principle (You Ain't Gonna Need It)
- Iterate and evolve architecture
- Regularly reassess design decisions

**Impact**: Wasted effort, increased complexity, slower delivery

---

### Pitfall 2: Ignoring Operational Concerns

**Risk**: Designing architecture without considering deployment, monitoring, and maintenance.

**Symptoms**:
- Difficult deployment process
- Lack of observability
- Manual operational tasks
- Poor documentation

**Prevention**:
- Involve DevOps team early
- Design for observability (logging, metrics, tracing)
- Automate operational tasks
- Document runbooks

**Impact**: High operational costs, frequent outages, slow incident response

---

### Pitfall 3: Tight Coupling Between Components

**Risk**: Components have strong dependencies, making changes difficult.

**Symptoms**:
- Cascading failures
- Difficult to test in isolation
- Changes require coordinated deployments
- Slow development velocity

**Prevention**:
- Define clear interfaces
- Use dependency injection
- Implement circuit breakers
- Apply loose coupling patterns

**Impact**: Reduced agility, higher risk, slower innovation

---

### Pitfall 4: Insufficient Risk Assessment

**Risk**: Not identifying or underestimating technical risks.

**Symptoms**:
- Surprise issues during implementation
- Missed deadlines
- Budget overruns
- Quality problems

**Prevention**:
- Conduct thorough risk assessment early
- Regular risk reviews
- Maintain risk register
- Have contingency plans

**Impact**: Project delays, cost overruns, quality issues

## Troubleshooting

### Issue 1: Stakeholders Disagree on Architecture

**Symptoms**: Conflicting opinions, decision paralysis.

**Resolution**:
1. Facilitate structured discussion
2. Create decision matrix with objective criteria
3. Build prototypes for competing approaches
4. Escalate to architecture review board if needed

---

### Issue 2: Architecture Doesn't Meet Performance Requirements

**Symptoms**: Performance tests fail, bottlenecks identified.

**Resolution**:
1. Profile to identify actual bottlenecks
2. Optimize critical paths
3. Consider caching strategies
4. Evaluate horizontal scaling options
5. Reassess architecture if fundamental issues

---

### Issue 3: Team Lacks Skills for Chosen Technology

**Symptoms**: Slow progress, low code quality, frustration.

**Resolution**:
1. Arrange training sessions
2. Pair programming with experts
3. Start with simpler components
4. Consider alternative technologies
5. Hire consultants if critical

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.2.0 | 2026-05-07 | Enhanced with standardized structure, added troubleshooting section | AI Harness Team |
| 1.1.0 | 2026-04-01 | Initial version | Original Author |

---

**Skill Version**: 1.2.0  
**Last Updated**: 2026-05-07  
**Author**: AI Harness Engineering Team
