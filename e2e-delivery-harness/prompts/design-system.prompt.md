---
name: design-system
description: 系统架构设计提示词，用于将需求规格转换为技术架构设计方案
type: execution
version: "1.2.0"
stage: "system-design"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [design, architecture, technical]
---

# Design System Architecture - Execution Prompt

> **版本**: 1.2.0 | **适用阶段**: 系统设计 | **预计工时**: 4-8小时
> 
> **重要**: 此 Prompt 为 AI 执行的完整脚本，必须严格按照以下步骤执行

## Task Description

基于需求规格说明书，设计系统的整体架构、技术方案和数据模型，为开发实现提供技术指导。

**核心目标**:
- 选择合适的架构风格（单体/微服务/事件驱动等）
- 设计清晰的模块划分和组件交互
- 定义完整的数据模型和接口规范
- 识别技术风险并制定应对策略

**成功标准**:
- 所有功能需求都有对应的设计实现
- 非功能性需求（性能、安全、可用性）得到满足
- 设计方案可落地实施且在团队能力范围内
- 技术评审通过率 ≥90%

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `requirements_spec` | string | true | - | 需求规格说明书内容 | 长度 > 100字符，包含功能和非功能需求 |
| `tech_stack_preference` | array | false | [] | 技术栈偏好列表 | 有效的技术名称 |
| `team_capabilities` | array | false | [] | 团队技术能力列表 | 有效的技能描述 |
| `budget` | string | false | "unlimited" | 预算限制 | 有效的金额描述 |
| `timeline` | string | false | "flexible" | 时间限制 | 有效的时间描述 |
| `compliance_requirements` | array | false | [] | 合规要求列表 | 行业标准或法规 |

### Variable Examples

```yaml
requirements_spec: |
  ## 功能需求
  FR-001: 用户注册登录
  FR-002: 商品管理
  ## 非功能需求
  NFR-001: 响应时间 < 200ms
  NFR-002: 可用率 99.9%

tech_stack_preference:
  - "Java"
  - "Spring Boot"
  - "MySQL"

team_capabilities:
  - "微服务架构经验"
  - "Vue3 前端开发"

budget: "100万以内"
timeline: "3个月内完成"

compliance_requirements:
  - "GDPR"
  - "ISO 27001"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 分析需求约束和技术要求
   ├─ 输入: requirements_spec
   ├─ 思考: 系统的核心业务场景是什么？非功能性需求有哪些？
   ├─ 验证: 所有需求都已理解且无歧义
   └─ 输出: 需求分析摘要
   ↓
Step 2: [ANALYZE] 选择架构风格和模块划分
   ├─ 输入: 需求分析摘要 + tech_stack_preference
   ├─ 思考: 单体还是微服务？如何划分模块边界？
   ├─ 验证: 架构风格满足业务需求和团队能力
   └─ 输出: 架构风格选择和模块划分方案
   ↓
Step 3: [DESIGN] 设计组件架构和数据模型
   ├─ 输入: 模块划分方案
   ├─ 思考: 组件职责是否单一？数据流是否清晰？
   ├─ 验证: 符合单一职责原则，数据模型满足业务场景
   └─ 输出: 组件架构图 + ER图
   ↓
Step 4: [IMPLEMENT] 定义接口规范和部署策略
   ├─ 输入: 组件架构图
   ├─ 思考: 接口契约是否清晰？部署拓扑如何设计？
   ├─ 验证: 接口稳定可扩展，部署方案可行
   └─ 输出: API 接口规格 + 部署架构图
   ↓
Step 5: [VERIFY] 验证设计方案完整性和一致性
   ├─ 输入: 所有设计文档
   ├─ 执行: Output Validation Checklist
   ├─ 验证: 所有检查项通过
   └─ 输出: 最终设计文档 + 验证报告
   ↓
Step 6: [HANDOVER] 准备交接给任务拆分阶段
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: Task Decomposer Agent
```

## Execution Flow (执行流程)

### Phase 1: Analysis (需求分析)

**目标**: 深入理解需求和约束条件

**步骤**:
1. 阅读需求规格说明书
   - 操作: 提取功能需求清单
   - 验证: 确认无遗漏
2. 分析非功能性需求
   - 操作: 量化性能、安全、可用性指标
   - 验证: 指标可测量
3. 识别约束条件
   - 操作: 列出技术、预算、时间约束
   - 验证: 约束明确具体

**产出**: 需求分析摘要文档

### Phase 2: Architecture Design (架构设计)

**目标**: 选择合适的架构风格并进行模块划分

**步骤**:
1. 评估架构选项
   - 操作: 对比单体/微服务/事件驱动等
   - 验证: 根据业务场景选择
