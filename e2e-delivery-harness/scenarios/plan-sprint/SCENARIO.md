# Scenario: 冲刺规划 (Plan Sprint)

## 概述

Sprint Planning 是敏捷开发中的核心仪式，负责定义冲刺周期内的目标与任务分配。

## 核心决策点

| 阶段 | 决策点 | 输出 |
|------|--------|------|
| 需求澄清 | Backlog Item Selection | Sprint Goal |
| 任务分解 | Task Breakdown | Task List |
| 资源评估 | Capacity Planning | Sprint Commitment |

## 执行流程

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

## 决策检查点

- [ ] **需求完整性**: 所有纳入的 Backlog Item 是否有清晰定义？
- [ ] **估算合理性**: 工作量估算是否经过团队共识？
- [ ] **容量匹配**: Sprint Commitment 是否在团队容量范围内？
- [ ] **依赖识别**: 是否识别并记录了所有跨团队依赖？

## 错误处理

| 场景 | 处理方式 |
|------|----------|
| 估算分歧 | 使用 Planning Poker 达成共识 |
| 容量超载 | 减少 Backlog Item 或延长期限 |
| 需求不清 | 推迟该 Item 到澄清会议 |

## 交接标准

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

## 关联资产

| 类型 | 路径 |
|------|------|
| SCENARIO | `scenarios/plan-sprint/SCENARIO.md` |
| PROMPT | `prompts/plan-sprint.prompt.md` |
| INSTRUCTIONS | `instructions/plan-sprint.instructions.md` |
| AGENT | `agents/plan-sprint.agent.md` |
| SKILL | `skills/plan-sprint/SKILL.md` |


## Purpose

> Define the objectives and scope of the plan-sprint scenario.
>
> This scenario ensures systematic execution of plan-sprint activities with clear decision checkpoints and handover criteria.


## Prerequisites

- [ ] Prerequisite 1: [Description]
- [ ] Prerequisite 2: [Description]
- [ ] Prerequisite 3: [Description]


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

## Error Handling

### Error Scenario 1
**Error**: [Description]
**Handling**: [Resolution steps]

### Error Scenario 2
**Error**: [Description]
**Handling**: [Resolution steps]


## Handover Criteria

- [ ] Criterion 1: [Description]
- [ ] Criterion 2: [Description]
- [ ] Criterion 3: [Description]
