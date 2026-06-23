---
name: plan-sprint
description: "Detailed technical instructions for plan-sprint scenario execution"
applyTo: "scenarios/plan-sprint/**"
phase: requirement-analysis
type: instruction
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['instruction', 'technical']
---
# Instructions: 冲刺规划 (Plan Sprint)

## Overview

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

## Conservative Strategy (Recommended)
承诺容量 = 可用容量 * 0.8
适用于: 新团队、不稳定需求、高风险 Sprint

## Balanced Strategy
承诺容量 = 可用容量 * 0.9
适用于: 成熟团队、稳定需求

## Aggressive Strategy
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

## Deliverable Templates

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

## Best Practices

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

## Associated Assets

| 类型 | 路径 |
|------|------|
| SCENARIO | `../../scenarios/plan-sprint/SCENARIO.md` |
| PROMPT | `../../prompts/plan-sprint.prompt.md` |
| AGENT | `../../agents/plan-sprint.agent.md` |
| SKILL | `../../skills/plan-sprint/SKILL.md` |


## Technical Specifications

> Detailed technical requirements and implementation guidelines for plan-sprint.

### Required Tools
- **Jira / Linear / Azure DevOps Boards**: Sprint Backlog 管理与任务跟踪
- **Planning Poker / Scrum Poker / Pointing Poker**: 估算协作工具
- **Miro / Mural / FigJam**: 虚拟白板（Sprint Planning / Retro 可视化）
- **Confluence / Notion / GitBook**: Sprint 文档与会议记录
- **Burndown Chart 生成器**: Sprint 进度可视化（内置于 Jira / 自定义脚本）

### Environment Requirements
- Backlog 已排序且顶部的 User Stories 满足 Definition of Ready（DoR）
- 团队可用容量已计算（扣除公共假期、休假、On-Call 轮值、跨团队支持）
- Sprint 目标草案已由 Product Owner 准备（≤1 句话，可衡量的业务成果）
- 历史速率数据可获取（最近 3-5 个 Sprint 的完成 Story Points）

### Configuration Parameters
- `SPRINT_LENGTH`: Sprint 周期（推荐 2 周，固定不可变）
- `VELOCITY_SAMPLE_SIZE`: 速率计算样本数（默认 3 个 Sprint，排除异常值）
- `CAPACITY_BUFFER`: 容量缓冲比例（20-30%，应对紧急工作和上下文切换）
- `FOCUS_FACTOR`: 团队专注因子（0.6-0.8，扣除会议/Code Review/沟通开销）
- `MAX_WIP`: 在制品数量上限（= 团队人数 × 1.5，防止多任务并行）


## Multi-Language Code Examples

### Jira API - Fetch Sprint Issues (Python)

```python
#!/usr/bin/env python3
"""
Jira API client to fetch sprint issues and calculate velocity.
Requires: pip install requests python-dotenv
"""
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://your-domain.atlassian.net")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


class JiraSprintClient:
    """Client for interacting with Jira Sprint data."""

    def __init__(self, base_url: str, email: str, api_token: str):
        self.base_url = base_url.rstrip("/")
        self.auth = (email, api_token)
        self.headers = {"Accept": "application/json"}

    def get_board_sprints(self, board_id: int, state: str = "active") -> List[Dict]:
        """Fetch sprints for a given board."""
        url = f"{self.base_url}/rest/agile/1.0/board/{board_id}/sprint"
        params = {"state": state}
        resp = requests.get(url, auth=self.auth, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.json().get("values", [])

    def get_sprint_issues(self, sprint_id: int) -> List[Dict]:
        """Fetch all issues in a sprint."""
        url = f"{self.base_url}/rest/agile/1.0/sprint/{sprint_id}/issue"
        params = {"fields": "summary,status,storypoints,customfield_10016"}
        resp = requests.get(url, auth=self.auth, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.json().get("issues", [])

    def calculate_velocity(self, sprint_id: int) -> Dict:
        """
        计算 Sprint Velocity: 已完成故事点 / 总承诺故事点
        Returns velocity ratio and detailed breakdown.
        """
        issues = self.get_sprint_issues(sprint_id)
        total_points = 0
        completed_points = 0
        breakdown = []

        for issue in issues:
            fields = issue.get("fields", {})
            story_points = fields.get("customfield_10016") or fields.get("storypoints", 0)
            status = fields.get("status", {}).get("name", "")
            issue_key = issue.get("key", "")

            total_points += story_points
            if status.lower() in ("done", "closed", "completed"):
                completed_points += story_points

            breakdown.append({
                "key": issue_key,
                "summary": fields.get("summary", ""),
                "points": story_points,
                "status": status,
            })

        velocity = round(completed_points / total_points * 100, 2) if total_points else 0
        return {
            "sprint_id": sprint_id,
            "total_points": total_points,
            "completed_points": completed_points,
            "velocity_pct": velocity,
            "remaining_points": total_points - completed_points,
            "issue_breakdown": breakdown,
        }


# Usage
if __name__ == "__main__":
    client = JiraSprintClient(JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN)
    sprints = client.get_board_sprints(board_id=1)
    for sprint in sprints[:3]:
        report = client.calculate_velocity(sprint["id"])
        print(f"Sprint {report['sprint_id']}: "
              f"Velocity={report['velocity_pct']}% "
              f"({report['completed_points']}/{report['total_points']} pts)")
```

