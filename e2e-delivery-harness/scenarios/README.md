# Scenarios

Scenarios 是 **AI 执行入口**：组合 Agent、Prompt、Instruction、Skill，并提供 Chain of Thought、错误处理与 KPI。

## 命名与路径

- 目录：`scenarios/{verb-noun}/`（与五类资产基名一致）
- 主文件：`SCENARIO.md`
- 示例：`scenarios/analyze-requirement/SCENARIO.md`

## 标准章节（Harness 合规）

见 [standards/harness-engineering.md](../standards/harness-engineering.md)。

| 章节 | Harness 层 |
|------|------------|
| Purpose | Goal |
| Chain of Thought | Strategy |
| Decision Checkpoints | Strategy / Constraint |
| Error Handling | Constraint + Feedback |
| Quality Metrics | Feedback |
| Handover Criteria | Observability |

## 工作流

```
加载 SCENARIO.md → Agent → Prompt（变量+验证+交接）→ Instruction/Skill（按需）
→ evaluations 自检 → 输出 Handover YAML
```

## 核心 vs 扩展场景

- **核心 7**：与 [e2e-delivery.pipeline.md](../workflows/e2e-delivery.pipeline.md) `stages` 一致
- **扩展 30**：专项深化，见 [AGENTS.md](../AGENTS.md) 场景目录

## 相关资产

- [AGENTS.md](../AGENTS.md) — Agent 导航
- [templates/scenario-template/](../templates/scenario-template/) — 场景模板
