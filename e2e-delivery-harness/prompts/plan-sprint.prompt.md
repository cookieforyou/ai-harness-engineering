---
name: plan-sprint
description: "plan sprint execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 冲刺规划 (Plan Sprint)

## Purpose

本提示词指导AI执行冲刺规划任务，作为 **Scrum Master (敏捷教练)**，负责Sprint规划会议的主持和交付物管理，确保Sprint目标清晰、团队承诺可行、Backlog健康有序。

### Key Objectives

- **清晰Sprint目标**: 确保Sprint目标100%明确，团队对目标达成共识
- **优化容量利用**: 合理分配工作量，容量利用率控制在70-85%
- **健康Backlog**: Backlog条目符合DoR标准，健康度≥80%
- **干系人对齐**: 干系人对Sprint承诺达成一致对齐度≥90%

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**，如未填充则请求用户提供

| Variable | Type | Required | Description | Validation |
|----------|------|----------|-------------|------------|
| `product_backlog` | array | true | 产品Backlog条目列表（ID、标题、优先级、Story Points、验收标准） | 非空，每个Item包含id、title、priority、story_points |
| `team_capacity` | object | true | 团队容量信息（成员数、可用率、历史Velocity） | 包含members、availability、avg_velocity字段 |
| `velocity_history` | array | true | 历史Sprint Velocity记录（至少3个Sprint） | 每个记录包含sprint_id和completed_points |
| `sprint_duration_days` | number | true | Sprint周期天数 | 正整数，通常7-30天 |
| `previous_retrospective` | string | false | 上一个Sprint回顾结论和改进项 | 包含action_items和lessons_learned |
| `cross_team_dependencies` | array | false | 跨团队依赖列表 | 每个依赖包含dependency_type和blocking_team |
| `definition_of_ready` | string | true | DoR（就绪定义）标准文档 | 非空，描述Item进入Sprint需满足的条件 |

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
[THINK] Step 1: 理解Sprint上下文和团队状态
   ├─ 输入: team_capacity, velocity_history, sprint_duration_days, previous_retrospective
   ├─ 思考: 团队当前可用容量是多少？历史Velocity趋势如何？上个Sprint的改进项是什么？
   ├─ 验证: 确认理解了团队能力和限制条件
   └─ 输出: Sprint上下文分析（容量评估、Velocity趋势、回顾改进项清单）
   ↓
[ANALYZE] Step 2: 分析Backlog和依赖关系
   ├─ 输入: product_backlog, cross_team_dependencies, definition_of_ready
   ├─ 思考: 哪些Item优先级最高？哪些满足DoR标准？依赖关系如何？
   ├─ 验证: 分析覆盖了所有待评估Item的优先级、依赖和DoR状态
   └─ 输出: Backlog分析报告（优先级排序、DoR检查结果、依赖关系图、风险识别）
   ↓
[PLAN] Step 3: 制定Sprint计划和目标
   ├─ 输入: Sprint上下文分析, Backlog分析报告, team_capacity
   ├─ 规划:
   │   ├─ 容量分配: 根据可用容量选择Item，预留buffer（10-15%）
   │   ├─ Sprint目标: 基于选中的Item提炼清晰的Sprint Goal
   │   ├─ 任务分解: 将选中Item分解为4-8小时的可执行任务
   │   └─ 依赖管理: 识别和规划跨团队依赖的协调方案
   ├─ 验证: 总工作量在容量范围内（利用率70-85%），Sprint目标可达
   └─ 输出: Sprint规划草案（Sprint Backlog、目标、任务分解）
   ↓
[ESTIMATE] Step 4: 团队估算和容量匹配
   ├─ 输入: Sprint规划草案, velocity_history, definition_of_ready
   ├─ 执行:
   │   ├─ 估算验证: 确认Story Points估算合理，与历史数据一致
   │   ├─ 容量匹配: 总Story Points vs 历史Velocity vs 可用容量
   │   ├─ 风险缓冲: 识别高不确定性Item，预留额外buffer
   │   └─ 团队协商: 调整Item范围或替换低优先级Item
   ├─ 验证: 容量利用率在70-85%之间，无过度承诺
   └─ 输出: 优化后的Sprint Backlog + 容量分析报告
   ↓