### Jira API - Fetch Sprint Issues (JavaScript/TypeScript)

```typescript
/**
 * Jira Sprint velocity calculator for Node.js.
 * Run: npx ts-node jira-velocity.ts
 */
import axios, { AxiosInstance } from "axios";

interface JiraIssue {
  key: string;
  fields: {
    summary: string;
    status: { name: string };
    customfield_10016?: number;
    storypoints?: number;
  };
}

interface VelocityReport {
  sprintId: number;
  totalPoints: number;
  completedPoints: number;
  velocityPct: number;
  remainingPoints: number;
  issues: Array<{ key: string; summary: string; points: number; status: string }>;
}

class JiraSprintService {
  private client: AxiosInstance;

  constructor(baseUrl: string, email: string, apiToken: string) {
    this.client = axios.create({
      baseURL: baseUrl.replace(/\/$/, ""),
      auth: { username: email, password: apiToken },
      headers: { Accept: "application/json" },
    });
  }

  /** Fetch all issues belonging to a sprint and compute velocity. */
  async calculateVelocity(sprintId: number): Promise<VelocityReport> {
    const { data } = await this.client.get<{ issues: JiraIssue[] }>(
      `/rest/agile/1.0/sprint/${sprintId}/issue`,
      { params: { fields: "summary,status,customfield_10016" } }
    );

    let totalPoints = 0;
    let completedPoints = 0;
    const issues: VelocityReport["issues"] = [];

    for (const issue of data.issues) {
      const pts = issue.fields.customfield_10016 ?? issue.fields.storypoints ?? 0;
      const done = ["done", "closed", "completed"].includes(
        issue.fields.status?.name?.toLowerCase() ?? ""
      );
      totalPoints += pts;
      if (done) completedPoints += pts;
      issues.push({ key: issue.key, summary: issue.fields.summary, points: pts, status: issue.fields.status?.name ?? "" });
    }

    return {
      sprintId,
      totalPoints,
      completedPoints,
      velocityPct: totalPoints ? +(completedPoints / totalPoints * 100).toFixed(2) : 0,
      remainingPoints: totalPoints - completedPoints,
      issues,
    };
  }
}
```

### GitHub Projects API - Sprint Planning Automation (Python)

