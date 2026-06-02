---
name: plan-sprint
description: "Domain skill for plan-sprint execution"
category: requirement
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['skill', 'knowledge']
---
# Skill: 冲刺规划 (Plan Sprint)

## Overview

本 Skill 定义了 Sprint Planning 的核心知识体系。

## Core Knowledge

### 敏捷方法论

```python
class SprintPlanningSkill:
    """Sprint Planning 技能"""

    def __init__(self):
        self.ceremonies = {
            "sprint_planning": {
                "duration": "2-4 hours",
                "frequency": "每 Sprint 开始时",
                "participants": ["PO", "SM", "Dev Team"]
            },
            "daily_standup": {
                "duration": "15 minutes",
                "frequency": "每天",
                "participants": ["Dev Team"]
            },
            "sprint_review": {
                "duration": "1-2 hours",
                "frequency": "每 Sprint 结束时",
                "participants": ["PO", "Stakeholders", "Team"]
            },
            "retrospective": {
                "duration": "1-2 hours",
                "frequency": "每 Sprint 结束时",
                "participants": ["Team", "SM"]
            }
        }

    def calculate_velocity(self, sprints):
        """
        计算团队速率
        Velocity = 完成的 Story Points 总和 / Sprint 数量
        """
        completed_points = sum(s.completed_points for s in sprints)
        return completed_points / len(sprints)

    def plan_sprint(self, backlog, capacity, velocity):
        """
        Sprint Planning 核心流程
        """
        # 1. 选择 Items
        selected = self.select_items(backlog, capacity, velocity)

        # 2. 分解任务
        tasks = self.break_down(selected)

        # 3. 制定计划
        plan = SprintPlan(selected, tasks, capacity)

        return plan
```

## Associated Assets

- **Scenario**: `../../scenarios/plan-sprint/SCENARIO.md`
- **Instruction**: `../../instructions/plan-sprint.instructions.md`
- **Prompt**: `../../prompts/plan-sprint.prompt.md`
- **Agent**: `../../agents/plan-sprint.agent.md`


## Core Knowledge

> Essential knowledge domain for plan-sprint execution.

### Domain Fundamentals
- [Core concept 1]
- [Core concept 2]
- [Core concept 3]

### Key Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]


## Best Practices

> Proven practices for plan-sprint excellence.

1. **Practice 1**: [Description and rationale]
2. **Practice 2**: [Description and rationale]
3. **Practice 3**: [Description and rationale]


## Anti-patterns (反模式)

> 与 Common Pitfalls 同义，执行时合并检查。

## Common Pitfalls

> Frequent mistakes to avoid during plan-sprint execution.

### Pitfall 1: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 2: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]

### Pitfall 3: [Name]
**Risk**: [Description]
**Prevention**: [How to avoid]
**Impact**: [Consequences if not avoided]