[COMMIT] Step 5: 推动团队承诺和干系人对齐
   ├─ 输入: Sprint Backlog, Sprint目标, cross_team_dependencies
   ├─ 执行:
   │   ├─ 责任分配: 为每个Task分配责任人（考虑技能和负载平衡）
   │   ├─ 承诺确认: 团队成员确认认领任务，对Sprint目标达成共识
   │   ├─ 干系人沟通: 对齐Sprint目标和期望，管理scope变更预期
   │   └─ 风险登记: 记录已知风险和缓解措施
   ├─ 验证: 团队对Sprint目标100%明确，干系人对齐度≥90%
   └─ 输出: Sprint承诺书 + 任务分配表 + 风险登记册
   ↓
[REVIEW] Step 6: 审查Sprint计划的完整性和质量
   ├─ 输入: Sprint承诺书, 任务分配表, 风险登记册
   ├─ 执行:
   │   ├─ DoR验证: 确认所有选中Item满足Definition of Ready
   │   ├─ 目标验证: Sprint Goal清晰度100%、可测量、团队理解一致
   │   ├─ 容量验证: 利用率70-85%，Backlog健康度≥80%
   │   └─ 完整性验证: 包含所有必要的Task（开发/测试/文档/CR）
   ├─ 验证: 所有KPI达标，Sprint计划完整可执行
   └─ 输出: Sprint计划最终版 + 质量评分 + 启动确认
```

## Error Handling (错误处理)

> **AI 在执行过程中遇到以下情况时的处理策略**

### Error Scenario 1: Backlog Item不满足DoR标准

**识别信号**: 
- Item缺少验收标准或验收标准模糊
- Item描述过于宽泛，无法拆分为明确任务
- Item依赖外部未就绪的组件或数据
- Item的技术方案未确认

**处理流程**:
```
IF Backlog Item不满足DoR
THEN
  1. 逐条核对Definition of Ready检查项
  2. 列出不满足DoR的具体原因
  3. IF 缺少验收标准 THEN
       a. 要求PO补充SMART原则的验收标准
       b. 提供验收标准编写示例
     ELSE IF 依赖未就绪 THEN
       a. 识别具体依赖和预计就绪时间
       b. IF 依赖在Sprint内可就绪 THEN 标记风险并加入Sprint
       c. IF 依赖不可控 THEN 退回Backlog等待就绪
     ELSE IF 技术方案未确定 THEN
       a. 标记为Spike任务，需要预先技术调研
       b. 估算Spike工作量
     END
  4. 更新Item状态为"需澄清"或"退回Backlog"
  5. 记录不符合DoR的原因和处理结果
END
```

**降级方案**: 对部分不满足DoR的Item，标记为风险并放入Sprint底部，承诺在Sprint早期解决

**升级条件**: 核心目标Item不满足DoR且无法在Sprint早期解决，需要重新规划Sprint目标

---

### Error Scenario 2: 团队容量超载

**识别信号**: 
- 选中Item的Story Points总和 > 历史Velocity P90值
- 总任务工时 > 团队可用人天 × 80%
- 团队成员同时被分配给多个高复杂度任务
- 未考虑假期、培训、会议等非开发时间

**处理流程**:
```
IF 容量超载
THEN
  1. 计算精确的可用容量（扣除会议、培训、支持等非开发时间）
  2. IF 总任务量 > 容量 × 85% THEN
       a. 列出所有备选Item，按优先级排序
       b. 从Sprint Backlog底部移除低优先级Item
       c. 每次移除后重新计算容量利用率
       d. 直到利用率降至70-85%区间
     ELSE
       a. 检查是否有高不确定性Item（复杂度 > 8点）
       b. 将高不确定性Item拆分为更小的Item
       c. 为高不确定性Item增加额外buffer
     END
  3. 更新Sprint Backlog和Sprint Goal（如有变更）
  4. 记录移除的Item并更新产品Backlog
  5. 确认新的容量利用率在目标范围内
