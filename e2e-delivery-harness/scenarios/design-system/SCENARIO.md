---
name: design-system
description: 系统设计场景，负责设计系统架构、技术方案和数据模型
type: scenario
version: "1.2.0"
category: design
stage: system-design
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [design, architecture, technical]
---

# Design System

## Purpose

基于需求规格说明书，设计系统的整体架构、技术方案和数据模型，为开发实现提供技术指导。

## Chain of Thought

> **AI 执行时的强制性思维引导**,确保逐步完成系统设计工作并自我验证

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解系统边界和范围
   ├─ 问：系统的边界和核心模块是什么？
   ├─ 验证：与需求规格说明书对照
   └─ 检查：识别所有外部依赖和集成点
   ↓
[ANALYZE] Step 2: 分析非功能性需求和技术约束
   ├─ 问：性能、安全、可用性的量化指标是什么？
   ├─ 验证：指标可测量且合理
   └─ 检查：技术约束已明确
   ↓
[DESIGN] Step 3: 设计系统架构和模块划分
   ├─ 问：架构风格是否适合业务需求？
   ├─ 验证：满足非功能性需求
   └─ 检查：模块高内聚低耦合
   ↓
[MODEL] Step 4: 设计数据模型和接口方案
   ├─ 问：核心实体关系是否清晰？
   ├─ 验证：满足业务场景
   └─ 检查：符合范式和扩展性要求
   ↓
[VERIFY] Step 5: 验证设计方案完整性和一致性
   ├─ 问：所有需求都有对应的设计？
   ├─ 验证：执行 Design Validation Checklist
   └─ 检查：技术方案可行且风险可控
   ↓
[HANDOVER] Step 6: 准备交接给任务拆分阶段
   ├─ 生成：Handover Context
   ├─ 更新：Global Context
   └─ 通知：Task Decomposer Agent
```

### Step-by-Step Reasoning (详细推理)

**Step 1: 系统边界理解**
- **目标**: 明确系统的范围、核心模块和外部依赖
- **思考**: 
  - 问：系统需要解决的核心问题是什么？
  - 问：系统与外部系统的边界在哪里？
- **验证**: 对照需求规格说明书的功能清单
- **检查点**: 
  - [ ] 核心模块已识别
  - [ ] 外部依赖已列出
  - [ ] 系统边界已明确
- **产出**: 系统边界图

**Step 2: 非功能性需求分析**
- **目标**: 量化性能、安全、可用性等非功能性指标
- **思考**: 
  - 问：预期的用户量和并发量是多少？
  - 问：安全和合规要求有哪些？
- **验证**: 指标可测量且有明确目标值
- **检查点**: 
  - [ ] 性能指标已量化
  - [ ] 安全要求已明确
  - [ ] 可用性目标已设定
- **产出**: 非功能性需求清单

**Step 3: 架构设计**
- **目标**: 选择合适的架构风格并进行模块划分
- **思考**: 
  - 问：单体、微服务还是其他架构？
  - 问：模块间如何解耦？
- **验证**: 架构满足非功能性需求
- **检查点**: 
  - [ ] 架构风格已选择
  - [ ] 模块划分合理
  - [ ] 技术栈已确定
- **产出**: 系统架构图

**Step 4: 数据建模**
- **目标**: 设计核心数据实体和关系
- **思考**: 
  - 问：核心业务实体有哪些？
  - 问：实体间的关系是什么？
- **验证**: 数据模型满足业务场景
- **检查点**: 
  - [ ] 核心实体已识别
  - [ ] 关系已定义
  - [ ] 符合范式要求
- **产出**: ER图和数据字典

**Step 5: 接口定义**
- **目标**: 定义模块间和对外的接口
- **思考**: 
  - 问：接口契约是否清晰？
  - 问：是否考虑版本兼容性？
- **验证**: 接口稳定且可扩展
- **检查点**: 
  - [ ] API 接口已定义
  - [ ] 接口文档完整
  - [ ] 考虑了扩展性
- **产出**: API 接口规格

## Decision Checkpoints

> **执行过程中必须确认的关键决策点**,每个决策点都需要明确记录

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 架构风格选择 | 完成非功能性分析后 | 单体/微服务/事件驱动/其他 | 团队能力、业务复杂度、扩展性需求 | 架构设计文档 |
| DC-002 | 技术栈选型 | 架构确定后 | 具体技术框架和工具 | 成熟度、社区支持、团队熟悉度 | 技术方案文档 |
| DC-003 | 模块划分策略 | 设计核心模块时 | 按功能/按领域/按层次 | 内聚性、耦合度、可维护性 | 模块设计文档 |
| DC-004 | 数据存储方案 | 数据建模完成后 | SQL/NoSQL/混合 | 数据结构、查询模式、扩展性 | 数据设计文档 |

**决策记录要求**:
- 每个决策必须记录：决策时间、决策人(或AI)、选择理由、备选方案评估
- 重大决策需要技术委员会确认
- 决策变更必须记录变更原因和影响分析

## Error Handling

> **遇到异常情况时的标准化处理流程**,AI 必须严格按照此流程执行

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误,无法继续执行 | 立即停止,升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误,影响核心功能 | 尝试修复,失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误,可降级处理 | 记录并继续,后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息,不影响执行 | 记录并继续 |

### 错误类型 1：架构决策困难

| 属性 | 值 |
|------|-----|
| **错误级别** | P1 |
| **识别信号** | 多种架构方案各有优劣，难以抉择 |
| **根本原因** | 需求不明确、技术评估不足、团队意见分歧 |
| **自动处理** | 1. 列出各方案优缺点对比表<br>2. 根据非功能性需求权重评分<br>3. 选择综合得分最高的方案<br>4. 记录决策依据和备选方案 |
| **降级方案** | 采用保守方案(团队最熟悉的)，预留重构空间 |
| **升级条件** | 团队无法达成共识或风险等级为 High |
| **升级对象** | 技术委员会或架构师 |
| **恢复验证** | 方案获得技术委员会批准 |

### 错误类型 2：技术风险识别

| 属性 | 值 |
|------|-----|
| **错误级别** | P1 |
| **识别信号** | 关键技术存在不确定性或团队缺乏经验 |
| **根本原因** | 新技术未验证、复杂度超出预期、依赖外部因素 |
| **自动处理** | 1. 识别所有技术风险点<br>2. 评估风险概率和影响<br>3. 制定应对策略(规避/转移/缓解/接受)<br>4. 在设计方案中标注风险 |
| **降级方案** | 采用成熟技术替代，或增加技术验证阶段 |
| **升级条件** | 风险等级为 High/Critical 且无有效缓解措施 |
| **升级对象** | 技术负责人和项目管理者 |
| **恢复验证** | 风险应对计划获得批准并分配资源 |

### 错误类型 3：需求与设计冲突

| 属性 | 值 |
|------|-----|
| **错误级别** | P2 |
| **识别信号** | 设计方案无法满足某些需求或需求之间存在矛盾 |
| **根本原因** | 需求分析不完整、技术约束未考虑、需求变更 |
| **自动处理** | 1. 分析冲突的根本原因<br>2. 与 Requirement Analyst 确认<br>3. 提出设计调整建议或需求修改建议<br>4. 记录冲突和解决方案 |
| **降级方案** | 暂时标注为已知问题，在 Handover 中说明 |
| **升级条件** | 影响核心功能实现或需要重大设计变更 |
| **升级对象** | 产品经理和系统设计师 |
| **恢复验证** | 冲突解决并获得相关方确认 |

### 错误日志要求

```yaml
error_log:
  - error_id: "ERR-{timestamp}-{sequence}"
    timestamp: "{{ISO8601}}"
    level: "P0/P1/P2/P3"
    type: "{错误类型}"
    description: "{详细描述}"
    context: "{发生时的上下文}"
    action_taken: "{采取的行动}"
    result: "{处理结果}"
    escalated: true/false
    resolved: true/false