2. 划分模块边界
   - 操作: 按业务领域或功能模块划分
   - 验证: 符合单一职责原则
3. 确定技术栈
   - 操作: 结合团队能力和项目需求
   - 验证: 技术成熟度评估

**产出**: 架构设计方案

### Phase 3: Detailed Design (详细设计)

**目标**: 完成组件、数据和接口的详细设计

**步骤**:
1. 设计组件架构
   - 操作: 绘制组件图，定义职责
   - 验证: 组件间耦合度低
2. 设计数据模型
   - 操作: 创建 ER 图，定义数据字典
   - 验证: 满足业务场景
3. 定义接口规范
   - 操作: 编写 API 文档，定义协议
   - 验证: 接口稳定可扩展

**产出**: 详细设计文档

### Phase 4: Deployment & Security (部署与安全)

**目标**: 设计部署拓扑和安全策略

**步骤**:
1. 设计部署架构
   - 操作: 绘制部署图，规划拓扑
   - 验证: 满足高可用要求
2. 制定安全策略
   - 操作: 设计认证授权、数据加密
   - 验证: 符合安全标准

**产出**: 部署和安全设计文档

### Phase 5: Risk Analysis (风险分析)

**目标**: 识别技术风险并制定应对措施

**步骤**:
1. 识别风险点
   - 操作: 列出所有潜在技术风险
   - 验证: 评估概率和影响
2. 制定应对策略
   - 操作: 为每个风险制定缓解措施
   - 验证: 策略可行有效

**产出**: 风险分析报告

### Phase 6: Validation (验证阶段)

**目标**: 验证所有产出符合质量标准

**步骤**:
1. 执行 Output Validation Checklist
2. 记录验证结果
3. 处理未通过的检查项

**产出**: 验证报告

## Output Format (输出格式)

> **AI 必须严格遵循以下输出格式**，不得随意更改结构

```markdown
# System Architecture Design Document

## Executive Summary

- **Status**: [completed | partial | blocked]
- **Completion**: {percentage}%
- **Quality Score**: {score}/100
- **Duration**: {execution_time}
- **Architecture Style**: {单体/微服务/事件驱动}
- **Key Technologies**: {技术栈列表}

## 1. Document Information

- **Project Name**: {项目名称}
- **Version**: 1.0
- **Date**: {当前日期}
- **Status**: Draft/Review/Final
- **Author**: {设计师姓名}

## 2. Design Scope & Objectives

### 2.1 Design Scope
{明确设计涵盖的系统范围}

### 2.2 Design Goals
| Goal | Description | Priority |
|------|-------------|----------|
| Goal 1 | {描述} | High |
| Goal 2 | {描述} | Medium |

### 2.3 Constraints
- {约束1}
- {约束2}
- {约束3}

## 3. Architecture Overview

### 3.1 Architecture Style
**Selected Style**: {架构风格}

**Rationale**:
{选择该架构风格的理由}

**Alternatives Considered**:
- {备选方案1}: {优缺点}
- {备选方案2}: {优缺点}

### 3.2 Technology Stack

| Layer | Technology | Version | Rationale |
|-------|-----------|---------|-----------|
| Frontend | Vue3 | 3.x | 团队熟悉，生态完善 |
| Backend | Spring Boot | 2.7+ | 成熟稳定，社区活跃 |
| Database | MySQL | 8.0 | 事务支持，性能优秀 |
| Cache | Redis | 7.x | 高性能缓存 |

### 3.3 Design Principles
1. {原则1: 如单一职责原则}
2. {原则2: 如开闭原则}
3. {原则3: 如依赖倒置原则}

## 4. System Architecture

### 4.1 Architecture Diagram

```
[在此处使用文字描述或 Mermaid 语法绘制架构图]

例如:
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Client    │────▶│  API Gateway │────▶│   Service   │
│  (Web/Mobile)│     │              │     │   Layer     │
└─────────────┘     └──────────────┘     └─────────────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │   Data      │
                                        │   Layer     │
                                        └─────────────┘
