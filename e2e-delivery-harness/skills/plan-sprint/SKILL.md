---
name: plan-sprint
description: "Domain skill for plan-sprint execution"
category: requirement
type: skill
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['skill', 'knowledge']
---
# Skill: 冲刺规划 (Plan Sprint)

## Overview

本 Skill 定义了 Sprint Planning 的核心知识体系，涵盖故事估算方法、速率计算、容量规划、DoR/DoD 标准及 INVEST 原则。适用于 Scrum Master、Product Owner 及敏捷开发团队进行高效 Sprint 规划。

## Core Knowledge

### 估算技术

| 技术 | 适用场景 | 精度 | 耗时 |
|------|---------|------|------|
| **Planning Poker** | 团队估算，消除锚定偏差 | 高 | 中等 |
| **T-shirt Sizing (S/M/L/XL)** | 初期预估，快速分类 | 中 | 低 |
| **Affinity Estimation** | 大量 Backlog 快速排序 | 中高 | 低 |
| **Bucket System** | 50+ Item 批量估算 | 中 | 极低 |

#### T-shirt Sizing 参考映射

| Size | Story Points | 工作量参考 | 示例 |
|------|-------------|-----------|------|
| XS | 1 | ≤2 小时 | 文案修改、配置变更 |
| S | 2 | 2-4 小时 | 简单功能、单API |
| M | 3-5 | 1-2 天 | 标准功能、多API交互 |
| L | 8-13 | 3-5 天 | 复杂功能、涉及多个模块 |
| XL | 21+ | ≥1 周 | 史诗级、需拆分 |

### 速率计算 (Velocity Calculation)

```
速率 = 过去 N 个 Sprint 完成的 Story Points 总和 / N
推荐 N = 3-5（排除异常 Sprint，如节假日、大规模人员变动）
```

#### 容量缓冲

```
有效速率 = 计算速率 × (1 - 缓冲比例)
缓冲比例 = 20-30%（用于处理突发事件、Bug 修复、代码审查等不可预知工作）
```

### Sprint 容量公式

```
Sprint 总容量 = (团队人数 × 每人可用小时数 × 聚焦因子) - 缓冲时间
```

- **团队人数**: 实际参与开发的成员数（排除 PO、SM）
- **每人可用小时数**: Sprint 总工作时间 × 0.6-0.7（扣除会议、代码审查、沟通等）
- **聚焦因子**: 0.6-0.8（根据团队成熟度调整，成熟团队取高值）
- **缓冲时间**: 总容量的 20-30%

**示例**: 5人团队，每人可用6小时/天，Sprint 10天，聚焦因子 0.7，缓冲 25%
```
容量 = (5 × 6 × 10 × 0.7) × (1 - 0.25) = 210 × 0.75 = 157.5 人时
```

### Definition of Ready (DoR)

User Story 进入 Sprint 前必须满足的条件：

1. **描述清晰**: 用户故事描述完整，PO 和团队理解一致
2. **验收标准**: 有明确、可测试的 Acceptance Criteria（≥3 条）
3. **依赖已识别**: 外部/内部依赖已识别并确认可用
4. **估算完成**: 团队已完成相对估算（Story Points）
5. **优先级明确**: PO 已确定其在 Backlog 中的优先级
6. **粒度合适**: 可在 1 个 Sprint 内完成（否则需拆分）

### Definition of Done (DoD)

故事标记为"完成"时必须满足的 checklist：

1. 代码已完成并提交（≥1 次 Code Review 通过）
2. 所有单元测试通过，覆盖率 ≥80%
3. 集成测试 / E2E 测试通过
4. API 文档已更新（如适用）
5. 无障碍 / 性能 / 安全验证通过
6. PO 验收通过（Demo 或 UAT）

### INVEST 原则

优秀的 User Story 应满足：

| 原则 | 含义 | 反例 |
|------|------|------|
| **I**ndependent | 独立可交付，减少依赖 | "用户登录后才能..." |
| **N**egotiable | 可协商细节，非合同 | "必须用Redis实现" |
| **V**aluable | 对用户/业务有价值 | "修改数据库索引"（技术任务） |
| **E**stimable | 可估算工作量 | "系统性能更好"（模糊） |
| **S**mall | 足够小，1个Sprint内完成 | "重构整个支付系统" |
| **T**estable | 有明确测试方法 | "用户体验更好"（主观） |

