---
name: design-architecture
description: "架构设计提示词，用于设计系统高层架构、微服务拆分、技术选型和系统拓扑"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: [prompt, architecture, design]
---
# Design Architecture Prompt

## Purpose

本提示词指导AI执行架构设计任务，设计系统高层架构，包括微服务拆分、技术选型、系统拓扑和数据架构。

### Key Objectives

- **合理的微服务拆分**: 基于业务能力和领域边界进行服务拆分
- **科学的技术选型**: 平衡技术先进性、团队技能和长期维护成本
- **清晰的系统拓扑**: 定义服务间通信、数据流和部署架构
- **完整的架构文档**: 输出包含架构图、接口契约和ADR的完整文档

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `requirements_spec` | string | true | - | 需求规格说明书路径或内容 | 文件存在或内容有效 |
| `project_type` | enum | true | - | 项目类型 | web-app/mobile-api/iot-platform/ecommerce |
| `team_size` | number | true | - | 团队规模（人数） | 正整数 |
| `estimated_users` | number | false | 10000 | 预估用户数 | 正整数 |
| `peak_concurrency` | number | false | 1000 | 峰值并发数 | 正整数 |
| `availability_target` | number | false | 99.9 | 可用性目标(%) | 99-99.999之间 |
| `latency_target_p99` | number | false | 500 | P99延迟目标(ms) | 正整数 |
| `budget_range` | string | false | - | 预算范围 | 描述性字符串 |
| `timeline` | string | false | - | 项目时间线 | 描述性字符串 |
| `existing_constraints` | array | false | [] | 现有约束条件 | 技术栈、合规要求等 |
| `team_skills` | array | false | [] | 团队技能列表 | 字符串数组 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的架构设计输入
project_name: "电商平台系统"
requirements_spec: "docs/requirements-spec.md"
project_type: "ecommerce"
team_size: 8
estimated_users: 100000
peak_concurrency: 5000
availability_target: 99.95
latency_target_p99: 300
budget_range: "100-150万元"
timeline: "6个月"
existing_constraints:
  - "必须使用阿里云基础设施"
  - "需要符合PCI DSS支付安全标准"
  - "前端必须支持移动端和PC端"
team_skills:
  - "Java/Spring Boot"
  - "React"
  - "MySQL"
  - "Redis"
  - "Docker/Kubernetes"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解业务需求和约束
   ├─ 输入: requirements_spec, project_type, existing_constraints
   ├─ 思考: 业务用例是什么？核心功能域有哪些？质量属性要求？
   ├─ 验证: 与需求规格对照，确认理解准确
   └─ 输出: 业务需求分析摘要
   ↓
[ANALYZE] Step 2: 分析技术需求和约束
   ├─ 输入: estimated_users, peak_concurrency, availability_target, team_skills
   ├─ 思考: 性能指标是否合理？团队技能是否匹配？预算和时间约束？
   ├─ 验证: 评估现有技术栈、外部依赖、合规要求
   └─ 输出: 技术约束分析报告
   ↓
[DESIGN] Step 3: 设计系统架构
   ├─ 输入: 业务需求分析、技术约束分析
   ├─ 思考: 采用什么架构风格？如何拆分微服务？技术栈如何选型？
   ├─ 验证: 架构是否符合业务需求？服务边界是否清晰？
   └─ 输出: 初步架构设计方案（架构图+服务列表+技术栈）
   ↓
[EVALUATE] Step 4: 评估备选方案
   ├─ 输入: 初步架构设计方案
   ├─ 思考: 有哪些备选方案？各方案的优缺点？成本和风险？
   ├─ 验证: 进行技术可行性分析和成本效益分析
   └─ 输出: 方案对比分析（至少2个备选方案）
   ↓
[DOCUMENT] Step 5: 输出架构文档
   ├─ 生成系统架构图、服务交互图、数据流图
   ├─ 定义接口契约（内部接口、外部API规范）
   ├─ 编写架构决策记录（ADR）和技术选型理由
   └─ 输出: 完整的架构设计文档
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织架构评审会议，收集干系人反馈
   ├─ 根据反馈修订架构设计
   ├─ 获得关键干系人签字确认
   └─ 生成交接上下文，准备移交详细设计阶段
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 服务边界不清晰

**识别信号**: 
- 服务间耦合严重，频繁跨服务调用
- 多个服务操作同一数据表
- 服务职责重叠或模糊

**处理流程**:
```
IF 检测到服务边界不清晰
THEN
  1. 重新分析业务能力和领域边界
  2. 使用DDD方法识别限界上下文
  3. 调整服务拆分粒度
  4. 重构服务接口，减少跨服务依赖
  5. 验证新边界的合理性（低耦合、高内聚）
END
```

**降级方案**: 暂时接受当前边界，但标记为“待优化”，在后续迭代中重构