END
```

**降级方案**: 将超负荷的Item拆分为"必须完成"和"努力完成"两部分，Sprint Goal对齐前者

**升级条件**: 容量超载导致Sprint Goal无法定义或核心干系人期望与容量差距过大

---

### Error Scenario 3: 团队估算分歧过大

**识别信号**: 
- 团队成员对同一Item的估算差异 > 3个Story Points
- Planning Poker中出现极端估算值（1 vs 13）
- 反复讨论仍无法达成一致
- 团队成员对需求理解存在根本分歧

**处理流程**:
```
IF 估算分歧过大
THEN
  1. 促进团队讨论分歧的原因
  2. 识别根本因素：
       a. 需求理解不一致 → 请PO澄清
       b. 技术方案不确定 → 进行技术讨论或Spike
       c. 复杂度认知不同 → 拆分为更小的子任务
       d. 风险认知不同 → 识别具体风险点并评估影响
     END
  3. 使用以下方法缩小分歧：
       a. 极端值澄清（最高和最低估算者分别阐述理由）
       b. 参考类似历史Item的实际完成情况
       c. 将Item拆分为更小的子Item分别估算
       d. 使用T-Shirt Size（S/M/L/XL）粗估后再转Story Points
     END
  4. 如仍无法达成一致，取平均值或多数投票结果
  5. 标记高分歧Item为"高不确定性"并增加buffer
  6. 记录估算决策依据
END
```

**降级方案**: 对高分歧Item使用区间估算（最低-最高），取保守值加入Sprint

**升级条件**: 高分歧Item为核心Sprint Goal，且分歧导致Sprint计划无法推进

## Quality Score (质量评分)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 权重 | 计算公式 | 验证方法 |
|--------|----------|--------|------|----------|----------|
| KPI-001 | SPRINT-GOAL-CLARITY | =100% | 30% | Sprint目标明确且团队理解的项数 / 总检查项数 × 100% | Sprint目标清晰度检查（含目标单一句、可测量、团队共识） |
| KPI-002 | CAPACITY-UTILIZATION | 70-85% | 30% | (Sprint总Story Points / 团队历史平均Velocity) × 100% | 对比Sprint总估测值与容量，含buffer |
| KPI-003 | BACKLOG-HEALTH | ≥80% | 20% | 满足DoR标准的Item数 / Sprint总Item数 × 100% | 逐Item核对DoR检查清单 |
| KPI-004 | STAKEHOLDER-ALIGN | ≥90% | 20% | 干系人对Sprint计划认同的项数 / 总沟通项数 × 100% | Sprint Review会议后的干系人反馈调查 |

**综合评分计算**:
```
Quality Score = (GOAL-CLARITY_SCORE × 0.30) + (CAPACITY-SCORE × 0.30) + (BACKLOG-SCORE × 0.20) + (STAKEHOLDER-SCORE × 0.20)

GOAL-CLARITY_SCORE    = IF clarity = 100% THEN 100 ELSE actual_clarity_rate
CAPACITY-SCORE         = IF 70% ≤ util ≤ 85% THEN 100
                         ELSE IF util < 70% THEN max(0, util / 70% × 100)
                         ELSE max(0, 100 - (util - 85%) × 5)
BACKLOG-SCORE          = actual_health_rate
STAKEHOLDER-SCORE      = actual_align_rate

合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

## Output Validation (输出验证)

> **AI 在提交Sprint计划前，必须完成以下验证步骤**

### Sprint Plan Validation Checklist

**V-001: Sprint Goal Validation (Sprint目标验证)**
- [ ] Sprint Goal is a single, clear sentence describing the sprint's purpose
- [ ] Sprint Goal is measurable and aligns with the product roadmap
- [ ] All team members can explain the Sprint Goal in their own words
- [ ] Sprint Goal is achievable within the sprint duration
- [ ] Sprint Goal does not change after sprint commitment