```

### 4.2 Module Decomposition

| Module | Responsibility | Technology | Dependencies |
|--------|---------------|------------|--------------|
| User Module | 用户管理、认证授权 | Spring Security | Database |
| Product Module | 商品管理、库存 | Spring Boot | Database, Cache |
| Order Module | 订单处理、支付 | Spring Boot | Database, Message Queue |

### 4.3 Component Interactions

{描述组件间的交互关系，包括:
- 同步调用 (REST/gRPC)
- 异步消息 (Message Queue)
- 事件驱动 (Event Bus)
}

## 5. Data Architecture

### 5.1 Data Model

**Core Entities**:

| Entity | Attributes | Relationships |
|--------|-----------|---------------|
| User | id, username, email, password | Has many Orders |
| Product | id, name, price, stock | Belongs to Category |
| Order | id, user_id, total, status | Has many OrderItems |

### 5.2 Storage Strategy

| Data Type | Storage Solution | Rationale |
|-----------|-----------------|-----------|
| Structured Data | MySQL | ACID transactions, relational queries |
| Session Data | Redis | Fast access, TTL support |
| File Storage | OSS/S3 | Scalable, cost-effective |

### 5.3 Data Flow

{描述数据在系统中的流动:
1. 用户请求 → API Gateway → Service → Database
2. 数据变更 → Event Bus → Cache Invalidation
3. 异步处理 → Message Queue → Worker Service
}

## 6. Interface Design

### 6.1 API List

| API Name | Method | Path | Description | Auth Required |
|----------|--------|------|-------------|---------------|
| User Login | POST | /api/v1/auth/login | 用户登录 | No |
| Get Products | GET | /api/v1/products | 获取商品列表 | Yes |
| Create Order | POST | /api/v1/orders | 创建订单 | Yes |

### 6.2 API Specification

#### API: User Login

**Endpoint**: `POST /api/v1/auth/login`

**Request**:
```json
{
  "username": "string",
  "password": "string"
}
```

**Response** (Success - 200):
```json
{
  "code": 0,
  "data": {
    "token": "jwt_token_string",
    "expiresIn": 3600,
    "user": {
      "id": 1,
      "username": "john"
    }
  },
  "message": "Login successful"
}
```

**Response** (Error - 401):
```json
{
  "code": 1001,
  "data": null,
  "message": "Invalid credentials"
}
```

**Error Codes**:
| Code | Description | Action |
|------|-------------|--------|
| 1001 | Invalid credentials | Show error message |
| 1002 | Account locked | Contact admin |

## 7. Deployment Architecture

### 7.1 Deployment Topology

```
[在此处描述部署拓扑]

