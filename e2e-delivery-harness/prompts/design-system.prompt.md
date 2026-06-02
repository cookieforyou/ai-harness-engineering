---
name: design-system
description: "系统设计提示词，用于将需求规格转换为技术架构设计方案"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, design, architecture]
---
# Design System Prompt

## Purpose

本提示词指导AI执行系统设计任务，基于需求规格说明书设计系统的整体架构、技术方案和数据模型。

### Key Objectives

- **合理的架构选择**: 根据业务需求和团队能力选择合适的架构风格
- **清晰的模块划分**: 遵循单一职责原则，实现高内聚低耦合
- **完整的技术方案**: 包含技术栈选型、数据模型、接口规范
- **可控的技术风险**: 识别潜在风险并制定应对策略

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `requirements_spec` | string | true | - | 需求规格说明书内容 | 长度>100字符，包含功能和非功能需求 |
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `tech_stack_preference` | array | false | [] | 技术栈偏好列表 | 有效的技术名称 |
| `team_capabilities` | array | false | [] | 团队技术能力列表 | 有效的技能描述 |
| `budget` | string | false | "unlimited" | 预算限制 | 有效的金额描述 |
| `timeline` | string | false | "flexible" | 时间限制 | 有效的时间描述 |
| `compliance_requirements` | array | false | [] | 合规要求列表 | GDPR/ISO 27001等 |
| `existing_architecture` | string | false | - | 现有系统架构（改造项目） | 架构描述或文档路径 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的系统设计输入
project_name: "电商平台系统"
requirements_spec: |
  ## 功能需求
  FR-001: 用户注册登录（支持手机号、邮箱）
  FR-002: 商品浏览和搜索
  FR-003: 购物车管理
  FR-004: 订单创建和支付
  FR-005: 订单跟踪
  
  ## 非功能需求
  NFR-001: 响应时间 < 200ms (P95)
  NFR-002: 可用率 99.9%
  NFR-003: 支持10000并发用户
  NFR-004: 符合GDPR隐私保护要求

tech_stack_preference:
  - "Java"
  - "Spring Boot"
  - "MySQL"
  - "Redis"
  
team_capabilities:
  - "微服务架构经验（2年）"
  - "Vue3 前端开发"
  - "Docker/Kubernetes部署"
  
budget: "100万以内"
timeline: "3个月内完成MVP"

compliance_requirements:
  - "GDPR"
  - "PCI DSS（支付安全）"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解系统边界和范围
   ├─ 输入: requirements_spec, project_name
   ├─ 思考: 系统的核心业务场景是什么？外部依赖有哪些？
   ├─ 验证: 与需求规格对照，确认功能清单完整
   └─ 输出: 系统边界分析摘要
   ↓
[ANALYZE] Step 2: 分析非功能性需求和技术约束
   ├─ 输入: requirements_spec, team_capabilities, budget, timeline
   ├─ 思考: 性能指标是否合理？团队能力是否匹配？预算和时间是否充足？
   ├─ 验证: 评估技术可行性、资源充足性
   └─ 输出: 技术约束分析报告
   ↓
[DESIGN] Step 3: 设计系统架构和模块划分
   ├─ 输入: 系统边界分析、技术约束分析
   ├─ 思考: 采用什么架构风格？如何划分模块？技术栈如何选择？
   ├─ 验证: 架构满足非功能性需求，模块高内聚低耦合
   └─ 输出: 初步架构设计方案（架构图+模块列表+技术栈）
   ↓
[EVALUATE] Step 4: 设计数据模型和接口方案
   ├─ 输入: 初步架构设计方案
   ├─ 思考: 核心实体关系如何？接口契约是否稳定？通信协议如何选择？
   ├─ 验证: 数据模型满足业务场景，接口设计规范
   └─ 输出: 数据模型（ER图）+ 接口规范（API文档）
   ↓
[DOCUMENT] Step 5: 输出系统设计文档
   ├─ 生成系统架构图、组件图、部署图
   ├─ 编写技术选型理由和ADR
   ├─ 制定风险分析和应对策略
   └─ 输出: 完整的系统设计文档
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织技术评审会议，收集反馈
   ├─ 根据反馈修订设计方案
   ├─ 获得技术委员会签字确认
   └─ 生成交接上下文，准备移交任务拆分阶段
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 架构决策困难

**识别信号**: 
- 多种架构方案各有优劣，难以抉择
- 团队对架构方向存在分歧
- 技术评估结果不明确

**处理流程**:
```
IF 检测到架构决策困难
THEN
  1. 列出各方案的优缺点对比表（功能、性能、成本、风险）
  2. 根据非功能性需求权重评分（性能30%、可维护性25%、成本20%、风险25%）
  3. 选择综合得分最高的方案
  4. IF 分数接近 THEN 选择团队最熟悉的方案，降低实施风险
  5. 记录决策依据和备选方案评估（ADR）
  6. 提交技术委员会评审确认
END
```

