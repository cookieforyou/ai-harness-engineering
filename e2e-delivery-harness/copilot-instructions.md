# Copilot Instructions for E2E Delivery Harness

> **合规状态**：全库 282 资产 **95.3% A+**，8/8 类别 A 级，零 B/C/D/F 资产
> **主协议**：[AGENTS.md](AGENTS.md)
> **合规基准**：[standards/harness-engineering.md](standards/harness-engineering.md)（Harness 六层模型）
> **深度分析**：[资产库全面评估深度分析报告.md](资产库全面评估深度分析报告.md)

## General Guidelines

### 1. Asset Discovery

When asked to assist with delivery tasks:

1. Read [AGENTS.md](AGENTS.md) execution protocol (R1–R5：先 Scenario 后 Prompt、变量未填不执行、每步 VALIDATE、准出前量化、必须 Handover)
2. Identify pipeline stage via `workflows/*.pipeline.md`
3. Load assets in strict order:
   - `scenarios/{base}/SCENARIO.md` — Purpose / CoT / DC-* 决策点 / Error Handling / KPI
   - `agents/{base}.agent.md` — 确认 YAML `tools` 数组和 `harness_layers` 声明
   - `prompts/{base}.prompt.md` — Input Variables → CoT → Error Handling → Output Validation → Handover
   - `instructions/{base}.instructions.md` — 操作 Runbook（含领域特定工具、环境要求、配置参数）
   - `skills/{base}/SKILL.md` — 领域知识包（含 Best Practices + Common Pitfalls）

### 2. Role Activation

When activating a specific role:
```
1. Read the .agent.md file: Role Definition + Use When / Not Applicable + Working Rules
2. Review Expected Input / Output table (field-level validation rules)
3. Load Handoff YAML contract for downstream stage
4. Check Quality Checklist (Pre/During/Post execution)
5. Reference associated skills and instructions as needed
```

### 3. Output Quality

Ensure all outputs meet the standards defined in:

- `standards/harness-engineering.md` — 六层模型合规（Goal/Strategy/Tooling/Constraint/Feedback/Observability）
- `standards/naming-conventions.md` — `{verb}-{noun}` 命名与 ID 前缀体系
- `standards/output-quality-rubric.md` — 输出质量评分标准
- `standards/id-generation-quantification.md` — 28 个 MET-* 指标与 7 个 Q-* 质量门禁
- `evaluations/output-validation-checklist.md` — V-001~V-004 通用验证 + Failure Protocol
- `evaluations/regression-checklist.md` — 7 阶段回归检查（155 个检查项）
- `evaluations/common-error-patterns.md` — 10 类常见错误模式（检测+修复+预防）

### 4. Compliance Check

每次执行完成后运行合规自检：
```bash
python3 scripts/harness-compliance-check.py
```
全量 1974 项自动检查，覆盖 YAML frontmatter / 内容深度 / 量化指标 / 交叉引用 / 占位符检测 / Evaluation 检查项。

## Phase-Specific Instructions

### Requirement Analysis (需求分析)
- **Core Scenario**: `analyze-requirement` — 需求规格评审，REQ-COVER ≥95%
- **Extended**: `plan-sprint` — Sprint 规划，容量缓冲 20-30%
- Load `skills/analyze-requirement/SKILL.md` for INVEST 原则和需求优先级矩阵
- Output: 需求规格说明书 + 干系人分析 + 用例 + 追溯矩阵

### System Design (系统设计)
- **Core Scenario**: `design-system` — 架构评审通过，设计可追溯需求
- **Extended**: `design-architecture`（架构模式 ADR）、`design-database`（ER/Schema/迁移策略）、`review-design`（ATAM/SAAM 评审）
- Load `skills/design-database/SKILL.md` for 1NF/2NF/3NF 正式定义和索引对比表
- Output: 架构说明 + 组件定义 + API 概要 + ADR

### Task Decomposition (任务拆分)
- **Core Scenario**: `decompose-task` — TASK-COVER ≥98%
- Load `skills/plan-sprint/SKILL.md` for Planning Poker/T-shirt sizing/亲和估算
- Output: Backlog + 估算 + 依赖图 + 迭代计划

### Development (开发实现)
- **Core Scenario**: `implement-feature` — DEV-COVERAGE ≥80%，CR 通过
- **Extended**: `integrate-api`（API 集成/契约测试）、`manage-dependencies`（依赖冲突/升级策略）、`manage-config`（多环境配置分层）、`manage-secrets`（密钥轮换/AES-256 加密）、`document-project`（Diátaxis/Arc42 文档框架）
- **Auxiliary** (declared in Pipeline): `manage-dependencies`, `manage-tech-debt`
- Load `skills/implement-feature/SKILL.md` for coding patterns and anti-patterns
- Output: 源代码 + 单测 + 技术说明

