# 任务拆分场景 / Task Decomposition Scenario

> **阶段**: P3 — 任务拆分
> **核心 Agent**: `agents/project-manager`
> **目标输出**: 可执行任务计划（Epic → Story → Task 树、关键路径、里程碑、风险）
> **效力等级**: P0（强制）

---

## 场景概述

本场景基于 P2 阶段输出的 ADR，将架构设计拆分为可执行、可追踪的任务清单。输出物包含任务树（Epic → Story → Task）、关键路径、并行组、工时估算及风险清单，为开发实现阶段提供清晰的执行蓝图。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `adr_doc` | `object` | 是 | P2 阶段输出的架构决策记录 ADR |
| `team_capacity` | `string` | 是 | 团队资源（人数、角色、可用工时/迭代） |
| `iteration_constraints` | `string` | 是 | 迭代约束（截止日期、里程碑、外部依赖） |
| `risk_appetite` | `string` | 否 | 风险容忍度：`conservative` / `balanced` / `aggressive` |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "plan_title": "迭代计划",
  "version": "1.0.0",
  "epics": [
    {
      "id": "E-001",
      "title": "...",
      "stories": [
        {
          "id": "S-001",
          "title": "...",
          "tasks": [
            {
              "id": "T-001",
              "title": "...",
              "description": "...",
              "estimated_hours": { "optimistic": 2, "most_likely": 4, "pessimistic": 8 },
              "dependencies": ["T-002"],
              "assignee_role": "backend|frontend|devops|qa",
              "risk_level": "low|medium|high"
            }
          ]
        }
      ]
    }
  ],
  "critical_path": ["T-001", "T-003", "T-005"],
  "parallel_groups": [
    ["T-002", "T-004"],
    ["T-006", "T-007"]
  ],
  "total_estimated_hours": { "optimistic": 40, "most_likely": 60, "pessimistic": 90 },
  "milestones": [
    { "name": "...", "date": "YYYY-MM-DD", "deliverables": ["..."] }
  ],
  "risks": [
    { "id": "R-001", "description": "...", "probability": "low|medium|high", "impact": "low|medium|high", "mitigation": "...", "owner": "..." }
  ],
  "external_dependencies": [
    { "id": "D-001", "description": "...", "blocking_tasks": ["T-001"], "expected_ready_date": "YYYY-MM-DD", "fallback": "..." }
  ]
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **Project Manager** | 任务拆分、工时估算、依赖分析、关键路径识别、里程碑规划 | 迭代计划 JSON |
| **人类项目经理** | 确认资源分配合理性、审批里程碑计划、接受或调整风险清单 | 已确认的执行计划 |

---

## 质量检查要点

- [ ] 任务拆分粒度满足：单个任务可在 1-2 天内完成，最大不超过 3 天
- [ ] 依赖关系形成有向无环图（DAG），无循环依赖
- [ ] 工时估算采用三点估算（乐观/最可能/悲观），禁止绝对精确数字
- [ ] 关键路径上的任务分配经验丰富的执行者
- [ ] 外部依赖明确阻塞任务、预计就绪日期及降级方案
- [ ] 输出通过 `evaluations/task-decomposition-checkpoint.yaml` 质量门禁

---

## 上游衔接

接收 `scenarios/tech-arch-design/` 的输出（`{{adr_doc}}`）。
衔接规范详见 `standards/scenario-integration.md#P2→P3`。

## 下游衔接

本场景输出直接作为 `scenarios/code-review/` 的上下文输入（任务清单用于确定代码审查范围）。
衔接规范详见 `standards/scenario-integration.md#P3→P4`。
