# E2E Delivery Harness — AI 工程化资产库

> **合规状态**：🟢 **95.3% A+** | 282 资产全部 A 级 | 8/8 类别 A 级 | 零 B/C/D/F 资产

## 项目概述

E2E Delivery Harness 是一套基于 **Harness Engineering（驾驭工程）** 理念的 AI 工程化资产库。通过 37 个场景 × 5 类资产（Scenario + Agent + Prompt + Instruction + Skill）的模块化设计，覆盖软件交付全生命周期（需求 → 设计 → 开发 → 测试 → 部署 → 运维 → 治理），提供标准化、可复用、可评估的 AI 工作流模板。

## 核心价值

- **Harness Engineering 六层对齐**：Goal / Strategy / Tooling / Constraint / Feedback / Observability 映射到每类资产，见 [standards/harness-engineering.md](./standards/harness-engineering.md)
- **37 场景 × 5 资产 = 185 个一一映射的执行单元**：统一 `{verb}-{noun}` 命名，开箱即用
- **量化质量门禁**：7 个 Q-* 门禁 + 28 个 MET-* KPI + 3 级阈值（70/85/95）
- **强制思维链 (CoT)**：7 步标签体系（THINK→ANALYZE→DESIGN→IMPLEMENT→VERIFY→HANDOVER），每步 VALIDATE
- **机器可读 Handoff YAML**：100% Agent 使用结构化 YAML 交接，`to_stage` 100% 可路由
- **282 资产全部 A 级**：通过 1974 项自动化合规检查，零占位符残留
- **可评估可自我修复**：27 个 Evaluation 清单 + P0-P4 错误升级机制 + 10 类反模式库

## 资产全景

```
e2e-delivery-harness/
├── AGENTS.md                          # Agent 导航图与执行协议（R1-R5）
├── 资产库全面评估深度分析报告.md       # 全库深度评估（v3.0 最终版）
├── README.md                          # 本文件
├── INTRODUCTION.zh.md / .en.md        # 中英文介绍
├── USAGE.zh.md / .en.md               # 中英文使用指南
├── copilot-instructions.md            # Copilot/IDE 集成指引
│
├── scenarios/      37 × SCENARIO.md   # 场景入口（Purpose + CoT + DC-* + KPI）
├── agents/         37 × .agent.md     # 角色身份（Role + I/O + Handoff YAML）
├── prompts/        37 × .prompt.md    # 执行脚本（Variables → CoT → Validation）
├── instructions/   37 × .instructions.md  # 操作 Runbook（工具+环境+配置）
├── skills/         37 × SKILL.md      # 领域知识包（Best Practices + Pitfalls）
│
├── standards/      44 × .md           # 标准规范（命名/资产模型/量化/质量等）
├── evaluations/    27 × .md           # 评估清单（回归/评分卡/错误模式等）
├── templates/      26 × .template.md  # 交付物模板（含 5 个资产模板）
├── workflows/       2 × .pipeline.md   # Pipeline 编排（主交付 + 故障响应）
├── contexts/        4 × .md           # 上下文与交接模板
└── scripts/         3+ × .py          # 合规检查与修补脚本
```

## 交付阶段

| 阶段 | Stage ID | 核心场景 | 质量门禁 | 辅助场景 |
|------|----------|---------|---------|---------|
| 需求分析 | `analyze-requirement` | 需求分析 | Q-001: REQ-COVER ≥95% | plan-sprint |
| 系统设计 | `design-system` | 系统设计 | Q-002: 评审 100% 通过 | design-architecture, design-database, review-design |
| 任务拆分 | `decompose-task` | 任务拆分 | Q-003: TASK-COVER ≥98% | — |
| 开发实现 | `implement-feature` | 功能开发 | Q-004: DEV-COVERAGE ≥80% | integrate-api, manage-dependencies, manage-config, manage-secrets, document-project, manage-tech-debt |
| 测试验证 | `verify-test` | 测试验证 | Q-005: TEST-PASS ≥90% | automate-test, performance-testing, review-code |
| 部署发布 | `deploy-release` | 部署发布 | Q-006: DEPLOY-SUCCESS ≥99% | setup-infra, implement-cicd, prepare-release, plan-rollback |
| 监控运维 | `monitor-operate` | 监控运维 | Q-007: MON-SLO ≥99.5% | backup-data, migrate-data, migrate-environment, integrate-monitor, manage-change, optimize-performance, plan-capacity |
| 治理（全阶段） | — | 安全/故障/灾备/复盘 | — | audit-security, respond-incident, apply-hotfix, review-incident, plan-disaster-recovery, manage-knowledge |

## 快速开始

```bash
# 1. 全量合规自检
python3 scripts/harness-compliance-check.py

# 2. 阅读 Agent 执行协议
cat AGENTS.md

# 3. 选择场景（以需求分析为例）
cat scenarios/analyze-requirement/SCENARIO.md   # 场景入口
cat agents/analyze-requirement.agent.md          # 角色定义
cat prompts/analyze-requirement.prompt.md        # 执行脚本

# 4. 按 CoT 逐步执行，每步 VALIDATE，完成后 Handover
```

详细使用方法见 [USAGE.zh.md](./USAGE.zh.md)，深度分析见 [资产库全面评估深度分析报告.md](资产库全面评估深度分析报告.md)。

## License

MIT