**升级条件**: 经过2次调整后服务间耦合仍然严重，需要架构委员会介入评审

---

### Error Scenario 2: 技术选型不合理

**识别信号**: 
- 技术无法满足性能或可用性要求
- 团队缺乏该技术的关键技能
- 社区支持不足或学习曲线陡峭

**处理流程**:
```
IF 检测到技术选型不合理
THEN
  1. 重新评估技术需求和约束条件
  2. 列出备选技术方案（至少2个）
  3. 进行POC测试关键指标
  4. 对比各方案的优缺点
  5. 选择最优方案并更新技术选型文档
  6. 记录架构决策理由（ADR）
END
```

**降级方案**: 采用更成熟稳定的替代方案，即使功能稍弱但风险更低

**升级条件**: 所有备选方案都无法满足核心需求，需要重新审视业务目标

---

### Error Scenario 3: 性能指标不达标

**识别信号**: 
- 架构设计无法支持目标QPS或延迟要求
- 单点瓶颈明显，无法水平扩展
- 数据一致性机制导致性能下降过多

**处理流程**:
```
IF 检测到性能指标不达标
THEN
  1. 分析性能瓶颈位置（计算、IO、网络、数据库）
  2. 评估优化方案：缓存、读写分离、异步处理、分库分表
  3. 估算优化后的性能提升幅度
  4. IF 优化后仍不达标 THEN 考虑调整架构风格（事件驱动、CQRS）
  5. 重新进行性能基准测试
  6. 更新架构设计文档
END
```

**降级方案**: 降低非核心功能的性能要求，优先保障核心业务流程

**升级条件**: 经过多轮优化仍无法满足SLA要求，需要业务方调整预期

## Output Validation (输出验证)

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### Validation Checklist

**V-001: Architecture Completeness (架构完整性)**
- [ ] 所有架构视图已完成（逻辑、物理、开发、进程视图）
- [ ] 每个服务都有明确的边界和职责定义
- [ ] 接口契约完整（请求/响应格式、错误码、超时设置）
- [ ] 部署架构包含所有环境（开发、测试、生产）

**V-002: Design Consistency (设计一致性)**
- [ ] 术语和命名在整个架构文档中保持一致
- [ ] 架构图与文字描述一致
- [ ] 技术选型与团队技能匹配
- [ ] 与其他相关文档（需求规格、数据库设计）协调一致

**V-003: Technical Feasibility (技术可行性)**
- [ ] 所有关键技术都经过POC验证
- [ ] 性能指标可通过基准测试达到
- [ ] 预算和时间约束可满足
- [ ] 团队具备实施能力或可获取培训

**V-004: Scalability & Resilience (可扩展性和韧性)**
- [ ] 架构支持水平扩展
- [ ] 无单点故障
- [ ] 数据分片策略合理
- [ ] 缓存策略有效

**V-005: Compliance & Standards (规范性和标准)**
- [ ] 遵循架构设计最佳实践（如12-Factor App）
- [ ] 符合安全和合规要求
- [ ] ADR文档格式规范
- [ ] 架构图使用标准符号

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items
  2. Attempt to fix based on available information
  3. IF cannot fix THEN mark as [NEEDS REVIEW] with explanation
  4. Generate validation report with pass/fail status
  5. Highlight critical issues requiring immediate attention
END
```

## Output Format (输出格式)

> AI必须按照以下结构生成架构设计文档

```markdown
# Architecture Design Document

## 1. Executive Summary
- Project Name: {project_name}
- Architecture Type: {monolith/microservices/event-driven/serverless}
- Deployment Target: {cloud/on-premise/hybrid}
- Version: 1.0
- Date: {current_date}

## 2. Business Requirements Analysis

### 2.1 Core Business Capabilities
{列出核心业务能力}

### 2.2 Quality Attribute Requirements
| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Availability | {target}% | SLA monitoring |
| Latency (P99) | < {ms}ms | Performance testing |
| Throughput | {QPS} QPS | Load testing |

## 3. Architecture Overview

### 3.1 Architecture Style
{描述采用的架构风格及理由}

### 3.2 System Context Diagram
{系统上下文图说明}

## 4. Service Decomposition

### 4.1 Service List
| Service Name | Type | Team | Tech Stack | Description |
|--------------|------|------|------------|-------------|
| {service-1} | core/frontend/backend | {team} | {tech} | {description} |

### 4.2 Service Boundaries
{描述每个服务的职责和边界}

### 4.3 Service Interaction Diagram
{服务交互图说明}

## 5. Technology Stack

### 5.1 Frontend Technologies
| Layer | Technology | Version | Rationale |
|-------|------------|---------|----------|
| Framework | {framework} | {version} | {reason} |

### 5.2 Backend Technologies
{后端技术栈列表}

### 5.3 Data Technologies
{数据技术栈列表}

### 5.4 Infrastructure Technologies
{基础设施技术栈列表}