Production Environment:
- Load Balancer (Nginx)
- API Gateway (Kong)
- Application Servers (3 instances)
- Database Cluster (Master-Slave)
- Redis Cluster (3 nodes)
- Message Queue (RabbitMQ Cluster)
```

### 7.2 Deployment Strategy

- **Environments**: Dev → Staging → Production
- **Method**: Blue-Green Deployment
- **Configuration**: Centralized (Consul/Apollo)
- **CI/CD**: Jenkins/GitLab CI

### 7.3 Scaling Strategy

- **Horizontal Scaling**: Auto-scaling based on CPU/Memory
- **Database Scaling**: Read replicas for read-heavy workloads
- **Cache Strategy**: Multi-level caching (L1: Local, L2: Redis)

## 8. Security Design

### 8.1 Authentication & Authorization

| Module | Authentication | Authorization |
|--------|---------------|---------------|
| API Layer | JWT Token | RBAC |
| Admin Panel | OAuth2 + MFA | Role-based |

### 8.2 Data Security

- **Transport Encryption**: TLS 1.2+
- **Storage Encryption**: AES-256 for sensitive data
- **Sensitive Data**: Password (bcrypt), PII (encrypted at rest)
- **Audit Logging**: All critical operations logged

## 9. Risk Analysis

### 9.1 Technical Risks

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| New technology learning curve | Medium | Medium | Training + PoC phase |
| Third-party dependency stability | High | Low | Backup providers + monitoring |
| Performance bottleneck | High | Medium | Load testing + optimization |

### 9.2 Mitigation Measures

1. **Technology Validation**: Conduct PoC for new technologies
2. **Monitoring**: Implement comprehensive monitoring and alerting
3. **Backup Plan**: Prepare fallback solutions for critical components

## 10. Key Design Decisions (ADRs)

| Decision ID | Decision | Options | Selected | Rationale |
|------------|----------|---------|----------|-----------|
| ADR-001 | Architecture Style | Monolith vs Microservices | Microservices | Scalability, team structure |
| ADR-002 | Database | MySQL vs PostgreSQL | MySQL | Team expertise, ecosystem |
| ADR-003 | Message Queue | RabbitMQ vs Kafka | RabbitMQ | Simpler ops, sufficient performance |

## 11. Implementation Plan

### 11.1 Milestones

| Milestone | Timeline | Deliverables |
|-----------|----------|--------------|
| M1: Foundation | Week 1-2 | Project setup, CI/CD, basic modules |
| M2: Core Features | Week 3-6 | User, Product, Order modules |
| M3: Integration | Week 7-8 | API integration, testing |
| M4: Deployment | Week 9-10 | Production deployment, monitoring |

### 11.2 Priority

1. **P0**: User authentication, core business logic
2. **P1**: Product management, order processing
3. **P2**: Advanced features, optimizations

## 12. Appendix

### 12.1 Glossary

| Term | Definition |
|------|-----------|
| ADR | Architecture Decision Record |
| RBAC | Role-Based Access Control |
| JWT | JSON Web Token |

### 12.2 References

- [Spring Boot Documentation](https://spring.io/projects/spring-boot)
- [Microservices Patterns](https://microservices.io/)
- [OWASP Security Guidelines](https://owasp.org/)

## Validation Report

### V-001: Requirements Coverage Check
- [ ] All functional requirements have corresponding design
- [ ] All non-functional requirements are addressed
- [ ] All constraints are respected
- **Status**: [PASS/FAIL]

### V-002: Architecture Quality Check
- [ ] Module decomposition follows single responsibility principle
- [ ] Component dependencies are clear and minimal
- [ ] Interface contracts are well-defined
- **Status**: [PASS/FAIL]

### V-003: Feasibility Check
- [ ] Technology stack is within team capabilities
- [ ] Implementation timeline is realistic
- [ ] Risks have mitigation strategies
- **Status**: [PASS/FAIL]

### V-004: Completeness Check
- [ ] Architecture diagram is clear and complete
- [ ] API definitions are detailed
- [ ] Data model is consistent
- **Status**: [PASS/FAIL]

### Validation Summary
- **Total Checks**: 12
- **Passed**: {number}
- **Failed**: {number}
- **Overall Status**: [PASS/FAIL]



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Context

```yaml
handover:
  from_stage: "system-design"
  to_stage: "task-decomposition"
  status: "completed"
  
  artifacts:
    - name: "System Architecture Document"
      path: "docs/architecture-design.md"
      version: "1.0.0"
    - name: "API Specification"
      path: "docs/api-spec.yaml"
      version: "1.0.0"
    - name: "Data Model"
      path: "docs/data-model.md"
      version: "1.0.0"
  
  decisions:
    - id: "ADR-001"
      description: "Selected microservices architecture"
      rationale: "Better scalability and team autonomy"
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Performance testing needed for high-load scenarios"
        planned_resolution: "Schedule load testing in Week 8"
        
  risks:
    - id: "RISK-001"
      description: "Team needs training on new technology stack"
      probability: "medium"
      impact: "medium"
      mitigation: "Arrange training sessions in Week 1"
      
  recommendations:
    - "Start with core modules to validate architecture"
    - "Implement comprehensive logging from day one"
    - "Set up monitoring before production deployment"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: 95
        target: 95
        status: "pass"
      - kpi_id: "KPI-002"
        value: 100
        target: 100
        status: "pass"
```
```

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Classification

| Level | Code | Description | Action |
|-------|------|-------------|--------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: Requirements-Design Mismatch

**识别信号**: 发现某些需求无法通过当前设计方案实现

**处理流程**:
```
IF 需求与设计不匹配
THEN
  1. 明确指出不匹配的具体需求
  2. 分析原因（技术限制/资源不足/需求冲突）
  3. 提出替代方案或建议调整需求
  4. 标记为 [设计冲突-需确认]
  5. IF 影响核心功能 THEN 升级到产品经理和架构师
END
```

**降级方案**: 暂时标注为已知问题，在 Handover 中说明

**升级条件**: 影响核心功能实现或需要重大架构调整

### Error Scenario 2: Technology Selection Uncertainty

**识别信号**: 多个技术选项都可接受，难以决策

**处理流程**:
```
IF 技术选型不确定
THEN
  1. 列出所有可行选项及其优缺点
  2. 根据团队能力、项目约束、社区支持评分
  3. 选择综合得分最高的方案
  4. 记录决策理由和备选方案
  5. 建议在实施前进行 PoC 验证
END
```

**降级方案**: 选择团队最熟悉的技术，降低风险

**升级条件**: 团队无法达成共识或风险等级为 High

### Error Scenario 3: Component Boundary Ambiguity

**识别信号**: 组件职责重叠或边界不清晰

**处理流程**:
```
IF 组件边界不清晰
THEN
  1. 重新分析业务领域边界
  2. 应用单一职责原则重新划分
  3. 明确定义组件间的契约和依赖
  4. 更新架构图和文档
  5. 征求团队成员反馈
END
```

**降级方案**: 暂时保持现状，在后续迭代中重构

**升级条件**: 导致严重的耦合或维护困难

### Error Logging

