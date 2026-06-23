# E2E 交付全流程 AI Harness 使用指南

> **合规状态**：🟢 **95.3% A+**（`python3 scripts/harness-compliance-check.py` 验证）
> **主协议**：[AGENTS.md](./AGENTS.md)

## 目录

1. [资产概述](#资产概述)
2. [使用流程](#使用流程)
3. [场景选型](#场景选型)
4. [质量保障](#质量保障)
5. [最佳实践](#最佳实践)

---

## 资产概述

### 资产类型与职责

| 资产类型 | 用途 | 文件格式 | 加载顺序 |
|----------|------|----------|---------|
| Workflow | 流水线阶段顺序与准入准出 | `workflows/*.pipeline.md` | ① 首先 |
| Scenario | 场景入口：Purpose + CoT + 决策点 + 错误处理 + KPI | `scenarios/*/SCENARIO.md` | ② |
| Agent | 角色身份：工作规则 + I/O 契约 + 工具声明 + Handoff | `agents/*.agent.md` | ③ 同时 |
| Prompt | 执行脚本：变量 → 逐步 CoT → 输出验证 → Handover | `prompts/*.prompt.md` | ④ 执行主文档 |
| Instruction | 操作 Runbook：工具列表 + 环境要求 + 配置参数 | `instructions/*.instructions.md` | ⑤ 按需 |
| Skill | 领域知识包：方法论 + Best Practices + Common Pitfalls | `skills/*/SKILL.md` | ⑥ 按需 |
| Standard | 规范约束：命名/量化/质量/资产模型 | `standards/*.md` | ⑦ 准出前 |
| Evaluation | 评估清单：回归检查/评分卡/错误模式 | `evaluations/*.md` | ⑧ 阶段结束 |

### 资产规模

| 类别 | 数量 | 合规等级 |
|------|------|---------|
| Scenario | 37 | 100.0% A |
| Agent | 37 | 98.1% A |
| Prompt | 37 | 97.1% A |
| Instruction | 37 | 94.8% A |
| Skill | 37 | 100.0% A |
| Standard | 44 | 94.7% A |
| Evaluation | 27 | 100.0% A |
| Template | 26 | 92.9% A |
| **总计** | **282** | **95.3% A+** |

---

## 使用流程

### 步骤 1：确定交付阶段与流水线

查看 `workflows/e2e-delivery.pipeline.md` 确认当前处于哪条流水线、哪一阶段：

```
analyze-requirement → design-system → decompose-task
  → implement-feature → verify-test → deploy-release → monitor-operate
```

故障时切换到 `workflows/incident-response.pipeline.md`（检测分级→响应缓解→恢复闭环→复盘改进）。

### 步骤 2：加载场景入口

读取对应阶段的 `scenarios/{name}/SCENARIO.md`：

- **Purpose / Business Value**：为什么做，业务价值
- **Chain of Thought**：AI 必须遵循的逐步思维链（THINK→ANALYZE→DESIGN→IMPLEMENT→VERIFY→HANDOVER）
- **Decision Checkpoints**：DC-001 至 DC-006 决策点，含触发条件和选择标准
- **Error Handling**：P0-P4 错误场景，识别信号→处理流程→降级方案→升级条件
- **Quality Metrics**：KPI 加权评分公式 + 三级阈值（70=合格/85=优秀/95=卓越）

### 步骤 3：配置角色资产

读取 `agents/{name}.agent.md`：

1. **Role Definition**：角色定位与核心职责
2. **Use When / Not Applicable**：激活与排除条件
3. **Working Rules**：工作规则 + YAML 工作流步骤
4. **Expected Input / Output**：字段级验证规则表
5. **Handoff**：下游阶段的结构化 YAML 交接模板
6. **Quality Checklist**：执行前/中/后检查项

### 步骤 4：按 Prompt 逐步执行

读取 `prompts/{name}.prompt.md` 作为执行主文档：

1. **Input Variables**：确认所有 `Required: true` 的变量已填充
2. **Chain of Thought**：逐步执行，每步完成 `[VALIDATE]` 自检
3. **Error Handling**：异常时参考 Scenario 的错误处理流程
4. **Output Validation**：对照 V-001~V-004 验证输出质量
5. **Handover Preparation**：填写 YAML 交接包

### 步骤 5：引用 Skill 和 Instruction（按需）

- 需要领域专业知识时加载 `skills/{name}/SKILL.md`（Best Practices + Common Pitfalls）
- 需要具体操作细节时加载 `instructions/{name}.instructions.md`（工具+环境+配置参数）

### 步骤 6：质量评估与准出

1. 运行 `evaluations/output-validation-checklist.md` 通用验证
2. 运行 `evaluations/regression-checklist.md` 对应阶段章节
3. 排除 `evaluations/common-error-patterns.md` 中的已知反模式
4. 对照 `standards/id-generation-quantification.md` 确认 KPI 达标
5. 更新 `contexts/global-context.md`，执行 Handover

---

## 场景选型

### 按用户意图快速路由

| 用户说… | 首选场景 | 可选并行 |
|---------|----------|----------|
| 分析/澄清需求 | `analyze-requirement` | `plan-sprint` |
| 做架构/设计 | `design-system` | `design-architecture`, `design-database`, `review-design` |
| 拆任务/排期 | `decompose-task` | `plan-sprint` |
| 写代码/做功能 | `implement-feature` | `integrate-api`, `manage-dependencies`, `manage-tech-debt` |
| 测试 | `verify-test` | `automate-test`, `performance-testing` |
| 上线 | `deploy-release` | `prepare-release`, `plan-rollback`, `implement-cicd` |
| 线上问题 | `respond-incident` | `apply-hotfix`, `review-incident` |
| 安全/合规 | `audit-security` | `manage-secrets` |
| 性能优化 | `optimize-performance` | `plan-capacity` |
| 文档欠缺 | `document-project` | `manage-knowledge` |

### 决策树

```
是否有生产故障？
  是 → respond-incident → (需要代码?) apply-hotfix → review-incident
  否 → 项目处于哪一阶段？
        需求 → analyze-requirement
        设计 → design-system (+ 专项设计)
        开发 → implement-feature (+ manage-dependencies)
        测试 → verify-test
        发布 → deploy-release (+ plan-rollback)
        运维 → monitor-operate
```

---

## 质量保障

### 合规检查

```bash
# 全量合规检查（1974 项）
python3 scripts/harness-compliance-check.py

# 单类别检查
python3 scripts/harness-compliance-check.py --category agents
python3 scripts/harness-compliance-check.py --category standards

# 单文件检查
python3 scripts/harness-compliance-check.py --file agents/deploy-release.agent.md
```

### 质量门禁（Pipeline 级）

| 过渡 | 门禁 | 标准 |
|------|------|------|
| 需求 → 设计 | Q-001 | REQ-COVER ≥ 95% |
| 设计 → 任务 | Q-002 | 设计评审 100% 通过 |
| 任务 → 开发 | Q-003 | TASK-COVER ≥ 98% |
| 开发 → 测试 | Q-004 | DEV-COVERAGE ≥ 80% |
| 测试 → 部署 | Q-005 | TEST-PASS ≥ 90% |
| 部署 → 运维 | Q-006 | DEPLOY-SUCCESS ≥ 99% |
| 运维稳态 | Q-007 | MON-SLO ≥ 99.5% |

### 评分体系

使用 A-F 评级（与 [evaluations/scorecard-template.md](./evaluations/scorecard-template.md) 对齐）：

| 分数 | 等级 | 含义 |
|------|------|------|
| 90-100 | A (优秀) | 超出预期 |
| 80-89 | B (良好) | 符合预期，小幅改进 |
| 70-79 | C (合格) | 满足基本要求（最低准出线） |
| 60-69 | D (需改进) | 存在明显不足 |
| 0-59 | F (不合格) | 不满足基本要求，不准出 |

---

## 最佳实践

### 1. R1-R5 五条不可违反的规则

| # | 规则 | 违反后果 |
|---|------|----------|
| R1 | 先 Scenario 后 Prompt | 跳过质量门禁与错误处理 |
| R2 | 变量未填不执行 | 产出不可追溯、无法交接 |
| R3 | 每步 VALIDATE 自检 | 幻觉需求/设计漂移 |
| R4 | 准出前量化（对照 KPI） | 无法进入下一阶段 |
| R5 | 必须 Handover（YAML 交接） | 下游 Agent 上下文断裂 |

### 2. 渐进式使用

从核心 7 场景开始（analyze-requirement → design-system → decompose-task → implement-feature → verify-test → deploy-release → monitor-operate），逐步引入扩展场景。

### 3. 上下文传递

每个阶段输出必须作为下一阶段输入——通过 `contexts/unified-handover-template.md` 的 YAML Handoff 模板确保信息连贯。

### 4. 迭代优化

运行 `python3 scripts/harness-compliance-check.py` 定期审计，根据 WARN 项持续优化资产质量。

### 5. 团队协作

多 Agent 协同时遵循 Handoff YAML 契约，明确 `from_stage`/`to_stage` 路由和 `artifacts` 交付物清单。

---

## 常见问题

### Q: 如何选择合适的场景？
A: 参考 [场景选型](#场景选型) 的决策树和路由表，或查看 [AGENTS.md 场景全目录](./AGENTS.md#场景全目录37)。

### Q: 如何确保输出质量？
A: 每个 Prompt 包含 Output Validation（V-001~V-004），对照 `evaluations/` 评估清单逐项验证，不通过则回退修正。

### Q: 如何贡献新资产？
A: 参考 `standards/authoring-checklist.md` 和 [AGENTS.md 资产维护章节](./AGENTS.md#资产维护与扩展)，从 `templates/` 复制模板创建，通过合规检查后提交。

### Q: 资产库合规状态如何查看？
A: 运行 `python3 scripts/harness-compliance-check.py` 查看实时合规报告，或阅读 [深度分析报告](./资产库全面评估深度分析报告.md)。

---

## 相关文档

| 文档 | 用途 |
|------|------|
| [AGENTS.md](./AGENTS.md) | Agent 导航图与执行协议 |
| [INTRODUCTION.zh.md](./INTRODUCTION.zh.md) | 项目介绍 |
| [资产库全面评估深度分析报告.md](./资产库全面评估深度分析报告.md) | 全库深度评估（v3.0） |
| [standards/harness-engineering.md](./standards/harness-engineering.md) | 六层驾驭模型对齐标准 |
| [workflows/e2e-delivery.pipeline.md](./workflows/e2e-delivery.pipeline.md) | 主交付流水线 |
| [copilot-instructions.md](./copilot-instructions.md) | Copilot/IDE 集成指引 |