```python
#!/usr/bin/env python3
"""
GitHub Projects (Beta) API integration for sprint planning.
Requires: pip install pygithub
"""
import os
from datetime import datetime, timedelta
from github import Github, GithubIntegration

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ORG_NAME = os.getenv("GITHUB_ORG", "your-org")
PROJECT_NUMBER = 1  # GitHub Projects project number


def create_sprint_iteration(project_id: str, title: str, duration_days: int = 14):
    """
    Create a new iteration (sprint) field in GitHub Projects.
    Uses GraphQL API since PyGithub doesn't fully support Projects v2.
    """
    import requests

    query = """
    mutation($project: ID!, $field: ID!, $iteration: CreateProjectV2IterationInput!) {
      createProjectV2Iteration(input: { projectId: $project, fieldId: $field, iteration: $iteration }) {
        iteration {
          id
          title
          startDate
          duration
        }
      }
    }
    """
    variables = {
        "project": project_id,
        "field": "FIELD_NODE_ID",  # Replace with actual iteration field ID
        "iteration": {
            "title": title,
            "start_date": datetime.now().isoformat(),
            "duration": duration_days,
        },
    }
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    resp = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def get_team_velocity_history(org: str, repo: str, sprints: int = 5) -> float:
    """
    Fetch completed issues from recent milestones to calculate average velocity.
    """
    g = Github(GITHUB_TOKEN)
    repo_obj = g.get_repo(f"{org}/{repo}")
    milestones = list(repo_obj.get_milestones(state="closed"))[:sprints]

    total_pts = 0
    completed_pts = 0
    for milestone in milestones:
        for issue in repo_obj.get_issues(milestone=milestone, state="closed"):
            pts = 0
            for label in issue.labels:
                if label.name.startswith("pts-"):
                    pts = int(label.name.replace("pts-", ""))
            completed_pts += pts

        for issue in repo_obj.get_issues(milestone=milestone, state="all"):
            pts = 0
            for label in issue.labels:
                if label.name.startswith("pts-"):
                    pts = int(label.name.replace("pts-", ""))
            total_pts += pts

    return round(completed_pts / total_pts * 100, 2) if total_pts else 0


# Usage: predict capacity for next sprint
def predict_capacity(team_size: int, avg_velocity: float, sprint_days: int = 10) -> dict:
    """
    基于历史 Velocity 预测下一个 Sprint 可完成的 Story Points。
    结合团队规模和历史交付能力进行预测。
    """
    historical_capacity = avg_velocity * team_size * 0.1  # normalized
    recommended = historical_capacity * 0.85  # 15% buffer
    aggressive = historical_capacity * 0.95  # 5% buffer
    return {
        "avg_velocity_pct": avg_velocity,
        "team_size": team_size,
        "recommended_points": round(recommended),
        "aggressive_points": round(aggressive),
        "sprint_days": sprint_days,
    }
```

### Excel-Based Velocity Calculation Template

```python
#!/usr/bin/env python3
"""
Generate an Excel workbook for sprint velocity tracking and planning.
Requires: pip install openpyxl
"""
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


def create_velocity_tracker(output_path: str = "sprint_velocity.xlsx"):
    """Generate a standard Sprint Velocity tracking spreadsheet."""
    wb = Workbook()

    # --- Sheet 1: Sprint Data ---
    ws = wb.active
    ws.title = "Sprint Velocity"
    headers = [
        "Sprint", "Start Date", "End Date", "Committed Points",
        "Completed Points", "Velocity %", "Team Size", "Notes"
    ]
    # Style header row
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    thin_border = Border(
        left=Side(style="thin"), right=Side(style="thin"),
        top=Side(style="thin"), bottom=Side(style="thin")
    )

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")
        cell.border = thin_border

    # Sample data rows
    sample_data = [
        ["Sprint 1", "2026-01-06", "2026-01-19", 40, 35, 87.5, 5, ""],
        ["Sprint 2", "2026-01-20", "2026-02-02", 45, 40, 88.9, 5, "Holiday impact"],
        ["Sprint 3", "2026-02-03", "2026-02-16", 42, 38, 90.5, 6, "New member onboarded"],
        ["Sprint 4", "2026-02-17", "2026-03-02", 50, 42, 84.0, 6, ""],
        ["Sprint 5", "2026-03-03", "2026-03-16", 48, 44, 91.7, 6, "Stable velocity"],
    ]
    for row_idx, row_data in enumerate(sample_data, 2):
        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="center")

    # Add formula for average velocity
    avg_row = len(sample_data) + 2
    ws.cell(row=avg_row, column=1, value="Average Velocity").font = Font(bold=True)
    ws.cell(row=avg_row, column=6, value="=AVERAGE(F2:F{0})".format(len(sample_data) + 1))
    ws.cell(row=avg_row, column=6).border = thin_border

    # --- Sheet 2: Capacity Planner ---
    ws2 = wb.create_sheet("Capacity Planner")
    ws2.cell(row=1, column=1, value="Sprint Capacity Planning Tool").font = Font(bold=True, size=14)
    planner_headers = ["Parameter", "Value", "Description"]
    for col, h in enumerate(planner_headers, 1):
        cell = ws2.cell(row=3, column=col, value=h)
        cell.font = header_font
        cell.fill = header_fill

    planner_data = [
        ["Team Members", 6, "Number of developers"],
        ["Sprint Days", 10, "Working days in sprint"],
        ["Hours per Day", 6.5, "Effective coding hours"],
        ["Utilization Rate", "0.8", "80% focus factor"],
        ["Buffer", "0.85", "15% buffer for unknowns"],
        ["Historical Velocity", 89.4, "Average from Sheet 1"],
        ["Forecasted Points", "=B4*B5*B6*B7*B8/8", "Estimated story points"],
    ]
    for row_idx, row_data in enumerate(planner_data, 4):
        for col_idx, value in enumerate(row_data, 1):
            ws2.cell(row=row_idx, column=col_idx, value=value).border = thin_border

    # --- Chart ---
    chart = BarChart()
    chart.type = "col"
    chart.title = "Sprint Velocity Trend"
    chart.y_axis.title = "Velocity %"
    chart.x_axis.title = "Sprint"

    data_ref = Reference(ws, min_col=6, min_row=1, max_row=len(sample_data) + 1)
    cats_ref = Reference(ws, min_col=1, min_row=2, max_row=len(sample_data) + 1)
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.shape = 4

    ws.add_chart(chart, "A{0}".format(len(sample_data) + 4))

    # Set column widths
    for ws_target in [ws, ws2]:
        for col in range(1, 15):
            ws_target.column_dimensions[get_column_letter(col)].width = 18

    wb.save(output_path)
    print(f"Velocity tracker saved to {output_path}")
```