**降级方案**: 采用保守方案（团队最熟悉的），预留重构空间，制定演进路线图

**升级条件**: 团队无法达成共识或风险等级为High，需要CTO或架构委员会介入

---

### Error Scenario 2: 技术风险识别

**识别信号**: 
- 关键技术存在不确定性或团队缺乏经验
- 新技术未经生产环境验证
- 依赖外部因素（第三方服务、开源项目）

**处理流程**:
```
IF 检测到技术风险
THEN
  1. 识别所有技术风险点（新技术、复杂算法、外部依赖）
  2. 评估风险概率和影响（高/中/低）
  3. 制定应对策略：规避/转移/缓解/接受
  4. IF 高风险 THEN 安排POC验证或增加技术预研阶段
  5. 在设计方案中标注风险及应对措施
  6. 更新风险管理文档
END
```

**降级方案**: 采用成熟技术替代，或分阶段实施（先MVP验证，再全面推广）

**升级条件**: 风险等级为High/Critical且无有效缓解措施，需要技术负责人和项目管理者决策

---

### Error Scenario 3: 需求与设计冲突

**识别信号**: 
- 设计方案无法满足某些需求
- 需求之间存在矛盾（如高性能vs低成本）
- 技术约束导致需求调整

**处理流程**:
```
IF 检测到需求与设计冲突
THEN
  1. 分析冲突的根本原因（需求不完整、技术限制、资源不足）
  2. 与Requirement Analyst确认需求优先级和可调整范围
  3. 提出设计调整建议或需求修改建议
  4. IF 影响核心功能 THEN 组织架构评审会议讨论
  5. 记录冲突和解决方案（ADR）
  6. 更新需求规格说明书或设计方案
END
```

**降级方案**: 暂时标注为已知问题，在Handover中说明，留待后续迭代解决

**升级条件**: 影响核心功能实现或需要重大设计变更，需要产品经理和系统设计师共同决策

## Output Validation (输出验证)

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### Validation Checklist

**V-001: Design Completeness (设计完整性)**
- [ ] 所有功能需求都有对应的设计实现
- [ ] 非功能性需求（性能、安全、可用性）得到满足
- [ ] 架构文档包含所有必需章节（概述、架构、模块、数据、接口、部署、风险）
- [ ] 关键设计决策有ADR记录

**V-002: Architecture Consistency (架构一致性)**
- [ ] 术语和命名在整个设计文档中保持一致
- [ ] 架构图与文字描述一致
- [ ] 数据模型与接口定义一致
- [ ] 与其他相关文档（需求规格、数据库设计）协调一致

**V-003: Technical Feasibility (技术可行性)**
- [ ] 技术方案在团队能力范围内
- [ ] 预算和时间约束可满足
- [ ] 技术风险可控，有应对策略
- [ ] 依赖的外部服务或组件可获得

**V-004: Interface Stability (接口稳定性)**
- [ ] API设计规范（RESTful/gRPC标准）
- [ ] 接口版本兼容性已考虑
- [ ] 错误码和异常处理完整
- [ ] 接口文档清晰易懂

**V-005: Compliance & Standards (规范性和标准)**
- [ ] 遵循架构设计最佳实践（SOLID、DRY）
- [ ] 符合安全和合规要求（GDPR、ISO 27001等）
- [ ] 代码结构和命名规范明确
- [ ] 文档格式规范，图表清晰

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

> AI必须按照以下结构生成系统设计文档

