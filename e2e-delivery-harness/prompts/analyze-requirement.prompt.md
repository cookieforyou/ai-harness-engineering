---
name: analyze-requirement
description: "业务需求分析提示词，用于将原始需求转换为结构化的需求规格说明书"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [prompt, requirements, analysis]
---
# Analyze Requirement Prompt

## Purpose

本提示词指导AI执行需求分析任务，将原始业务需求转换为结构化、可验证的需求规格说明书。

### Key Objectives

- **全面识别干系人**: 确保所有关键干系人的诉求都被捕获
- **明确业务目标**: 将模糊的业务期望转化为具体的、可衡量的目标
- **规范化需求描述**: 使用标准格式（用户故事）描述功能需求
- **定义验收标准**: 为每条需求制定可测试的验收标准
- **建立追溯关系**: 确保需求与业务目标的清晰追溯

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `project_name` | string | true | - | 项目名称 | 非空字符串 |
| `raw_requirements` | string | true | - | 原始需求描述（来自业务方） | 非空，包含业务场景描述 |
| `stakeholders` | array | false | [] | 已知干系人列表 | 对象数组，含name/role/contact |
| `business_background` | string | false | - | 业务背景信息 | 描述业务现状和问题 |
| `constraints` | array | false | [] | 已知约束条件 | 技术/时间/资源/法规约束 |
| `existing_docs` | array | false | [] | 现有相关文档 | 文档路径或URL列表 |
| `industry_context` | string | false | - | 行业背景 | 所在行业特点和监管要求 |

### 示例: 变量的正确格式

```yaml
# 示例: 完整的需求分析输入
project_name: "电商订单系统"
raw_requirements: |
  用户希望能够在线下单购买商品，支持多种支付方式，
  并且可以查看订单状态和物流信息。
  
stakeholders:
  - name: "张三"
    role: "产品经理"
    contact: "zhangsan@example.com"
  - name: "李四"
    role: "运营总监"
    contact: "lisi@example.com"
    
business_background: |
  公司计划拓展线上销售渠道，目前主要依靠线下门店。
  需要建立电商平台以触达更广泛的客户群体。
  
constraints:
  - "必须在3个月内上线MVP版本"
  - "预算不超过50万元"
  - "需要与现有ERP系统集成"
  
existing_docs:
  - "docs/current-system-overview.md"
  - "docs/market-research.pdf"
  
industry_context: "零售电商行业，需符合电子商务法和消费者权益保护法"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解业务背景和目标
   ├─ 输入: project_name, raw_requirements, business_background
   ├─ 思考: 业务痛点是什么？期望达成的目标是什么？目标是否SMART？
   ├─ 验证: 业务目标清晰、可衡量、与项目价值一致
   └─ 输出: 业务目标清单（3-5条核心目标）
   ↓
[ANALYZE] Step 2: 识别干系人和诉求
   ├─ 输入: stakeholders, industry_context
   ├─ 思考: 谁是决策者、使用者、影响者？他们的核心诉求是什么？是否有冲突？
   ├─ 验证: 覆盖所有关键干系人类型，诉求记录完整
   └─ 输出: 干系人分析报告（含影响力矩阵和诉求清单）
   ↓
[GATHER] Step 3: 收集和整理需求
   ├─ 输入: raw_requirements, existing_docs
   ├─ 思考: 功能需求有哪些？非功能需求（性能/安全/可用性）是否明确？
   ├─ 验证: 使用"As a... I want... so that..."格式规范化每条需求
   └─ 输出: 初步需求清单（功能+非功能）
   ↓
[MODEL] Step 4: 构建业务模型
   ├─ 输入: 需求清单, business_background
   ├─ 思考: 主要业务流程是什么？关键决策点和异常处理如何设计？
   ├─ 验证: 流程图完整，用例覆盖主要场景和边界情况
   └─ 输出: 业务流程图和用例模型
   ↓
[SPECIFY] Step 5: 编写需求规格
   ├─ 输入: 需求清单, 业务模型, constraints
   ├─ 思考: 每条需求的验收标准是否可测试？优先级是否合理？依赖关系是否明确？
   ├─ 验证: 需求符合SMART原则，验收标准可量化，追溯关系清晰
   └─ 输出: 需求规格说明书（草稿）
   ↓
[VALIDATE] Step 6: 评审确认并准备交接
   ├─ 组织评审会议，收集干系人反馈
   ├─ 根据反馈修订需求文档
   ├─ 获得干系人签字确认
   └─ 生成交接上下文，准备移交系统设计阶段
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: 需求模糊不清

**识别信号**: 
- 原始需求描述不完整或含糊
- 使用“大概”、“可能”、“最好能”等模糊词汇
- 缺乏具体的业务场景或用户故事支撑

**处理流程**:
```
IF 原始需求描述不完整或含糊
THEN
  1. 列出所有可能的理解方式（至少2种）
  2. 为每种理解方式生成假设和业务场景
  3. 主动向业务方提出澄清问题（最多3轮）
  4. IF 仍无法澄清 THEN 在输出中标注 [需要确认] 并说明各种可能性
  5. 记录决策依据和假设前提
