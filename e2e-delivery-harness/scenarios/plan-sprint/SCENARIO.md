---
name: plan-sprint
description: "Plan Sprint scenario for the E2E delivery lifecycle"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Scenario: 冲刺规划 (Plan Sprint)

## Overview

Sprint Planning 是敏捷开发中的核心仪式，负责定义冲刺周期内的目标与任务分配。

## Core Decision Points

| 阶段 | 决策点 | 输出 |
|------|--------|------|
| 需求澄清 | Backlog Item Selection | Sprint Goal |
| 任务分解 | Task Breakdown | Task List |
| 资源评估 | Capacity Planning | Sprint Commitment |

## Execution Flow

```python
class SprintPlanning:
    """冲刺规划流程"""

    def execute(self, backlog_items, team_capacity, sprint_duration):
        """
        1. 澄清需求 (60分钟)
        2. 估算工作量 (60分钟)
        3. 任务分解 (60分钟)
        4. 承诺评审 (30分钟)
        """
        # Step 1: 需求澄清
        clarified_items = self.clarify_requirements(backlog_items)

        # Step 2: 估算工作量
        estimated_items = self.estimate_effort(clarified_items)

        # Step 3: 任务分解
        task_list = self.break_down_tasks(estimated_items)

        # Step 4: 承诺评审
        sprint_goal, commitment = self.review_commitment(
            task_list, team_capacity, sprint_duration
        )

        return SprintPlan(sprint_goal, commitment, task_list)

    def clarify_requirements(self, items):
        """需求澄清"""
        # 1. 逐项讨论
        # 2. 明确验收标准
        # 3. 识别依赖
        # 4. 确认优先级
        pass

    def estimate_effort(self, items):
        """工作量估算"""
        # 1. 使用故事点或人天
        # 2. 参考历史速率
        # 3. 考虑风险系数
        pass

    def break_down_tasks(self, items):
        """任务分解"""
        # 1. 识别子任务
        # 2. 分配责任人
        # 3. 估算子任务工时
        pass
```

## Decision Checkpoints

- [ ] **需求完整性**: 所有纳入的 Backlog Item 是否有清晰定义？
- [ ] **估算合理性**: 工作量估算是否经过团队共识？
- [ ] **容量匹配**: Sprint Commitment 是否在团队容量范围内？
- [ ] **依赖识别**: 是否识别并记录了所有跨团队依赖？

## Error Handling

| 场景 | 处理方式 |
|------|----------|
| 估算分歧 | 使用 Planning Poker 达成共识 |
| 容量超载 | 减少 Backlog Item 或延长期限 |
| 需求不清 | 推迟该 Item 到澄清会议 |

## Handover Standards

### Sprint Planning 完成标准

```
✅ Sprint Goal 明确定义
✅ Sprint Backlog 已选择并排序
✅ Task Breakdown 完成
✅ Sprint Commitment 已达成共识
✅ 团队成员均已认领任务
```

### 交付物

1. **Sprint Goal**: 冲刺目标声明
2. **Sprint Backlog**: 选中的 Backlog Item 列表
3. **Task Board**: 任务分解与分配
4. **Sprint Burndown**: 燃尽图基准

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `scenarios/plan-sprint/SCENARIO.md` |
| PROMPT | `prompts/plan-sprint.prompt.md` |
| INSTRUCTIONS | `instructions/plan-sprint.instructions.md` |
| AGENT | `agents/plan-sprint.agent.md` |
| SKILL | `skills/plan-sprint/SKILL.md` |


## Purpose

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




> Define the objectives and scope of the plan-sprint scenario.
>
> This scenario ensures systematic execution of plan-sprint activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: Product backlog is groomed and prioritized
- [ ] Prerequisite 2: Team capacity and availability are confirmed
- [ ] Prerequisite 3: Definition of Ready criteria are established


## Primary Assets

| Asset Type | Path | Description |
|------------|------|-------------|
| Scenario | `scenarios/plan-sprint/SCENARIO.md` | This scenario definition |
| Prompt | `prompts/plan-sprint.prompt.md` | Execution prompt |
| Instructions | `instructions/plan-sprint.instructions.md` | Technical instructions |
| Agent | `agents/plan-sprint.agent.md` | Responsible agent |
| Skill | `skills/plan-sprint/SKILL.md` | Domain skill |


## Chain of Thought

1. Understand the context and requirements for plan-sprint
2. Analyze dependencies and constraints
3. Execute core activities systematically
4. Validate outputs against acceptance criteria
5. Document decisions and handover state


## Decision Checkpoints

| Checkpoint | Question | Decision Options |
|------------|----------|-----------------|



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



## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `COMMITMENT-ACCURACY` | ≥80% | 承诺准确率：实际完成/承诺完成 |
| `CAPACITY-UTIL` | 85-95% | 容量利用率：实际使用/可用容量 |
| `CARRYOVER-RATE` | ≤20% | 遗留率：遗留到下次冲刺的故事占比 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识



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



## Handover Criteria

- [ ] Criterion 1: Sprint backlog is committed and documented
- [ ] Criterion 2: All stories meet Definition of Ready standards
- [ ] Criterion 3: Risk register is reviewed and mitigations are in place


### Handover Context Template

```yaml
handover:
  header:
    from_stage: "plan-sprint"
    to_stage: "unknown"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```

