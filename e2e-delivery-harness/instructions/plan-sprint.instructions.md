# Instructions: 冲刺规划 (Plan Sprint)

## 概述

本文档定义了 Sprint Planning 的详细技术规范和最佳实践。

## Sprint Planning 流程

### 时间盒管理

| 阶段 | 时长 | 产出 |
|------|------|------|
| 需求澄清 | 60 分钟 | 澄清的 Backlog Items |
| 工作量估算 | 60 分钟 | 估算值 |
| 任务分解 | 60 分钟 | Task List |
| 承诺评审 | 30 分钟 | Sprint Commitment |

### Sprint Goal 定义

**良好 Sprint Goal 的特征**:

```markdown
# Good Example
"在 2 周内完成用户认证模块，支持邮箱/手机注册、登录、找回密码功能"

# Bad Examples
- "完成用户模块" (模糊)
- "完成所有待办事项" (不可测量)
- "重构登录系统" (范围不明确)
```

### 需求澄清指南

#### Backlog Item 结构

```yaml
backlog_item:
  id: "USR-001"
  title: "用户注册功能"
  description: "用户可以通过邮箱或手机号注册账号"
  priority: "high"  # high, medium, low
  story_points: 5   # 斐波那契数列: 1, 2, 3, 5, 8, 13, 21
  acceptance_criteria:
    - "支持邮箱格式验证"
    - "密码长度 8-20 位"
    - "注册成功发送确认邮件"
  dependencies:
    - "需要设计团队提供 UI 设计稿"
    - "依赖用户中心服务 API"
  definitions:
    done: "功能测试通过且已部署到测试环境"
```

#### 澄清会议议程

```python
CLARIFICATION_AGENDA = """
1. 开场 (5 min)
   - 回顾 Sprint Goal 候选
   - 确认参会人员

2. Backlog Review (40 min)
   - 按优先级逐项讨论
   - 每个 Item 不超过 5 分钟

3. 依赖梳理 (10 min)
   - 识别跨团队依赖
   - 识别技术依赖

4. 排序确认 (5 min)
   - 最终优先级确认
   - 确认纳入 Sprint 的 Items
"""

def run_clarification_meeting(items):
    """执行澄清会议"""
    agenda = CLARIFICATION_AGENDA
    clarified = []

    for item in items:
        clarified_item = clarify_single_item(item)
        clarified.append(clarified_item)

    return clarified
```

### 工作量估算

#### 故事点估算

**估算维度**:

| 维度 | 说明 | 权重 |
|------|------|------|
| 复杂度 | 技术实现的复杂程度 | 30% |
| 工作量 | 实际需要的工作时间 | 40% |
| 风险 | 潜在的不确定性和风险 | 20% |
| 依赖 | 外部依赖和协调成本 | 10% |

**相对估算基准**:

```python
STORY_POINT_REFERENCE = {
    1: "1-2 小时，一个简单任务",
    2: "半天，一个简单但不熟悉的领域",
    3: "1 天，一个常规任务",
    5: "2-3 天，一个有多个子任务的功能",
    8: "1 周，一个复杂功能",
    13: "2 周，一个需要深入研究的功能",
    21: "3-4 周，一个大型功能或存在高不确定性"
}

def estimate_story_points(item, reference=STORY_POINT_REFERENCE):
    """
    估算故事点
    使用相对估算，对比参考项
    """
    complexity = assess_complexity(item)
    effort = assess_effort(item)
    risk = assess_risk(item)

    # 综合评估
    raw_points = calculate_points(complexity, effort, risk)

    # 映射到斐波那契数列
    return map_to_fibonacci(raw_points)
```

#### Planning Poker

**执行流程**:

```python
def planning_poker(team, item):
    """
    Planning Poker 执行流程
    """
    # 1. PO 描述 Item
    po.describe(item)

    # 2. 团队提问 (3-5 分钟)
    team.ask_questions()

    # 3. 团队独立估算
    estimates = team.estimate_independently()

    # 4. 展示估算结果
    team.reveal_estimates()

    # 5. 高低估算者解释
    high_estimator, low_estimator = team.explain_extremes()

    # 6. 重新估算 (重复直到收敛)
    while not converged(estimates):
        estimates = team.reestimate()

    # 7. 达成共识
    final_estimate = consensus(estimates)
    return final_estimate
```