每次遇到错误必须记录:
```yaml
error_log:
  - error_id: "ERR-{timestamp}-{sequence}"
    timestamp: "{{ISO8601}}"
    level: "P0/P1/P2/P3"
    type: "{错误类型}"
    description: "{详细描述}"
    action_taken: "{采取的行动}"
    result: "resolved/unresolved/escalated"
```

## Output Validation (输出验证)

> **在生成最终输出前，AI 必须完成以下验证步骤**

### Mandatory Validation Checklist

**V-001: Completeness Validation**
- [ ] All required sections are present (Sections 1-12)
- [ ] Architecture diagram is included
- [ ] API specifications are detailed
- [ ] Data model is complete
- [ ] No placeholder text remains

**V-002: Consistency Validation**
- [ ] Terminology is consistent throughout
- [ ] Technology stack is consistent across sections
- [ ] Module names match between diagram and description
- [ ] API paths follow consistent naming convention

**V-003: Accuracy Validation**
- [ ] All calculations (e.g., capacity planning) are correct
- [ ] Technology versions are current and compatible
- [ ] Security measures follow industry standards
- [ ] All assumptions are documented

**V-004: Quality Validation**
- [ ] Design meets all functional requirements
- [ ] Non-functional requirements are addressed
- [ ] Risks are identified with mitigation strategies
- [ ] Design is feasible within team capabilities

### Validation Failure Protocol

```
IF any validation check fails
THEN
  1. Document the failed check and reason
  2. Assess severity (P0/P1/P2/P3)
  3. For P0/P1: MUST fix before proceeding
  4. For P2/P3: Can document as known issue with justification
  5. Re-run validation until all checks pass or are accepted
  6. Record final validation status
END
```

### Self-Assessment

AI must provide a self-assessment:
- **Confidence Level**: [High/Medium/Low]
- **Areas of Uncertainty**: {list any uncertainties}
- **Recommendations for Human Review**: {what needs human attention}

## Constraints & Requirements (约束与要求)

### Mandatory Constraints

1. **Language**: 输出使用中文，技术术语可保留英文
2. **Format**: 严格遵循上述 Markdown 格式
3. **Completeness**: 所有章节必须填写，不可留空
4. **Feasibility**: 设计必须在团队能力和预算范围内可实施
5. **Standards**: 遵循行业最佳实践和安全标准

### Quality Requirements

| Requirement | Standard | Verification Method |
|-------------|----------|--------------------|
| Requirements Coverage | 100% | Traceability matrix |
| Architecture Quality | ≥85/100 | Architecture review checklist |
| Risk Management | All major risks identified | Risk register completeness |
| Feasibility | Within team capabilities | Team capability assessment |

### Performance Expectations

- **Execution Time**: 4-8 hours
- **Document Length**: 20-40 pages
- **Accuracy Target**: ≥95%

## Examples (示例)

### Example: E-commerce Platform Architecture

**Input**:
```yaml
requirements_spec: |
  ## Functional Requirements
  - User registration and login
  - Product browsing and search
  - Shopping cart and checkout
  - Order tracking
  
  ## Non-Functional Requirements
  - Response time < 200ms
  - Availability 99.9%
  - Support 10,000 concurrent users

tech_stack_preference:
  - "Java"
  - "Spring Boot"
  - "MySQL"
  
team_capabilities:
  - "Microservices experience"
  - "Vue3 frontend"
```

**Expected Output**:
完整的系统架构设计文档，包含:
- 微服务架构图
- 用户、商品、订单等服务模块设计
- MySQL 数据库 schema
- RESTful API 规范
- 部署拓扑和扩容策略

**Key Learnings**:
- 微服务架构适合电商平台的独立扩展需求
- 需要重点关注服务间通信和数据一致性
- 缓存策略对性能至关重要

## Tone and Style Guidelines

- **Tone**: Professional, objective, technical
- **Voice**: Active voice preferred
- **Terminology**: Use standard industry terms, define acronyms
- **Formatting**: 
  - Use tables for structured data
  - Use code blocks for technical specifications
  - Use diagrams (Mermaid/ASCII) for visual representation
  - Bold key decisions and important points

## References

- Related Scenario: [scenarios/design-system/SCENARIO.md](../../scenarios/design-system/SCENARIO.md)
- Related Skill: [skills/design-system/SKILL.md](../../skills/design-system/SKILL.md)
- Related Instruction: [instructions/design-system.instructions.md](../../instructions/design-system.instructions.md)
- Standards: [standards/asset-model.md](../../standards/asset-model.md)

---

**Prompt Version**: 1.2.0  
**Last Updated**: 2026-05-07  
**Author**: AI Harness Engineering Team