### Planning Poker Consensus Calculator

```python
#!/usr/bin/env python3
"""
Planning Poker consensus calculator with statistical outlier detection.
Helps the team converge on a final estimate by identifying disagreements.
"""
import statistics
from typing import List, Tuple

# Standard Scrum story point values (Fibonacci)
FIBONACCI = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100]


def nearest_fibonacci(value: float) -> int:
    """Map a raw estimate to the nearest Fibonacci number."""
    return min(FIBONACCI, key=lambda x: abs(x - value))


def calculate_poker_consensus(votes: List[float]) -> dict:
    """
    计算 Planning Poker 投票结果并检测异常值.

    Args:
        votes: List of story point estimates from each team member.

    Returns:
        Dict with consensus estimate, outlier detection, and recommendation.
    """
    if len(votes) < 3:
        return {"consensus": nearest_fibonacci(statistics.median(votes)),
                "confidence": "low", "outliers": []}

    median_vote = statistics.median(votes)
    mean_vote = statistics.mean(votes)
    stdev = statistics.stdev(votes) if len(votes) > 1 else 0

    # Detect outliers using IQR method
    sorted_votes = sorted(votes)
    q1 = sorted_votes[len(sorted_votes) // 4]
    q3 = sorted_votes[(3 * len(sorted_votes)) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = [v for v in votes if v < lower_bound or v > upper_bound]

    # Determine consensus level
    cv = stdev / mean_vote if mean_vote > 0 else 0  # Coefficient of variation
    if cv < 0.2:
        confidence = "high"
    elif cv < 0.4:
        confidence = "medium"
    else:
        confidence = "low"

    # Remove outliers and re-estimate
    filtered_votes = [v for v in votes if lower_bound <= v <= upper_bound]
    if filtered_votes:
        consensus = nearest_fibonacci(statistics.median(filtered_votes))
    else:
        consensus = nearest_fibonacci(median_vote)

    return {
        "consensus": consensus,
        "median": median_vote,
        "mean": round(mean_vote, 1),
        "std_dev": round(stdev, 2),
        "cv": round(cv, 2),
        "confidence": confidence,
        "outliers": sorted(outliers),
        "votes_cast": len(votes),
        "needs_discussion": confidence != "high",
    }


# Simulate a Planning Poker session
if __name__ == "__main__":
    # Team votes for a User Story
    team_votes = [5, 8, 5, 3, 8, 5, 13]  # 7 developers
    result = calculate_poker_consensus(team_votes)
    print(f"Votes: {team_votes}")
    print(f"Consensus: {result['consensus']} pts (confidence: {result['confidence']})")
    print(f"Outliers detected: {result['outliers']}")
    if result["needs_discussion"]:
        print("Action: High/low estimators need to explain their reasoning")
```

## Error Handling

### Error Scenario 1: Velocity历史数据不足 (P2)

**触发条件**: 团队为新组建或 Sprint 数量不足 3 个，无法计算可靠的 Velocity 基线