### 任务分解

#### 任务分解模板

```yaml
task:
  title: "实现用户注册 API"
  parent_item: "USR-001"
  assignee: "@zhangsan"
  estimated_hours: 8
  status: "TODO"
  subtasks:
    - title: "设计数据库表结构"
      hours: 2
    - title: "实现注册接口"
      hours: 4
    - title: "编写单元测试"
      hours: 2
  dependencies:
    - "USR-001-DB"
  labels:
    - "backend"
    - "api"
```

#### 分解指南

| 类型 | 任务示例 | 建议时长 |
|------|----------|----------|
| 开发 | 实现功能代码 | 4-8 小时 |
| 测试 | 编写测试用例 | 2-4 小时 |
| 集成 | API 联调 | 2-4 小时 |
| 文档 | 编写接口文档 | 1-2 小时 |
| Review | Code Review | 1-2 小时 |

### 容量规划

#### Capacity 计算

```python
def calculate_capacity(team, sprint_days, holidays=[]):
    """
    计算 Sprint 可用容量
    """
    # 基础工时
    base_hours = team.members * team.hours_per_day * sprint_days

    # 扣除假期
    working_days = sprint_days - len(holidays)
    available_hours = team.members * team.hours_per_day * working_days

    # 考虑可用率
    utilization = team.avg_utilization  # e.g., 0.8
    capacity = available_hours * utilization

    # 考虑 Buffer
    buffer = 0.1  # 10% Buffer
    final_capacity = capacity * (1 - buffer)

    return final_capacity
```

#### 承诺策略

```python
COMMITMENT_STRATEGY = """
# 容量承诺策略

## 保守策略 (推荐)
承诺容量 = 可用容量 * 0.8
适用于: 新团队、不稳定需求、高风险 Sprint

## 平衡策略
承诺容量 = 可用容量 * 0.9
适用于: 成熟团队、稳定需求

## 激进策略
承诺容量 = 可用容量
适用于: 高绩效团队、低风险 Sprint
"""

def determine_commitment(capacity, strategy='conservative'):
    if strategy == 'conservative':
        return capacity * 0.8
    elif strategy == 'balanced':
        return capacity * 0.9
    else:
        return capacity
```

## 交付物模板

### Sprint Plan 模板

```markdown
# Sprint Plan: Sprint #{number}

## Sprint Goal
{Goal Description}

## Sprint Duration
{start_date} - {end_date} ({duration} days)

## Team Capacity
| 成员 | 可用天数 | 备注 |
|------|----------|------|
| 张三 | 10 天 | 缺席 2 天 |
| 李四 | 12 天 | 全勤 |

**总可用容量**: {total_points} 故事点

## Sprint Backlog

| ID | 标题 | 故事点 | 状态 |
|----|------|--------|------|
| USR-001 | 用户注册功能 | 5 | TODO |

## Task Board

| Task | Owner | 估算 | Item |
|------|-------|------|------|
| T-001 | @张三 | 8h | USR-001 |

## Risks & Dependencies

### Risks
- [ ] 风险 1: 设计稿可能延期

### Dependencies
- [ ] 依赖: 设计团队 - UI 设计稿

## Commitment
团队承诺完成 {commitment_points} 故事点
置信度: {confidence}%
```

## 最佳实践

### DO

1. **充分准备**: 提前阅读所有 Backlog Items
2. **控制时间盒**: 每个阶段严格按时结束
3. **团队共识**: 估算必须经过团队讨论达成共识
4. **留有 Buffer**: 承诺容量预留 10-20% Buffer
5. **明确验收标准**: 每个 Item 都有清晰验收标准

### DON'T

1. **不要匆忙估算**: 没有理解需求前不要估算
2. **不要过度承诺**: 超出容量会导致质量下降
3. **不要遗漏依赖**: 外部依赖是常见风险来源
4. **不要模糊目标**: Sprint Goal 必须具体可测量
5. **不要单人决策**: 任务分配需团队协商

## 关联资产

| 类型 | 路径 |
|------|------|
| SCENARIO | `../../scenarios/plan-sprint/SCENARIO.md` |
| PROMPT | `../../prompts/plan-sprint.prompt.md` |
| AGENT | `../../agents/product-owner.agent.md` |
| SKILL | `../../skills/plan-sprint/SKILL.md` |