## 6. Data Architecture

### 6.1 Database Design
| Database | Type | Purpose | Data Volume |
|----------|------|---------|-------------|
| {db-name} | {type} | {purpose} | {volume} |

### 6.2 Data Flow Diagram
{数据流图说明}

### 6.3 Data Consistency Strategy
{数据一致性策略}

## 7. Deployment Architecture

### 7.1 Infrastructure Topology
{基础设施拓扑说明}

### 7.2 Environment Configuration
| Environment | Instances | Resources | Purpose |
|-------------|-----------|-----------|---------|
| Production | {count} | {resources} | Live traffic |

### 7.3 CI/CD Pipeline
{CI/CD流程说明}

## 8. Interface Contracts

### 8.1 Internal APIs
{内部API规范}

### 8.2 External APIs
{外部API规范}

### 8.3 Event Schemas
{事件模式定义}

## 9. Architecture Decision Records (ADR)

### ADR-001: {Decision Title}
- **Context**: {背景}
- **Decision**: {决策}
- **Rationale**: {理由}
- **Alternatives Considered**: {备选方案}
- **Consequences**: {后果}

## 10. Risk Assessment

### 10.1 Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | High/Medium/Low | High/Medium/Low | {mitigation} |

### 10.2 Operational Risks
{运维风险}

## 11. Cost Estimation

### 11.1 Infrastructure Costs
- Monthly: ${amount}
- Yearly: ${amount}

### 11.2 Development Costs
- Initial Development: ${amount}
- Ongoing Maintenance: ${amount}/month

## 12. Validation Summary

- Architecture Review Status: {passed/pending}
- Security Review Status: {passed/pending}
- Performance Benchmark: {results}
- Stakeholder Sign-off: {yes/no}
```

## Handover Context (交接上下文)

> 完成架构设计后，生成以下交接信息给详细设计阶段

```yaml
handover:
  header:
    from_stage: "architecture-design"
    to_stage: "system-design"
    handover_id: "HO-{{timestamp}}-ARCH"
    timestamp: "{{ISO8601}}"
    prepared_by: "Solution Architect Agent"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    architecture_type: "microservices/monolith/event-driven"
    total_services: {{count}}
    
  artifacts:
    delivered:
      - name: "Architecture Design Document"
        path: "docs/architecture/design.md"
        version: "1.0"
        sections:
          - Business Requirements Analysis
          - Architecture Overview
          - Service Decomposition
          - Technology Stack
          - Data Architecture
          - Deployment Architecture
          - Interface Contracts
          - ADRs
          - Risk Assessment
          
  metrics:
    total_services: {{count}}
    core_services: {{count}}
    supporting_services: {{count}}
    databases: {{count}}
    external_integrations: {{count}}
    adrs_documented: {{count}}
    risks_identified: {{count}}
    
  decisions:
    - id: "DC-001"
      description: "Architecture style selection"
      rationale: "Microservices chosen for scalability and team autonomy"
      alternatives_considered: ["Monolith", "Modular Monolith"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Some service boundaries need refinement during implementation"
        impact: "May require minor refactoring"
        owner: "System Designer"
        
  risks:
    - id: "RISK-001"
      description: "Team lacks experience with selected technology stack"
      probability: "medium"
      impact: "high"
      mitigation: "Schedule training sessions and POC before full implementation"
      
  recommendations:
    - "Start with core services first to validate architecture"
    - "Implement comprehensive monitoring from day one"
    - "Establish clear API versioning strategy"
    - "Plan for gradual migration if replacing legacy system"
    
  next_steps:
    - "Begin detailed system design for each service"
    - "Set up development environment and CI/CD pipeline"
    - "Create initial database schemas"
    - "Define coding standards and best practices"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/design-architecture/SCENARIO.md` | 架构设计场景定义 |
| Agent | `../agents/design-architecture.agent.md` | 架构设计Agent角色 |
| Skill | `../skills/design-architecture/SKILL.md` | 架构设计技能包 |
| Instruction | `../instructions/design-architecture.instructions.md` | 架构设计技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [ADR Template](../standards/adr-template.md) - 架构决策记录模板
  - [12-Factor App](../standards/12-factor-app.md) - 云原生应用设计原则
- **Templates**: 
  - [Architecture Document Template](../templates/architecture-doc.template.md) - 架构文档模板
  - [Service Boundary Definition](../templates/service-boundary.template.md) - 服务边界定义模板
- **Evaluations**: 
  - [Architecture Review Checklist](../evaluations/architecture-review-checklist.md) - 架构评审检查清单

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "decompose-task"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "design-architecture"
  summary:
    status: completed|partial|blocked
    quality_score: {0-100}
  artifacts:
    delivered: []
  decisions: []
  open_issues:
    blocking: []
    non_blocking: []
  risks: []
  quality_metrics:
    kpi_results: []
  recommendations: []
```
