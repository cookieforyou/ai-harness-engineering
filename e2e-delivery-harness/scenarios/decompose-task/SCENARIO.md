---
name: decompose-task
description: 任务拆分场景，负责将需求分解为可执行的技术任务
version: "1.2.0"
type: scenario
category: planning
stage: task-decomposition
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: [planning, decomposition, tasks]
---
# Task Decomposition

## Purpose

将需求规格说明书和技术设计方案分解为可执行、可跟踪、可度量的技术任务，为开发团队提供清晰的工作项清单，确保开发过程的可控性和可预测性。

### Business Value

- **降低认知负荷**: 将复杂需求拆解为小颗粒度任务
- **提升可预测性**: 通过任务估算和依赖分析提高计划准确性
- **增强可追溯性**: 建立需求-任务-代码的完整追溯链
- **优化资源配置**: 基于任务优先级和技能匹配合理分配人力

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成任务拆分工作

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: 理解需求范围和边界
   ├─ 问：需求的业务范围和技术边界是什么？
   ├─ 验证：与需求规格说明书对照
   └─ 检查：识别所有功能模块和非功能要求
   ↓
[ANALYZE] Step 2: 识别技术任务和依赖
   ├─ 问：实现每个功能需要哪些技术工作？
   ├─ 验证：覆盖前端、后端、数据库、测试等维度
   └─ 检查：识别任务间的依赖关系和并行可能性
   ↓
[DESIGN] Step 3: 设计任务结构和粒度
   ├─ 问：任务粒度是否合适（1-3天工作量）？
   ├─ 验证：符合INVEST原则（独立、可协商、有价值、可估算、小、可测试）
   └─ 检查：任务之间有清晰的接口和交付物定义
   ↓
[ESTIMATE] Step 4: 估算工作量和优先级
   ├─ 问：每个任务的复杂度、风险和工作量是多少？
   ├─ 验证：参考历史数据和团队能力
   └─ 检查：考虑缓冲时间和不确定性因素
   ↓
[VERIFY] Step 5: 验证任务分解完整性
   ├─ 问：是否覆盖所有需求？是否有遗漏或重复？
   ├─ 验证：需求-任务映射表100%覆盖
   └─ 检查：关键路径和里程碑已识别
   ↓
[HANDOVER] Step 6: 准备交接给开发阶段
   ├─ 生成：任务清单（Task List）
   ├─ 更新：Global Context（任务状态追踪）
   └─ 通知：Feature Implementer Agent