```markdown
# System Design Document

## 1. Executive Summary
- Project Name: {project_name}
- Architecture Style: {monolith/microservices/event-driven}
- Technology Stack: {key technologies}
- Version: 1.0
- Date: {current_date}

## 2. Requirements Analysis

### 2.1 Functional Requirements
{列出核心功能需求，映射到设计模块}

### 2.2 Non-Functional Requirements
| Requirement | Target | Measurement |
|-------------|--------|-------------|
| Response Time (P95) | < 200ms | Performance testing |
| Availability | 99.9% | SLA monitoring |
| Concurrent Users | 10,000 | Load testing |

## 3. Architecture Overview

### 3.1 Architecture Style
{描述采用的架构风格及理由}

### 3.2 System Context Diagram
{系统上下文图说明}

### 3.3 Component Architecture
{组件架构图说明}

## 4. Module Design

### 4.1 Module List
| Module Name | Responsibility | Dependencies | Tech Stack |
|-------------|----------------|--------------|------------|
| {module-1} | {responsibility} | {deps} | {tech} |

### 4.2 Module Interaction
{模块间交互图说明}

## 5. Technology Stack

### 5.1 Backend Technologies
| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| Framework | {framework} | {version} | {reason} |
| Language | {language} | {version} | {reason} |

### 5.2 Frontend Technologies
{前端技术栈列表}

### 5.3 Data Technologies
{数据技术栈列表}

### 5.4 Infrastructure Technologies
{基础设施技术栈列表}

## 6. Data Model

### 6.1 Entity Relationship Diagram
{ER图说明或Mermaid代码}

### 6.2 Core Entities
| Entity | Attributes | Relationships |
|--------|------------|---------------|
| {entity-1} | {attributes} | {relationships} |

### 6.3 Data Dictionary
{核心表结构定义}

## 7. Interface Design

### 7.1 API Specifications
{REST API或gRPC接口定义}

### 7.2 Communication Protocols
| Protocol | Use Case | Rationale |
|----------|----------|-----------|
| REST | External APIs | Standard, easy to use |
| gRPC | Internal services | High performance |
| Message Queue | Async processing | Decoupling |

## 8. Deployment Architecture

### 8.1 Deployment Topology
{部署拓扑图说明}

### 8.2 Environment Configuration
| Environment | Instances | Resources | Purpose |
|-------------|-----------|-----------|---------|
| Production | {count} | {resources} | Live traffic |

### 8.3 CI/CD Pipeline
{CI/CD流程说明}

## 9. Security Design

### 9.1 Authentication & Authorization
{认证授权方案}

### 9.2 Data Encryption
{数据加密策略}

### 9.3 Compliance Requirements
{合规要求实现}

## 10. Risk Analysis

### 10.1 Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | High/Medium/Low | High/Medium/Low | {mitigation} |

### 10.2 Operational Risks
{运维风险}

## 11. Architecture Decision Records (ADR)

### ADR-001: {Decision Title}
- **Context**: {背景}
- **Decision**: {决策}
- **Rationale**: {理由}
- **Alternatives Considered**: {备选方案}
- **Consequences**: {后果}

## 12. Validation Summary

- Architecture Review Status: {passed/pending}
- Security Review Status: {passed/pending}
- Performance Benchmark: {results}
- Stakeholder Sign-off: {yes/no}
```

## Handover Context (交接上下文)

> 完成系统设计后，生成以下交接信息给任务拆分阶段

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "task-decomposition"
    handover_id: "HO-{{timestamp}}-SYS"
    timestamp: "{{ISO8601}}"
    prepared_by: "System Designer Agent"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    architecture_type: "microservices/monolith/event-driven"
    total_modules: {{count}}
    estimated_effort: "{{person-days}}"
    
  artifacts:
    delivered:
      - name: "System Design Document"
        path: "docs/system-design/design.md"
        version: "1.0"
        sections:
          - Requirements Analysis
          - Architecture Overview
          - Module Design
          - Technology Stack
          - Data Model
          - Interface Design
          - Deployment Architecture
          - Security Design
          - Risk Analysis
          - ADRs
          
  metrics:
    total_modules: {{count}}
    core_modules: {{count}}
    supporting_modules: {{count}}
    apis_defined: {{count}}
    adrs_documented: {{count}}
    risks_identified: {{count}}
    
  key_decisions:
    - id: "DC-001"
      description: "Architecture style selection - Microservices chosen for scalability"
      rationale: "Business complexity and team size justify microservices"
      alternatives_considered: ["Monolith", "Modular Monolith"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Some module boundaries need refinement during implementation"
        impact: "May require minor refactoring"
        owner: "Task Decomposer"
        
  risks:
    - id: "RISK-001"
      description: "Team lacks experience with selected technology stack"
      probability: "medium"
      impact: "high"
      mitigation: "Schedule training sessions and POC before full implementation"
      
  recommendations:
    - "Start with core modules first to validate architecture"
    - "Implement comprehensive monitoring from day one"
    - "Establish clear coding standards and best practices"
    - "Plan for gradual migration if replacing legacy system"
    
  next_steps:
    - "Begin task decomposition for each module"
    - "Set up development environment and CI/CD pipeline"
    - "Create initial project structure and scaffolding"
    - "Define coding standards and review processes"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/design-system/SCENARIO.md` | 系统设计场景定义 |
| Agent | `../agents/design-system.agent.md` | 系统设计Agent角色 |
| Skill | `../skills/design-system/SKILL.md` | 系统设计技能包 |
| Instruction | `../instructions/design-system.instructions.md` | 系统设计技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [ADR Template](../standards/adr-template.md) - 架构决策记录模板
  - [API Design Guidelines](../standards/api-design-guidelines.md) - API设计规范
- **Templates**: 
  - [System Design Document Template](../templates/system-design-doc.template.md) - 系统设计文档模板
  - [Architecture Diagram Template](../templates/architecture-diagram.template.md) - 架构图模板
- **Evaluations**: 
  - [Architecture Review Checklist](../evaluations/architecture-review-checklist.md) - 架构评审检查清单
  - [Design Quality Assessment](../evaluations/design-quality-assessment.md) - 设计质量评估表

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "decompose-task"
    handover_id: "HO-{ISO8601}-{sequence}"
    timestamp: "{ISO8601}"
    prepared_by: "design-system"
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