**处理流程**:
```
IF 历史 Sprint 数据 < 3 个
THEN
  1. 首次 Sprint 采用行业基准数据（建议初始 Velocity = 团队人数 × 0.6）
  2. 首次 Sprint 采用 Conservative 承诺策略（承诺容量 = 容量 × 0.6）
  3. 记录每个成员的实际完成点数，建立基线
  4. 第二次 Sprint 使用前一次实际数据修正
  5. 第三次 Sprint 开始使用移动平均计算
END
```

**降级方案**: 采用 T-Shirt Size 粗略估算（S/M/L/XL），不依赖 Story Points

**升级条件**: 连续两个 Sprint Velocity < 50%，需 Coach 介入团队能力评估

### Error Scenario 2: Backlog DoR (Definition of Ready) 不达标 (P2)

**触发条件**: Sprint Planning 中发现超过 30% 的 Backlog Items 不满足 DoR 条件

**处理流程**:
```
IF DoR 达标率 < 70%
THEN
  1. 标记不合格 Items 并列出具体缺陷（无AC、无UI稿、依赖未确认）
  2. 将不合格 Items 退回 PO 重新准备
  3. 优先用合格的 Items 填充 Sprint Backlog
  4. 若合格 Items 不足 Sprint 容量 70%:
     a. 从 Done 池中选取技术债务/优化项补充
     b. 考虑缩短 Sprint 周期
  5. 记录 DoR 缺陷类型并反馈给 PO 改进
END
```

**降级方案**: 允许部分 Items 带有低风险 DoR 缺陷进入 Sprint，但需在 Sprint 前 3 天补齐

**升级条件**: 连续 2 个 Sprint DoR 达标率 < 60%，需要升级至 Engineering Manager 介入流程改进

### Error Scenario 3: 跨团队依赖破裂 (P1)

**触发条件**: Sprint 执行中识别到关键外部依赖无法按时交付，影响 Sprint Goal 达成

**处理流程**:
```
IF 外部依赖阻塞 > 3 天
THEN
  1. 立即识别依赖破裂的影响范围（哪些 Items 被阻塞）
  2. 与依赖方召开紧急协调会议，评估替代方案
  3. 尝试以下缓解措施:
     a. 寻找内部替代实现（Mock/Stub）
     b. 调整 Backlog Items 顺序，先做独立部分
     c. 借用依赖方工程师短期支援
  4. IF 无法缓解 THEN 将依赖项移出 Sprint，补充同等工作量 Items
  5. 更新 Sprint Backlog 和 Sprint Goal（如需要 PO 同意）
  6. 记录依赖破裂原因到 Retrospective Agenda
END
```

**降级方案**: 切分 User Story，先完成不依赖外部部分的子任务，保证 Sprint 产出物完整性

**升级条件**: Sprint Goal 完全无法达成，需要 PO 重新确认优先级并调整发布计划

### Error Scenario 4: 团队容量超负荷承诺 (P2)

**触发条件**: 团队承诺的故事点超过计算容量的 110%，或人均 Sprint 工时超过可用时间的 120%

**处理流程**:
```
IF 承诺点数 > 容量 × 1.1
THEN
  1. 展示历史数据：超负荷承诺 → 交付质量下降 → 技术债务增加
  2. 强制削减承诺至容量 × 0.9（Balanced 策略）
  3. 优先保留高价值、高优先级的 Items
  4. 将超出的 Items 明确标记为 Stretch Goal
  5. 与 PO 沟通削减理由并获得确认
END
```

**降级方案**: 接受部分 Stretch Goal，但不计入 Sprint 承诺，完成即 bonus

**升级条件**: PO 坚持原计划不削减，升级至 Engineering Manager 风险评估

## Quality Standards

> Acceptance criteria and quality gates for plan-sprint deliverables.

| Standard | Criteria | Verification Method |
|----------|----------|---------------------|
| Standard 1 | Sprint commitment accuracy is 80% or higher | Automated check |
| Standard 2 | Capacity utilization is 85-95% | Automated check |
| Standard 3 | Carryover rate is 20% or lower | Automated check |
## References

- [harness-engineering.md](../standards/harness-engineering.md)
- [output-validation-checklist.md](../evaluations/output-validation-checklist.md)
- [regression-checklist.md](../evaluations/regression-checklist.md)