```

### Step-by-Step Reasoning

**Step 1: 需求分析**
- **问**: 需求的范围和边界是什么？核心功能和非功能要求有哪些？
- **验证**: 与需求规格说明书逐条对照，确保理解一致
- **检查**: 识别所有功能模块、API接口、数据模型、用户交互点
- **输出**: 需求范围清单和功能分解树

**Step 2: 任务识别**
- **问**: 实现每个功能需要哪些技术工作？涉及哪些技术栈和组件？
- **验证**: 覆盖前端、后端、数据库、测试、部署等全维度
- **检查**: 无遗漏项，每个功能都有对应的技术任务
- **输出**: 初步任务列表（未估算）

**Step 3: 工作量估算**
- **问**: 每个任务的复杂度、风险和工作量是多少？
- **验证**: 参考历史数据和团队能力，使用故事点或人天估算
- **检查**: 考虑学习曲线、技术风险、依赖等待时间
- **输出**: 带估算的任务列表

**Step 4: 依赖分析**
- **问**: 任务间的依赖关系是什么？哪些可以并行执行？
- **验证**: 绘制依赖图，识别关键路径和阻塞点
- **检查**: 最小化串行依赖，最大化并行可能性
- **输出**: 任务依赖图和关键路径分析

**Step 5: 任务分配**
- **问**: 任务如何分配给团队成员？技能匹配度如何？
- **验证**: 评估成员技能与任务需求的匹配度
- **检查**: 负载均衡，避免单点过载，考虑成长机会
- **输出**: 任务分配方案

## Decision Checkpoints

> AI 在以下决策点必须暂停并记录决策依据

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | 任务粒度确定 | 任务拆分时 | 粗粒度(>5天) / 中粒度(2-5天) / 细粒度(<2天) | 符合INVEST原则，1-3天为佳 | 任务清单 |
| DC-002 | 优先级排序 | 任务列表完成后 | P0(紧急重要) / P1(重要不紧急) / P2(紧急不重要) / P3(其他) | 业务价值、依赖关系、风险程度 | 任务清单 |
| DC-003 | 估算方法选择 | 开始估算前 | 故事点 / 人天 / T-shirt尺寸 | 团队习惯、项目阶段、精度要求 | 估算说明文档 |
| DC-004 | 依赖处理方式 | 发现复杂依赖时 | 串行执行 / 并行执行+协调 / 重构解耦 | 时间约束、团队能力、长期收益 | 依赖分析文档 |
| DC-005 | 风险缓冲设置 | 高风险任务识别后 | 无缓冲 / 10%缓冲 / 20%缓冲 / 单独风险任务 | 风险概率和影响程度 | 风险管理计划 |

## Error Handling

### 任务粒度不当

| 属性 | 值 |
|------|-----|
| **识别信号** | 任务过大或过小 |
| **处理方式** | 1. 评估当前粒度；2. 拆分或合并任务；3. 确保可跟踪；4. 验证粒度合适 |
| **升级条件** | 影响开发效率 |

### 依赖不清晰

| 属性 | 值 |
|------|-----|
| **识别信号** | 任务间依赖关系不明确 |
| **处理方式** | 1. 梳理任务间关系；2. 绘制依赖图；3. 识别阻塞点；4. 调整任务顺序 |
| **升级条件** | 影响开发计划 |

### 估算分歧

| 属性 | 值 |
|------|-----|
| **识别信号** | 团队对估算有分歧 |
| **处理方式** | 1. 讨论估算依据；2. 参考历史数据；3. 使用 Planning Poker；4. 达成共识 |
| **升级条件** | 无法达成共识 |




## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | TASK-COVERAGE | 100% | (已分解需求数/总需求数) × 100% | 需求-任务映射表检查 | 25% |
| KPI-002 | GRANULARITY-SUITABILITY | ≥90% | (符合INVEST原则的任务数/总任务数) × 100% | 任务清单抽样审查 | 20% |
| KPI-003 | DEPENDENCY-COMPLETENESS | 100% | (已识别依赖数/实际依赖数) × 100% | 依赖图完整性检查 | 20% |
| KPI-004 | ESTIMATION-ACCURACY | ±20% | 1 - \|(实际工时-估算工时)/估算工时\| | 历史数据对比分析 | 20% |
| KPI-005 | CLARITY-SCORE | ≥85/100 | 任务描述清晰度评分（DoR检查） | 团队反馈和审查 | 15% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.25) + (KPI-002 × 0.20) + (KPI-003 × 0.20) + (KPI-004 × 0.20) + (KPI-005 × 0.15)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有需求都已分解为任务
- [ ] 每个任务都有明确的验收标准
- [ ] 依赖关系已全部识别并记录
- [ ] 风险评估已完成

**一致性验证 (Consistency)**:
- [ ] 任务命名遵循统一规范
- [ ] 估算单位一致（故事点或人天）
- [ ] 优先级排序逻辑一致
- [ ] 与技术方案保持一致

**准确性验证 (Accuracy)**:
- [ ] 工作量估算有依据支撑
- [ ] 依赖关系准确反映技术实现顺序
- [ ] 技能匹配度评估合理
- [ ] 关键路径识别正确

**可执行性验证 (Executability)**:
- [ ] 任务描述清晰，无歧义
- [ ] 验收标准可量化、可测试
- [ ] 所需资源和环境明确
- [ ] 任务粒度适合分配和执行

**规范性验证 (Compliance)**:
- [ ] 符合INVEST原则
- [ ] 遵循团队任务管理规范
- [ ] 满足DoR（Definition of Ready）要求
- [ ] 文档格式符合标准



## Handover Criteria (交接标准)

### 准入条件（必须满足）

```yaml
entry_criteria:
  - requirement_spec_approved: true  # 需求规格说明书已批准
  - tech_design_completed: true      # 技术设计已完成
  - team_assigned: true              # 开发团队已确定
  - estimation_baseline_available: true  # 有历史估算数据参考