### 敏捷仪式速查

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

    def calculate_velocity(self, sprints: list) -> float:
        """
        计算团队速率，排除异常 Sprint

        Args:
            sprints: Sprint 列表，每项含 completed_points 和 metadata

        Returns:
            velocity: 平均速率（排除 P<0.05 异常值后）
        """
        import statistics

        points = [s.completed_points for s in sprints if s.completed_points > 0]
        if len(points) < 2:
            return sum(points) / len(points) if points else 0.0

        # 排除异常值（超出均值的 2 个标准差）
        mean = statistics.mean(points)
        stdev = statistics.stdev(points)
        filtered = [p for p in points if abs(p - mean) <= 2 * stdev]

        return sum(filtered) / len(filtered) if filtered else mean

    def plan_sprint(self, backlog: list, capacity_hours: float,
                    velocity: float, focus_factor: float = 0.7) -> dict:
        """
        Sprint Planning 核心流程

        Args:
            backlog: 排好优先级的 Backlog
            capacity_hours: 可用人时
            velocity: 团队速率（Story Points）
            focus_factor: 聚焦因子 (0-1)

        Returns:
            plan: {selected_items, total_points, capacity_used, slack_time}
        """
        # 1. 容量缓冲
        effective_capacity = capacity_hours * (1 - 0.25)  # 25% buffer
        max_points = velocity * (effective_capacity / capacity_hours)

        # 2. 选择 Items (按优先级，不超过容量)
        selected = []
        total_points = 0
        for item in sorted(backlog, key=lambda x: x.priority, reverse=True):
            if total_points + item.story_points <= max_points:
                if self._check_dor(item):
                    selected.append(item)
                    total_points += item.story_points

        # 3. 分解任务
        tasks = self._break_down(selected)

        # 4. 制定计划
        plan = {
            "selected_items": selected,
            "total_points": total_points,
            "capacity_used": total_points / velocity * 100,
            "slack_hours": effective_capacity * 0.15,  # 额外 Slack
        }

        return plan

    def _check_dor(self, item) -> bool:
        """检查 Definition of Ready"""
        checks = [
            hasattr(item, 'acceptance_criteria') and len(item.acceptance_criteria) >= 3,
            hasattr(item, 'story_points') and item.story_points > 0,
            hasattr(item, 'priority') and item.priority > 0,
        ]
        return all(checks)

    def _break_down(self, items: list) -> list:
        """将 User Story 分解为开发任务"""
        tasks = []
        for item in items:
            task_template = [
                {"type": "coding", "hours": item.story_points * 0.5},
                {"type": "testing", "hours": item.story_points * 0.3},
                {"type": "review", "hours": item.story_points * 0.1},
                {"type": "documentation", "hours": item.story_points * 0.1},
            ]
            tasks.extend(task_template)
        return tasks
```

## Best Practices

1. **速率驱动规划**：基于最近 3-5 个 Sprint 的平均速率（排除异常值 P<0.05）进行容量规划，容量缓冲取 20-30%，避免过度承诺（承诺率 ≤80%）。Sprint 中若发现无法完成所有承诺项，优先与 PO 协商缩减范围而非加班。速率数据仅用于团队自身规划参考，禁止跨团队横向对比速率值。

2. **优先级分层**：使用 MoSCoW 方法（Must/Should/Could/Won't）将 Backlog 分为 4 层，每层明确占比上限（Must ≤60%），确保非核心需求不挤占关键交付。Must 必须先经过技术可行性评估，Should 项作为扩容备选。PO 每周 Review 一次优先级分层，确保反映最新业务需求变化。

3. **Sprint 目标聚焦**：每个 Sprint 定义 1 个 Sprint Goal（≤1 句话），所有 Sprint Backlog Item 必须直接支撑 Goal。Sprint 中不接受偏离 Goal 的变更请求（如有紧急需求走正式的变更流程）。Sprint Review 时首先评估是否达成 Sprint Goal，而非逐个检查 Item 完成情况。

## Common Pitfalls

### Pitfall 1: 速率膨胀预期

- **Risk**：管理层持续要求"提升速率"，团队为满足期望而虚增 Story Points（"膨胀"），导致 Sprint 完成率看似提升但实际产出下降。一旦开始膨胀，速率作为规划工具的价值完全丧失。
- **Prevention**：明确告知管理层速率用于规划而非考核，禁止将速率纳入绩效 KPI。建立 Story Points 一致性网格（Reference Story），供团队校准估算标准。速率下降时引导团队分析根因（技术债务？需求复杂度？），而非简单要求"做得更快"。
- **Impact**：Story Points 通货膨胀，跨团队可比性完全丧失。团队丧失估算信心，Sprint 规划变为"凑数字"游戏，交付质量下降。

### Pitfall 2: Sprint Backlog 过度填充

- **Risk**：将 Sprint 视为"必须全部完成"的承诺，填满 100% 容量，无缓冲处理紧急问题和未预见的复杂度。一旦出现突发 Bug 或需求变更，团队被迫加班或降低完成标准。
- **Prevention**：预留 20-30% 的 Slack/Buffer 时间用于处理突发事件。Sprint 中仅接受明确 Fail-fast 条件的变更（某 Item 明显不可行时及时丢弃）。建立"Pull"机制而非"Push"：Team 根据实际进度 Pull 下一个 Item，而非 PO Push 固定列表。
- **Impact**：持续过量承诺导致团队 burnout，缺陷率上升。未完成的 Item 累积为"Sprint 溢出"效应，破坏速率计算的准确性。

### Pitfall 3: 忽视 DoD 质量门槛

- **Risk**：为在 Sprint 截止前"完成"项目，跳过代码审查、自动化测试、文档更新等 DoD 项目，标注为"完成 + 技术债务"。短期看似提高了速率，长期导致代码腐化速度指数级增长。
- **Prevention**：DoD 清单在 Sprint Planning 中逐项确认并获得团队共识。未通过 DoD 的 Item 不得标记为 Done（即使 PO 口头同意）。建立"完成质量"看板：Done 数量 / 真正通过 DoD 数量，跟踪质量趋势。Sprint Retrospective 中单独 Review 所有跳过 DoD 项的情况。
- **Impact**：技术债务指数级增长，修复成本随延迟呈非线性上升。新功能开发速度持续下降，最终进入"重写还是继续维护"的两难困境。

## 相关资产

- **标准**: `../../standards/requirement-standard.md`
- **标准**: `../../standards/agile-standard.md`
- **评估**: `../../evaluations/sprint-planning-quality.json`
- **评估**: `../../evaluations/backlog-health-check.json`