END
```

**降级方案**: 基于最常见业务场景做出合理假设，但必须在文档中明确标注为“假设”，并在评审时重点确认

**升级条件**: 经过3轮澄清后业务方仍无法明确需求，升级到产品负责人或项目发起人决策

---

### Error Scenario 2: 干系人信息不足

**识别信号**: 
- 无法识别完整的干系人列表
- 关键角色类型（决策者、使用者、影响者）有遗漏
- 干系人联系方式缺失

**处理流程**:
```
IF 无法识别完整的干系人
THEN
  1. 列出已识别的干系人及其角色
  2. 识别可能遗漏的角色类型（决策者、使用者、受影响者、监管者）
  3. 分析每类角色的典型代表（如：财务总监、一线操作员等）
  4. 在输出中建议需要联系的干系人清单
  5. 提供干系人识别的最佳实践指南
END
```

**降级方案**: 先基于已知干系人进行分析，同时标记“待补充干系人”，建议在后续迭代中完善

**升级条件**: 缺少决策者或核心使用者的输入，导致无法确定业务目标或关键需求

---

### Error Scenario 3: 需求之间冲突

**识别信号**: 
- 不同干系人对同一功能有相反要求
- 资源分配存在竞争关系
- 优先级排序出现明显分歧
- 技术约束与业务期望矛盾

**处理流程**:
```
IF 发现需求之间存在矛盾
THEN
  1. 列出冲突的需求对和涉及的干系人
  2. 分析冲突的根本原因（利益不一致、理解偏差、资源限制等）
  3. 提出解决建议（至少2个备选方案）
     - 方案A: 折中方案
     - 方案B: 分阶段实现
  4. 组织冲突解决会议，引导达成共识
  5. IF 无法达成共识 THEN 标记为 [冲突待解决] 并升级到更高层级决策者
  6. 记录最终决策和理由
END
```

**降级方案**: 暂时搁置冲突需求，先推进无争议部分，同时安排专项会议解决冲突

**升级条件**: 经过2轮协商仍无法达成共识，或冲突涉及核心业务目标

---

### Error Scenario 4: 约束不明确或缺失

**识别信号**: 
- 约束条件缺失或模糊
- 未明确时间、预算、技术等关键约束
- 假设前提未经确认

**处理流程**:
```
IF 约束条件缺失或模糊
THEN
  1. 列出合理的默认假设（基于行业标准和类似项目经验）
  2. 在输出中标注 [基于假设] 并说明假设内容
  3. 评估假设不成立的风险和影响
  4. 建议在评审时重点确认这些假设
  5. 提供常见约束类型的检查清单供参考
END
```

**降级方案**: 使用行业标准值作为临时约束，但必须明确标注并在评审时确认

**升级条件**: 关键约束（如交付时间、预算上限）完全未知，导致无法进行合理规划

## Output Format (输出格式)

> AI必须按照以下结构生成需求规格说明书

```markdown
# Requirements Specification