```

### 准出条件（全部达成）

```yaml
exit_criteria:
  task_coverage: 100%                # 需求覆盖率100%
  granularity_check: "≥90%符合INVEST" # 任务粒度检查通过
  dependency_mapped: true            # 依赖关系已映射
  priority_assigned: true            # 优先级已分配
  estimates_completed: true          # 工作量估算完成
  dor_met: "≥95%任务满足DoR"         # Definition of Ready检查
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "task-decomposition"
    to_stage: "feature-implementation"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_tasks: {{任务总数}}
    estimated_total_effort: "{{总估算工作量}}"
    critical_path_length: "{{关键路径天数}}"
    
  artifacts:
    delivered:
      - name: "任务清单"
        path: "docs/task-list.md"
        version: "1.0.0"
        checksum: "{{SHA256}}"
      - name: "任务依赖图"
        path: "docs/dependency-graph.png"
        version: "1.0.0"
        format: "PNG/Mermaid"
      - name: "估算说明文档"
        path: "docs/estimation-notes.md"
        version: "1.0.0"
      - name: "风险管理计划"
        path: "docs/risk-management.md"
        version: "1.0.0"
      
  decisions:
    - id: "DC-001"
      description: "任务粒度选择"
      decision: "采用细粒度拆分（1-3天/任务）"
      rationale: "提高可预测性，便于并行执行和进度跟踪"
      alternatives_considered: ["粗粒度(>5天)", "中粒度(2-5天)"]
      
    - id: "DC-002"
      description: "估算方法选择"
      decision: "使用故事点估算"
      rationale: "团队熟悉该方法，有历史数据参考"
      alternatives_considered: ["人天估算", "T-shirt尺寸"]
      
  open_issues:
    blocking:
      - id: "ISSUE-001"
        description: "外部API接口文档未提供"
        impact: "影响3个任务的开始时间"
        required_by: "{{date}}"
    non_blocking:
      - id: "ISSUE-002"
        description: "某些任务的技能匹配度需要确认"
        suggestion: "在Sprint Planning时进一步讨论"
        
  risks:
    - id: "RISK-001"
      description: "新技术学习曲线可能影响估算准确性"
      probability: "medium"
      impact: "medium"
      mitigation: "安排技术预研阶段，预留20%缓冲时间"
      contingency: "如延期超过2天，寻求外部专家支持"
      
    - id: "RISK-002"
      description: "关键路径上的任务依赖外部团队"
      probability: "low"
      impact: "high"
      mitigation: "提前沟通，建立周同步机制"
      contingency: "准备替代方案，调整任务顺序"
      
  recommendations:
    - "建议先实现核心功能模块，再扩展辅助功能"
    - "高风险任务安排在Sprint早期，留出应对时间"
    - "每日站会重点关注关键路径任务的进展"
    - "建议使用看板工具可视化任务状态和依赖"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        name: "TASK-COVERAGE"
        value: {{actual_coverage}}
        target: 100%
        status: "pass/fail"
        
      - kpi_id: "KPI-002"
        name: "GRANULARITY-SUITABILITY"
        value: {{granularity_score}}
        target: "≥90%"
        status: "pass/fail"
        
      - kpi_id: "KPI-003"
        name: "DEPENDENCY-COMPLETENESS"
        value: {{dependency_coverage}}
        target: 100%
        status: "pass/fail"
        
      - kpi_id: "KPI-004"
        name: "ESTIMATION-ACCURACY"
        value: "待执行后评估"
        target: "±20%"
        status: "pending"
        
      - kpi_id: "KPI-005"
        name: "CLARITY-SCORE"
        value: {{clarity_rating}}
        target: "≥85/100"
        status: "pass/fail"
        
    overall_score: {{综合评分}}
    grade: "合格/优秀/卓越"
```
## Prerequisites (前置条件)

### 必需输入

| 输入项 | 类型 | 必填 | 描述 | 验证规则 |
|--------|------|------|------|----------|
| `requirements_spec` | document | 是 | 需求规格说明书 | 已批准，版本≥1.0 |
| `tech_design` | document | 是 | 技术设计方案 | 架构评审通过 |
| `team_members` | array | 是 | 团队成员列表 | 包含姓名、角色、技能标签 |
| `historical_data` | data | 否 | 历史估算数据 | 至少5个类似项目的数据 |

### 期望输出

| 输出项 | 类型 | 描述 | 质量标准 |
|--------|------|------|----------|
| `task_list` | document | 任务清单 | 100%需求覆盖，符合INVEST原则 |
| `dependency_graph` | diagram | 任务依赖图 | 清晰展示所有依赖关系 |
| `estimation_notes` | document | 估算说明 | 包含假设条件和风险说明 |
| `risk_management_plan` | document | 风险管理计划 | 识别Top 5风险及应对措施 |

### 环境要求

- **工具**: 项目管理工具（Jira/Trello等）、绘图工具（Draw.io/Lucidchart）
- **权限**: 访问需求文档库、技术方案库、历史项目数据
- **协作**: 与Tech Lead、Product Owner、开发团队的沟通渠道

## Primary Assets (主要资产)

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/decompose-task.agent.md` | 任务分解Agent，负责任务拆分执行 |
| **Prompt** | `../../prompts/decompose-task.prompt.md` | 任务拆分提示词模板 |
| **Instruction** | `../../instructions/decompose-task.instructions.md` | 任务拆分技术指令和最佳实践 |
| **Skill** | `../../skills/decompose-task/SKILL.md` | 任务拆分技能包 |

## Related Resources (相关资源)

- **Templates**: [Task List Template](../../templates/task-list.template.md)
- **Standards**: [Definition of Ready](../../standards/dor.md), [INVEST Principle](../../standards/invest.md)
- **Evaluations**: [Task Decomposition Checklist](../../evaluations/task-decomposition-checklist.md)