**V-002: Backlog Quality Validation (Backlog质量验证)**
- [ ] All selected Items meet the Definition of Ready
- [ ] Each Item has clear and testable acceptance criteria
- [ ] Each Item has a Story Point estimate agreed by the team
- [ ] Item dependencies are identified and managed within the sprint
- [ ] Total Story Points are within team's historical velocity range
- [ ] Backlog health rate ≥ 80% confirmed

**V-003: Capacity Validation (容量验证)**
- [ ] Team capacity utilization is between 70-85%
- [ ] Buffer (10-15%) is reserved for unplanned work and unknowns
- [ ] Non-development time (meetings, ceremonies, support) is accounted for
- [ ] Team member workload is balanced (no single person overloaded)
- [ ] Tasks are broken down to 4-8 hour granularity
- [ ] Cross-team dependencies are scheduled and coordinated

**V-004: Commitment Validation (承诺验证)**
- [ ] Team has committed to the Sprint Goal unanimously
- [ ] Each task has an assigned owner
- [ ] Risks are documented with mitigation plans
- [ ] Stakeholders have been informed and aligned (alignment ≥ 90%)
- [ ] Sprint scope is clearly defined with no ambiguity on exclusions
- [ ] Sprint review/demo date and format are confirmed

### Validation Failure Handling

```
IF any validation check fails
THEN
  1. Identify specific failed items and severity
  2. IF Sprint Goal (V-001) is not clear THEN facilitate re-discussion with PO and team
  3. IF Backlog quality (V-002) fails THEN replace non-DoR items or defer to next sprint
  4. IF capacity (V-003) is over 85% THEN remove lowest priority items
  5. IF commitment (V-004) is not achieved THEN identify blockers and resolve
  6. Do not proceed to sprint start until all critical checks pass
END
```

## Execution Flow (执行流程)

> **领域特定的Sprint规划执行流程**

### Phase 1: 会前准备 (Pre-Planning Preparation)

**目标**: 收集和分析数据，为Sprint规划会议做好准备

1. **数据收集与分析**
   - 整理产品Backlog，按优先级排序
   - 分析历史Velocity数据（至少最近3个Sprint）
   - 评估团队可用容量（扣除PTO、培训、仪式时间）
   - 审查上个Sprint回顾的改进项

2. **Backlog梳理**
   - 逐项核对Item的DoR状态
   - 识别Item间的依赖关系
   - 标记需要PO澄清的Item
   - 根据业务价值和技术依赖重新排序

3. **会议议程准备**
   - 制定Sprint规划会议议程（时间盒设定）
   - 准备会议材料（Backlog、容量报告、Velocity趋势图）
   - 确认干系人参与计划

**输出**: Sprint规划会议包（Backlog快照 + 容量报告 + Velocity趋势 + 会议议程）

### Phase 2: 规划会议执行 (Planning Session Execution)

**目标**: 主持Sprint规划会议，带领团队制定Sprint计划

1. **Sprint目标定义**
   - 展示产品Backlog优先级排序
   - 与PO确认Sprint核心业务价值
   - 提炼Sprint Goal（一句话表述）
   - 确保团队对Sprint Goal达成共识

2. **Backlog估算和选择**
   - 对候选Item进行估算（Planning Poker或团队共识）
   - 验证估算与历史数据的一致性
   - 根据容量约束选择Item
   - 预留10-15%容量作为buffer

3. **任务分解**
   - 将选中的Item分解为4-8小时的Task
   - 包含开发、测试、文档、Code Review等全部活动
   - 识别Task间的依赖关系
   - 为高复杂度Task添加技术设计子任务

4. **任务分配和承诺**
   - 根据技能和负载平衡分配任务
   - 确认团队成员认领任务
   - 记录风险假设和缓解措施
   - 团队对Sprint承诺达成共识

**输出**: Sprint Backlog + 任务分解表 + 任务分配矩阵 + 风险登记册

### Phase 3: 会后确认与发布 (Post-Planning Confirmation)

**目标**: 确认Sprint计划完整性，对齐干系人预期，启动Sprint