## 1. Document Information
- Project Name: {project_name}
- Version: 1.0
- Date: {current_date}
- Status: Draft/Confirmed
- Author: {agent_name}

## 2. Business Background & Goals

### 2.1 Business Context
{描述业务背景、现状和问题}

### 2.2 Business Objectives
| Objective | Description | Priority | KPI/Metric |
|-----------|-------------|----------|------------|
| OBJ-001 | {目标描述} | P0/P1/P2 | {可衡量指标} |

## 3. Stakeholder Analysis

### 3.1 Stakeholder Matrix
| Stakeholder | Role | Type | Key Concerns | Influence | Priority |
|-------------|------|------|--------------|-----------|----------|
| {name} | {role} | Decision Maker/User/Influencer | {concerns} | High/Medium/Low | P0/P1/P2 |

### 3.2 Communication Plan
{与各干系人的沟通频率和方式}

## 4. Functional Requirements

### 4.1 Requirements Overview
| ID | Requirement Name | Priority | Status | Dependencies |
|----|------------------|----------|--------|--------------|
| FR-001 | {名称} | P0/P1/P2 | New/Modified | {依赖ID} |

### 4.2 Detailed Requirements

#### FR-001: {Requirement Name}
- **User Story**: As a {role}, I want {feature}, so that {value}
- **Acceptance Criteria**:
  1. Given {condition}, When {action}, Then {expected_result}
  2. ...
- **Priority**: P0/P1/P2
- **Dependencies**: {FR-XXX or None}
- **Notes**: {additional information}

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Response Time | < X ms | Under normal load |
| Throughput | X requests/sec | Peak load |
| Concurrent Users | X users | Simultaneous |

### 5.2 Security Requirements
| Requirement | Specification | Compliance Standard |
|-------------|---------------|---------------------|
| Authentication | {method} | {standard} |
| Authorization | {RBAC/ABAC} | {policy} |
| Data Protection | {encryption} | {regulation} |

### 5.3 Availability Requirements
| Metric | Target | Recovery Strategy |
|--------|--------|--------------------|
| Uptime | 99.9% | {strategy} |
| RTO | < X hours | {plan} |
| RPO | < X minutes | {backup} |

## 6. Business Process Models

### 6.1 Process: {Process Name}
**Description**: {流程描述}
**Participants**: {参与者列表}
**Input**: {输入数据/事件}
**Output**: {输出结果}

**Flow Steps**:
1. {Step 1}
2. {Step 2}
3. {Decision Point} → Branch A / Branch B

**Exception Handling**:
- Exception 1: {handling strategy}
- Exception 2: {handling strategy}

## 7. Use Case Model

### UC-001: {Use Case Name}
- **Actors**: {actor list}
- **Preconditions**: {preconditions}
- **Main Flow**:
  1. {step 1}
  2. {step 2}
- **Alternative Flows**:
  - Alt 1: {description}
- **Postconditions**: {postconditions}

## 8. Constraints & Assumptions

### 8.1 Constraints
- Technical: {constraints}
- Time: {deadlines}
- Budget: {budget limits}
- Regulatory: {compliance requirements}

### 8.2 Assumptions
- [Assumption] {description} - Risk if invalid: {impact}

### 8.3 Open Issues
- ISSUE-001: {issue description} - Status: Pending confirmation from {stakeholder}

## 9. Traceability Matrix

| Business Objective | Related Requirements | Acceptance Criteria |
|--------------------|----------------------|---------------------|
| OBJ-001 | FR-001, FR-002 | AC-001, AC-002 |

## 10. Validation Summary