```


## Quality Metrics & Validation

> **量化的质量评估标准和自动化验证机制**

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | DESIGN-COMPLETENESS | ≥95% | (已完成章节数/必需章节总数) × 100% | 对照设计文档检查清单 | 30% |
| KPI-002 | REQ-TRACE | 100% | (已追溯需求数/总需求数) × 100% | 需求-设计映射表 | 25% |
| KPI-003 | REVIEW-PASS | ≥90% | (通过评审项数/总评审项数) × 100% | 技术评审记录 | 25% |
| KPI-004 | ARCHITECTURE-QUALITY | ≥85分 | 架构评分(见评分标准) | 架构评估工具 | 20% |

**综合评分计算**:
```
Score = Σ(KPI_i × Weight_i) / ΣWeight_i
合格线: ≥80分
优秀线: ≥90分
卓越线: ≥95分
```

### Output Validation Checklist (强制验证)

**V-001: 完整性验证**
- [ ] 系统架构图已绘制
- [ ] 技术方案文档已编写
- [ ] 数据模型(ER图)已设计
- [ ] API 接口规格已定义
- [ ] 所有必需章节已填充(无空白)
- [ ] 引用的资产都存在且可访问

**V-002: 一致性验证**
- [ ] 术语使用一致(对照术语表)
- [ ] 架构设计与非功能性需求一致
- [ ] 数据模型与业务需求一致
- [ ] 接口定义与模块划分一致
- [ ] 与上游需求分析的输出一致

**V-003: 准确性验证**
- [ ] 技术选型合理且有依据
- [ ] 性能估算基于实际测试或经验数据
- [ ] 安全设计符合行业标准
- [ ] 所有假设都已明确标注

**V-004: 可执行性验证**
- [ ] 技术方案在团队能力范围内
- [ ] 资源需求(服务器、存储等)合理
- [ ] 时间估算可行
- [ ] 技术风险可控且有应对计划

**V-005: 规范性验证**
- [ ] 符合命名规范
- [ ] 图表清晰可读
- [ ] 文档格式规范
- [ ] 元数据完整准确

### Validation Failure Handling

```
IF 任何验证项未通过
THEN
  1. 记录未通过的验证项及原因
  2. 评估影响程度(P0/P1/P2/P3)
  3. P0/P1: 必须修复后才能继续
  4. P2/P3: 可记录为已知问题,但需在Handover中说明
  5. 重新执行验证直到全部通过或确认可接受
