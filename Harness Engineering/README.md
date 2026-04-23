# AI Harness Engineering Assets

> **版本**: v2.0.0
> **定位**: AI 驱动软件交付的 E2E（端到端）全生命周期工作流统一资产库
> **原则**: 沉淀 · 编排 · 复用 · 闭环

---

## 目录结构

```
AI-Harness-Engineering/
├── agents/           # Agent 定义与角色配置
├── evaluations/      # 评估体系与质量门禁
├── instructions/     # 系统指令与行为约束
├── prompts/          # 场景化提示词资产
├── scenarios/        # E2E 工作流场景编排（覆盖全生命周期）
├── skills/           # 可复用技能模块
├── standards/        # 规范标准与最佳实践
├── templates/        # 项目模板与脚手架
├── copilot-instructions.md
├── INTRODUCTION.zh.md / INTRODUCTION.en.md
├── USAGE.zh.md / USAGE.en.md
└── README.md
```

---

## 快速开始

1. **了解体系**: 阅读 [INTRODUCTION.zh.md](./INTRODUCTION.zh.md)
2. **使用规范**: 参考 [USAGE.zh.md](./USAGE.zh.md)
3. **选取资产**: 根据所处交付阶段从 `scenarios/` 选取对应场景
4. **定制扩展**: 在 `agents/`、`skills/` 中按需沉淀新资产

---

## E2E 全生命周期覆盖

本资产库覆盖软件交付的六大核心阶段，各阶段通过标准化接口无缝衔接：

| 阶段 | 场景目录 | 核心 Agent | 输出物 |
| :--- | :--- | :--- | :--- |
| **需求分析** | `scenarios/requirements-analysis/` | Product Analyst | 用户故事、验收标准、RFC |
| **技术架构** | `scenarios/tech-arch-design/` | Solution Architect | 架构图、技术选型、接口契约 |
| **任务拆分** | `scenarios/task-decomposition/` | Project Manager | 任务清单、依赖图、工时估算 |
| **开发实现** | `scenarios/code-review/` | Senior Engineer | 审查报告、修复建议 |
| **部署迭代** | `scenarios/deployment-pipeline/` | DevOps Engineer | CI/CD 配置、部署脚本、回滚策略 |
| **健康监控** | `scenarios/health-monitoring/` | DevOps Engineer | 监控规则、告警策略、健康报告 |

阶段衔接规范详见 `standards/e2e-workflow-lifecycle.md`。

---

## 核心设计原则

| 原则 | 说明 |
| :--- | :--- |
| **统一沉淀** | 所有 AI 资产集中管理，避免散落在各项目仓库中 |
| **编排复用** | 场景通过组合 skills + prompts + agents 实现，支持声明式编排 |
| **版本受控** | 关键资产遵循语义化版本（SemVer），变更可追溯 |
| **质量门禁** | 每个资产入库前必须通过 `evaluations/` 中的对应评测集 |
| **E2E 闭环** | 从需求输入 → 场景选择 → Agent 执行 → 评估反馈 → 监控迭代，全链路覆盖 |
| **阶段衔接** | 前一阶段的输出 Schema 与后一阶段的输入 Schema 强制兼容 |

---

## 贡献指南

- 新增资产前请先查阅 `standards/` 中的相关规范
- 提交前在本地运行对应 `evaluations/` 脚本验证
- 所有 Markdown 文件需同时提供中英文版本（或至少中文）
- 新增场景必须补充对应阶段的衔接规范（`standards/scenario-integration.md`）
