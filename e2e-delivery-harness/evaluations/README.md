# Evaluations

Evaluations 是**质量评估工具**，用于验证资产和交付物是否满足质量标准。

## 概述

评估资产包括：

- **回归检查清单 (regression-checklist.md)**：按交付阶段的详细质量检查清单
- **评分卡模板 (scorecard-template.md)**：质量评估的加权评分
- **输出验证 (output-validation-checklist.md)**：通用 V-* 验证
- **常见错误模式 (common-error-patterns.md)**：反模式库
- **阶段专检**：需求、架构、任务、测试、部署、监控、热修复等专项清单（共 28 个文件，含 README）

## 文件结构

```
evaluations/
├── regression-checklist.md
├── scorecard-template.md
├── output-validation-checklist.md
├── common-error-patterns.md
├── requirement-quality-checklist.md
├── acceptance-criteria-review.md
├── architecture-review-checklist.md
├── task-quality-checklist.md
├── test-quality-checklist.md
├── deployment-quality-checklist.md
├── monitoring-quality-checklist.md
├── hotfix-quality-checklist.md
└── …
```

## 使用方式

### 阶段准出

1. 完成 [output-validation-checklist.md](output-validation-checklist.md) 通用项
2. 完成 [regression-checklist.md](regression-checklist.md) 对应阶段章节
3. 对照场景 Related Resources 中的专项 evaluation
4. 填写 Handover `quality_metrics.kpi_results`

## 相关资产

- **Standards**: [../standards/](../standards/) - 质量评分与 Harness 合规
- **Scenarios**: [../scenarios/](../scenarios/) - 阶段 KPI 与 DC-* 定义