END
```

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Started At**: `{{execution.started_at}}` — ISO8601格式开始时间
- **Completed At**: `{{execution.completed_at}}` — ISO8601格式完成时间
- **Agent**: `{{agent.name}}` — 执行Agent标识
- **Version**: `{{asset.version}}` — 使用的资产版本

## Handover Criteria & Context

> **阶段完成的严格验收标准和标准化交接流程**

### Mandatory Acceptance Criteria (必须全部满足)

```
✅ AC-001: 系统架构图已完成并通过评审 - [已验证/未验证]
✅ AC-002: 技术方案文档已编写完整 - [已验证/未验证]
✅ AC-003: 数据模型(ER图和数据字典)已设计 - [已验证/未验证]
✅ AC-004: API 接口规格已明确定义 - [已验证/未验证]
✅ AC-005: 所有 Quality Validation 检查项通过 - [是/否]
✅ AC-006: 所有 Decision Checkpoints 已记录 - [是/否]
✅ AC-007: 所有 Errors 已处理或记录 - [是/否]
✅ AC-008: 技术方案评审通过率 ≥90% - [是/否]
```

### Deliverables Checklist

| ID | 交付物名称 | 格式 | 必填 | 验证标准 | 状态 |
|----|------------|------|------|----------|------|
| DEL-001 | 系统架构文档 | .md + 图表 | 是 | 包含架构图、模块划分、技术栈 | ☐ |
| DEL-002 | 技术方案详细设计 | .md | 是 | 核心模块设计、关键算法 | ☐ |
| DEL-003 | 数据模型(ER图) | .png/.svg + .md | 是 | ER图、数据字典、索引设计 | ☐ |
| DEL-004 | API 接口规格 | OpenAPI/Swagger | 是 | 完整的接口定义、示例 | ☐ |
| DEL-005 | 技术风险评估报告 | .md | 是 | 风险清单、应对策略 | ☐ |
| DEL-006 | 设计决策记录 | .md | 否 | 关键决策及理由 | ☐ |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "system-design"
    to_stage: "task-decomposition"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_duration: "{{duration}}"
    
  artifacts:
    delivered:
      - name: "系统架构文档"
        path: "docs/architecture-design.md"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "数据模型"
        path: "docs/data-model.md"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "API 接口规格"
        path: "docs/api-spec.yaml"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-001"
      description: "架构风格选择"
      rationale: "选择微服务架构以支持高并发和独立扩展"
      alternatives_considered: ["单体架构", "事件驱动架构"]
    - id: "DC-002"
      description: "技术栈选型"
      rationale: "选择成熟稳定的技术栈以降低风险"
      alternatives_considered: ["其他技术组合"]
      
  open_issues:
    blocking:
      - id: "ISSUE-XXX"
        description: "{阻塞性问题描述}"
        impact: "{影响分析}"
        required_action: "{需要的行动}"
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{非阻塞性问题描述}"
        planned_resolution: "{计划解决方案}"
        
  risks:
    - id: "RISK-001"
      description: "新技术学习曲线陡峭"
      probability: "medium"
      impact: "medium"
      mitigation: "安排技术培训和技术预研阶段"
    - id: "RISK-002"
      description: "第三方依赖稳定性"
      probability: "low"
      impact: "high"
      mitigation: "准备备选方案，增加监控"
      
  recommendations:
    - "建议在任务拆分时优先考虑核心模块"
    - "建议先进行技术预研验证关键技术点"
    - "建议建立持续集成环境以支持快速迭代"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{实际值}}
        target: 95
        status: "pass/fail"
      - kpi_id: "KPI-002"
        value: {{实际值}}
        target: 100
        status: "pass/fail"
```

### Next Stage Notification

完成 Handover Context 后,必须:
1. 更新 Global Context 中的阶段状态为 "design-completed"
2. 通知 Task Decomposer Agent 开始任务拆分
3. 归档当前阶段的所有设计文档
4. 记录阶段完成时间戳

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/design-system.agent.md` | 系统设计角色 |
| **Prompt** | `../../prompts/design-system.prompt.md` | 系统设计提示词 |
| **Instruction** | `../../instructions/design-system.instructions.md` | 系统设计技术指令 |
| **Skill** | `../../skills/design-system/SKILL.md` | 系统设计技能 |

## Prerequisites

### 必需前置条件

1. 需求规格说明书已评审通过
2. 具备技术团队
3. 可获取技术约束信息

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `requirements_spec` | 是 | 需求规格说明书 |
| `tech_constraints` | 否 | 技术约束条件 |
| `team_capability` | 否 | 团队技术能力 |
