# AI Harness Engineering Assets

> **版本**: v1.0.0  
> **定位**: E2E 交付过程中的 AI 工作流统一资产库  
> **原则**: 沉淀 · 编排 · 复用

---

## 目录结构

```
AI-Harness-Engineering/
├── agents/           # Agent 定义与角色配置
├── evaluations/      # 评估体系与质量门禁
├── instructions/     # 系统指令与行为约束
├── prompts/          # 场景化提示词资产
├── scenarios/        # E2E 工作流场景编排
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
3. **选取资产**: 根据场景从 `scenarios/` 或 `templates/` 开始
4. **定制扩展**: 在 `agents/`、`skills/` 中按需沉淀新资产

---

## 核心设计原则

| 原则 | 说明 |
| :--- | :--- |
| **统一沉淀** | 所有 AI 资产集中管理，避免散落在各项目仓库中 |
| **编排复用** | 场景通过组合 skills + prompts + agents 实现，支持声明式编排 |
| **版本受控** | 关键资产遵循语义化版本（SemVer），变更可追溯 |
| **质量门禁** | 每个资产入库前必须通过 `evaluations/` 中的对应评测集 |
| **E2E 闭环** | 从需求输入 → 场景选择 → Agent 执行 → 评估反馈，全链路覆盖 |

---

## 贡献指南

- 新增资产前请先查阅 `standards/` 中的相关规范
- 提交前在本地运行对应 `evaluations/` 脚本验证
- 所有 Markdown 文件需同时提供中英文版本（或至少中文）