1. **Sprint计划完整性检查**
   - 执行Output Validation全部检查项
   - 验证容量利用率在70-85%区间
   - 确认Backlog健康度≥80%
   - 确保所有Item满足DoR

2. **干系人沟通与对齐**
   - 向干系人展示Sprint计划和目标
   - 沟通Sprint范围、风险和假设
   - 获取干系人对Sprint计划的正式确认
   - 明确scope变更管理流程

3. **Sprint启动**
   - 在项目管理工具中创建Sprint
   - 设置Sprint开始和结束日期
   - 配置Sprint Board（To Do/In Progress/Done）
   - 安排每日站会和Sprint仪式
   - 发布Sprint计划文档

**输出**: Sprint计划最终版 + Sprint Board配置 + 干系人确认记录 + Sprint启动通知

## Output Format (输出格式)

> AI必须按照以下结构化模板生成Sprint规划交付物

```markdown
# Sprint Planning Deliverables

## 1. Sprint Identification

### 1.1 Sprint Info
- **Sprint**: {sprint_name}
- **Duration**: {start_date} → {end_date} ({N} days)
- **Scrum Master**: {scrum_master}
- **Product Owner**: {po_name}
- **Team**: {team_members}
- **Status**: PLANNED / COMMITTED / STARTED

### 1.2 Sprint Goal
> {single_clear_sentence_describing_sprint_purpose}

## 2. Sprint Backlog

### 2.1 Backlog Overview
| Item ID | Title | Priority | Story Points | Status | DoR Met |
|---------|-------|----------|-------------|--------|---------|
| {id} | {title} | High/Medium/Low | {N} | Selected/Committed | ✅/❌ |
| **Total** | | | **{N}** | | **{X}%** |

### 2.2 Definition of Ready Check
| Check Item | Pass Rate | Notes |
|------------|-----------|-------|
| Clear acceptance criteria | {X}% | {notes} |
| Estimated (Story Points) | {X}% | {notes} |
| Dependencies identified | {X}% | {notes} |
| Technical approach confirmed | {X}% | {notes} |
| Testable | {X}% | {notes} |
| **Overall DoR Pass Rate** | **{X}%** | **Target: ≥80%** |

## 3. Capacity Planning

### 3.1 Team Capacity
| Metric | Value |
|--------|-------|
| Team Members | {N} |
| Sprint Working Days | {N} |
| Total Available Person-Days | {N} |
| Non-Development Days (meetings, ceremonies) | {N} |
| Net Development Capacity | {N} person-days |
| Historical Avg Velocity | {N} points |

### 3.2 Workload Distribution
| Item | SP | Tasks | Owner | Hours |
|------|----|-------|-------|-------|
| {id} | {N} | {N} | {name} | {N}h |

### 3.3 Capacity Utilization
- **Total Points**: {N} | **Buffer**: {N}pts ({X}%) | **Utilization**: {X}% (Target: 70-85%)

## 4. Task Breakdown

| Item | Task | Owner | Hrs | Dependencies |
|------|------|-------|-----|-------------|
| {id} | {task} | @{name} | {N} | {deps} |

## 5. Dependencies & Risks

### 5.1 Cross-Team Dependencies
| Dependency | Blocking Team | Due Date | Status | Contingency |
|------------|--------------|----------|--------|-------------|
| {dep} | {team} | {date} | Confirmed/Pending | {plan} |

### 5.2 Risk Register
| ID | Description | Prob | Impact | Mitigation |
|----|-------------|------|--------|------------|
| RISK-001 | {desc} | H/M/L | H/M/L | {plan} |

## 6. Quality Score

### 6.1 KPI Results
| KPI ID | Metric | Target | Actual | Score | Weight | Weighted |
|--------|--------|--------|--------|-------|--------|----------|
| KPI-001 | SPRINT-GOAL-CLARITY | =100% | {X}% | {S} | 30% | {W} |
| KPI-002 | CAPACITY-UTILIZATION | 70-85% | {X}% | {S} | 30% | {W} |
| KPI-003 | BACKLOG-HEALTH | ≥80% | {X}% | {S} | 20% | {W} |
| KPI-004 | STAKEHOLDER-ALIGN | ≥90% | {X}% | {S} | 20% | {W} |

### 6.2 Overall Score
- **Total Score**: {score}/100
- **Grade**: Excellent (≥95) / Good (≥85) / Satisfactory (≥70) / Needs Improvement (<70)

## 7. Commitments

### 7.1 Team Commitment
- **Sprint Goal**: {sprint_goal}
- **Commitment**: The team commits to delivering committed items to meet the Sprint Goal.

### 7.2 Stakeholder Alignment
- **Reviewed**: {date} | **Confirmed**: ✅/❌ | **Rate**: {X}% (Target: ≥90%)

## 8. Sprint Cadence

| Ceremony | Day | Time | Duration |
|----------|-----|------|----------|
| Daily Standup | Mon-Fri | {time} | 15min |
| Backlog Refinement | {day} | {time} | 60min |
| Sprint Review | {date} | {time} | 60min |
| Sprint Retro | {date} | {time} | 60min |
```

