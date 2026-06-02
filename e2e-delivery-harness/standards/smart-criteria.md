# SMART 目标与需求编写标准

## SMART 定义

| 字母 | 含义 | 检查问题 |
|------|------|----------|
| S | Specific 具体 | 是否明确「谁、做什么、在哪」？ |
| M | Measurable 可衡量 | 是否有数字、比例或可追溯指标？ |
| A | Achievable 可达成 | 在约束内是否现实？ |
| R | Relevant 相关 | 是否支撑业务目标 OBJ-*？ |
| T | Time-bound 有时限 | 是否有截止日期或迭代？ |

## 业务目标写法（OBJ-*）

```markdown
- OBJ-001: {动词}{对象} — KPI: {指标名} — Target: {数值} — By: {日期/迭代}
```

**反例**：提升用户体验  
**正例**：OBJ-001: 将结账完成率从 62% 提升至 75% — KPI: checkout_completion_rate — Target: 75% — By: Sprint 3

## 功能需求（REQ-*）

采用用户故事 + 验收标准：

```markdown
### REQ-001: {标题}
**Story**: As a {角色}, I want {能力}, so that {价值}.
**Priority**: P0|P1|P2|P3
**Acceptance** (Given-When-Then):
- AC-001: Given ... When ... Then ...
```

详见 [user-story-format.md](user-story-format.md)。

## 与 Harness Goal 层对齐

每条 REQ 必须在追溯矩阵中映射到至少一个 OBJ-*（100% 覆盖，见 KPI REQ-COVER ≥95%）。
