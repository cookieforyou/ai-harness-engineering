# Skill: 冲刺规划 (Plan Sprint)

## 概述

本 Skill 定义了 Sprint Planning 的核心知识体系。

## 核心知识

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

## 关联资产

- **Scenario**: `../../scenarios/plan-sprint/SCENARIO.md`
- **Instruction**: `../../instructions/plan-sprint.instructions.md`
- **Prompt**: `../../prompts/plan-sprint.prompt.md`
- **Agent**: `../../agents/product-owner.agent.md`