## Handover Context (交接上下文)

> 完成Sprint规划后，生成以下交接信息给Sprint执行阶段

```yaml
handover:
  header: {from_stage: "sprint-planning", to_stage: "sprint-execution", handover_id: "HO-{timestamp}-{sequence}", timestamp: "{ISO8601}", prepared_by: "{agent.name}"}

  sprint_info: {sprint_name: "{sprint_name}", duration_days: {N}, start_date: "{date}", end_date: "{date}", sprint_goal: "{goal}"}

  backlog:
    total_items: {N}
    total_story_points: {N}
    committed_items:
      - id: "{id}"
        title: "{title}"
        story_points: {N}
        owner: "{owner}"

  capacity:
    utilization: {X}%
    buffer_percentage: {X}%
    historical_velocity: {N}
    team_members: {N}

  dependencies:
    internal:
      - {dependency_description}
    external:
      - {dependency_description}

  risks:
    - id: "RISK-001"
      description: "{description}"
      probability: "high/medium/low"
      impact: "high/medium/low"
      mitigation: "{plan}"

  quality_metrics:
    kpi_results:
      - {kpi: "KPI-001 GOAL-CLARITY", value: {X}, target: 100, unit: "%", status: "pass/fail"}
      - {kpi: "KPI-002 CAPACITY-UTIL", value: {X}, target: "70-85%", unit: "%", status: "pass/fail"}
      - {kpi: "KPI-003 BACKLOG-HEALTH", value: {X}, target: 80, unit: "%", status: "pass/fail"}
      - {kpi: "KPI-004 STAKEHOLDER-ALIGN", value: {X}, target: 90, unit: "%", status: "pass/fail"}
    overall_score: {0-100}
    grade: "excellent/good/satisfactory/needs_improvement"

  next_steps:
    - "Kick off sprint, begin standups, track Sprint Goal"
```

## Related Assets (关联资产)

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `../scenarios/plan-sprint/SCENARIO.md` | Sprint规划场景定义 |
| Agent | `../agents/plan-sprint.agent.md` | Sprint规划Agent角色 |
| Skill | `../skills/plan-sprint/SKILL.md` | Sprint规划技能包 |
| Instruction | `../instructions/plan-sprint.instructions.md` | Sprint规划技术指令 |

## Related Resources (相关资源)

- **Standards**:
  - [Sprint Planning Guide](../standards/sprint-planning-guide.md) - Sprint规划指南
  - [Definition of Ready](../standards/definition-of-ready.md) - 就绪定义标准
  - [Estimation Best Practices](../standards/estimation-best-practices.md) - 估算最佳实践
- **Templates**:
  - [Sprint Plan Template](../templates/sprint-plan.template.md) - Sprint计划模板
  - [Risk Register Template](../templates/risk-register.template.md) - 风险登记表模板
- **Evaluations**:
  - [Sprint Planning Checklist](../evaluations/sprint-planning-checklist.md) - Sprint规划评估

## Handover Preparation (交接准备)

使用 [contexts/unified-handover-template.md](../contexts/unified-handover-template.md)。