- Total Requirements: {count}
- With Acceptance Criteria: {count} ({percentage}%)
- Stakeholders Reviewed: {list}
- Conflicts Resolved: {count}/{total}
- Next Review Date: {date}
```

## Output Validation (输出验证)

> **重要**: 在生成最终输出前，必须完成以下验证步骤

### Validation Checklist

**V-001: Completeness Check (完整性检查)**
- [ ] All required sections are present (Business Goals, Stakeholders, Functional/NFR, Processes, Use Cases)
- [ ] Each functional requirement has acceptance criteria
- [ ] Non-functional requirements cover performance, security, availability
- [ ] Business process diagrams include main paths and exception handling

**V-002: Consistency Check (一致性检查)**
- [ ] Terminology is consistent throughout the document
- [ ] No logical conflicts between requirements
- [ ] Requirements align with business objectives
- [ ] Traceability matrix is complete

**V-003: Testability Check (可测试性检查)**
- [ ] Each requirement can be converted to test cases
- [ ] Acceptance criteria use quantifiable metrics
- [ ] Boundary conditions and edge cases are considered
- [ ] Expected results are clearly defined

**V-004: Clarity Check (清晰度检查)**
- [ ] User stories follow "As a... I want... so that..." format
- [ ] No ambiguous terms (avoid "fast", "user-friendly", etc.)
- [ ] Business processes are easy to understand
- [ ] All assumptions are explicitly stated

**V-005: Compliance Check (规范性检查)**
- [ ] Requirements follow SMART criteria
- [ ] Industry standards and regulations are addressed
- [ ] Documentation follows organizational templates
- [ ] Version control and change tracking are maintained

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

## Handover Context (交接上下文)

> 完成需求分析后，生成以下交接信息给系统设计阶段

```yaml
handover:
  header:
    from_stage: "requirement-analysis"
    to_stage: "system-design"
    handover_id: "HO-{{timestamp}}-REQ"
    timestamp: "{{ISO8601}}"
    prepared_by: "Requirement Analyst Agent"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "Requirements Specification"
        path: "docs/requirements-spec.md"
        version: "1.0"
        sections:
          - Business Background & Goals
          - Stakeholder Analysis
          - Functional Requirements
          - Non-Functional Requirements
          - Business Process Models
          - Use Case Model
          - Traceability Matrix
          
  metrics:
    total_requirements: {{count}}
    functional_requirements: {{count}}
    non_functional_requirements: {{count}}
    with_acceptance_criteria: {{count}} ({{percentage}}%)
    total_stakeholders: {{count}}
    conflicts_resolved: {{count}}/{{total}}
    
  decisions:
    - id: "DC-001"
      description: "Stakeholder coverage confirmed"
      rationale: "All key stakeholder types identified and consulted"
      alternatives_considered: ["Expand stakeholder list", "Proceed with current coverage"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-001"
        description: "Some assumptions need validation during design phase"
        impact: "May affect technical architecture decisions"
        owner: "System Designer"
        
  risks:
    - id: "RISK-001"
      description: "Assumptions about integration with legacy system may be incorrect"
      probability: "medium"
      impact: "high"
      mitigation: "Validate integration requirements during system design"
      
  recommendations:
    - "Prioritize P0 requirements in initial design iterations"
    - "Consider scalability implications of performance requirements"
    - "Review security requirements with security team before implementation"
    
  next_steps:
    - "Review requirements specification with stakeholders for sign-off"
    - "Begin system architecture design based on approved requirements"
    - "Identify technical spikes for complex requirements"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/analyze-requirement/SCENARIO.md` | 需求分析场景定义 |
| Agent | `../agents/analyze-requirement.agent.md` | 需求分析Agent角色 |
| Skill | `../skills/analyze-requirement/SKILL.md` | 需求分析技能包 |
| Instruction | `../instructions/analyze-requirement.instructions.md` | 需求分析技术指令 |

## Related Resources (相关资源)

- **Standards**: 
  - [SMART Criteria](../standards/smart-criteria.md) - 需求编写标准
  - [User Story Format](../standards/user-story-format.md) - 用户故事格式规范
- **Templates**: 
  - [Requirements Specification Template](../templates/requirements-spec.template.md) - 需求规格说明书模板
  - [Stakeholder Analysis Template](../templates/stakeholder-analysis.template.md) - 干系人分析模板
- **Evaluations**: 
  - [Requirement Quality Checklist](../evaluations/requirement-quality-checklist.md) - 需求质量检查清单