### Testing (测试验证)
- **Core Scenario**: `verify-test` — TEST-PASS ≥90%
- **Extended**: `automate-test`（pytest/Jest/Selenium/k6）、`performance-testing`（USE/RED/四大黄金信号）、`review-code`（SonarQube/ESLint/ArchUnit）
- Use `evaluations/regression-checklist.md` testing phase section
- Output: 测试报告 + 缺陷列表 + 覆盖率报告

### Deployment (部署发布)
- **Core Scenario**: `deploy-release` — DEPLOY-SUCCESS ≥99%
- **Extended**: `setup-infra`（Terraform/Ansible）、`implement-cicd`（GitHub Actions/ArgoCD）、`prepare-release`（发布检查清单）、`plan-rollback`（5 种回滚策略）
- **Auxiliary**: `plan-rollback`
- Output: 部署记录 + 发布报告 + 回滚预案

### Monitoring & Operations (监控运维)
- **Core Scenario**: `monitor-operate` — MON-SLO ≥99.5%
- **Extended**: `backup-data`（3-2-1 原则/恢复演练）、`migrate-data`（数据一致性双校验）、`migrate-environment`（蓝绿/金丝雀/滚动）、`integrate-monitor`（Prometheus+Grafana+OpenTelemetry）、`manage-change`（变更审批）、`optimize-performance`（USE/RED/火焰图）、`plan-capacity`（Little's Law/排队论）
- Output: 监控仪表板 + 告警规则 + Runbook + SLO 追踪

### Governance (治理)
- **Extended**: `audit-security`（OWASP ZAP/Trivy/Snyk）、`manage-tech-debt`（债务清单/偿还计划）、`manage-knowledge`（复盘/Wiki）、`respond-incident`（P0≤5min 响应）、`review-incident`（Postmortem/改进项）、`plan-disaster-recovery`（RPO≤15min/RTO≤30min）、`apply-hotfix`（紧急修复 6 步工作流）
- Load `skills/apply-hotfix/SKILL.md` for 6 common pitfalls with risk/prevention/impact
- Output: 审计报告 + 事件时间线 + DR 方案 + Postmortem

## Quality Gates

| 过渡 | 门禁 ID | 标准 |
|------|---------|------|
| 需求 → 设计 | Q-001 | REQ-COVER ≥ 95% |
| 设计 → 任务 | Q-002 | 设计评审 100% 通过 |
| 任务 → 开发 | Q-003 | TASK-COVER ≥ 98% |
| 开发 → 测试 | Q-004 | DEV-COVERAGE ≥ 80% |
| 测试 → 部署 | Q-005 | TEST-PASS ≥ 90% |
| 部署 → 运维 | Q-006 | DEPLOY-SUCCESS ≥ 99% |
| 运维稳态 | Q-007 | MON-SLO ≥ 99.5% |

## Handoff Protocol

When transitioning between phases:

1. 填充 `contexts/unified-handover-template.md` 的 YAML Handoff 模板
2. 确保 `to_stage` 正确路由到下游阶段
3. 更新 `contexts/global-context.md` 中的 `project.stage`、`updated_at`、最近 `handover_id`
4. Summarize completed work, list pending items, flag potential risks
5. 验证 Handoff YAML 所有必填字段（header/artifacts/decisions/open_issues/risks/quality_metrics）

## Key Reference Files

| 文件 | 用途 |
|------|------|
| [AGENTS.md](AGENTS.md) | Agent 导航图与执行协议（R1-R5） |
| [资产库全面评估深度分析报告.md](资产库全面评估深度分析报告.md) | 全库深度评估（v3.0） |
| [standards/harness-engineering.md](standards/harness-engineering.md) | 六层驾驭模型对齐标准 |
| [standards/id-generation-quantification.md](standards/id-generation-quantification.md) | ID 体系与 28 个 MET-* KPI |
| [standards/naming-conventions.md](standards/naming-conventions.md) | `{verb}-{noun}` 命名规范 |
| [evaluations/regression-checklist.md](evaluations/regression-checklist.md) | 7 阶段 155 项回归检查 |
| [evaluations/common-error-patterns.md](evaluations/common-error-patterns.md) | 10 类反模式库 |
| [workflows/e2e-delivery.pipeline.md](workflows/e2e-delivery.pipeline.md) | 主交付流水线 |
| [workflows/incident-response.pipeline.md](workflows/incident-response.pipeline.md) | 故障响应流水线 |
