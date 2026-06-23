---
name: harness-engineering
description: "Harness Engineering 六层驾驭模型（Goal/Strategy/Tooling/Constraint/Feedback/Observability）在企业交付资产库中的映射与对齐标准"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'harness-engineering', 'six-layer-model', 'alignment', 'governance']
---

# Harness Engineering 规范 — E2E Delivery Harness 对齐标准

> 本规范将 [Harness Engineering（驾驭工程）](../../../Harness%20Engineering（驾驭工程）专业介绍.md) 六层模型映射到本资产库的五类执行资产，作为**审查与优化的唯一基准**。

## 核心理念

> **Humans steer, Agents execute.**（人类掌舵，智能体执行）

Harness 不是更长 Prompt，而是 **Model + Harness**：用结构化资产提供目标、策略、工具边界、约束、反馈与可观测性。

## 六层模型 → 资产映射

| Harness 层 | 职责 | 本库承载资产 | 必填内容 |
|------------|------|--------------|----------|
| **1. Goal（目标）** | KPI、成功标准、业务价值 | Scenario `Purpose`、Prompt `Task Description`、Agent `Expected Output` | 可量化 KPI（MET-* / KPI-*） |
| **2. Strategy（策略）** | Plan → Act → Reflect | Scenario/Prompt `Chain of Thought`、`Decision Checkpoints` (DC-*) | 逐步 [VALIDATE]，禁止跳步 |
| **3. Tooling（工具）** | 可调用的能力边界 | Agent `tools`、Instruction 操作步骤 | YAML `tools: []` 非空 |
| **4. Constraint（约束）** | 安全、合规、范围 | Prompt `Constraints`、Scenario 升级条件 | 升级人工的明确阈值 |
| **5. Feedback（反馈）** | 质量自检与重试 | Prompt `Output Validation`、Evaluation 清单 | V-* 验证项 + 不合格协议 |
| **6. Observability（可观测）** | 轨迹、交接、审计 | Handover YAML、`error_log`、Global Context | HO-* handover_id、ERR-* 日志 |

## 五类资产合规清单（单场景 `{base}`）

### Scenario (`scenarios/{base}/SCENARIO.md`)

- [ ] YAML：`name`, `type: scenario`, `version`, `status`
- [ ] `Purpose` + Business Value
- [ ] `Chain of Thought`（Think-Aloud）
- [ ] `Decision Checkpoints`（≥3 个 DC-*）
- [ ] `Error Handling`（≥2 个场景，含升级条件）
- [ ] `Quality Metrics`（KPI 表 + 合格线 ≥70）
- [ ] `Handover Criteria` + handover YAML 片段
- [ ] `Related Assets` 五类链接有效

### Agent (`agents/{base}.agent.md`)

- [ ] YAML：`tools` 数组（必填）
- [ ] `harness_layers` 标注（goal/strategy/tooling/constraint/feedback/observability）
- [ ] `Use When` / `Not Applicable`
- [ ] `Working Rules` + `Expected Input/Output` 表
- [ ] `Handoff` YAML

### Prompt (`prompts/{base}.prompt.md`)

- [ ] YAML：`type: prompt`（统一，不用 execution）
- [ ] `Input Variables` 表（Required 列）
- [ ] `Chain of Thought`
- [ ] `Error Handling`（ERR-* 分级）
- [ ] `Output Validation`（V-001～V-004 + Failure Protocol）
- [ ] `Handover Preparation`（对齐 [unified-handover-template.md](../contexts/unified-handover-template.md)）
- [ ] `Output Format` 模板

### Instruction (`instructions/{base}.instructions.md`)

- [ ] YAML：`applyTo`, `phase`
- [ ] 分步操作 + 检查清单
- [ ] 引用 `standards/` 与 `evaluations/`

### Skill (`skills/{base}/SKILL.md`)

- [ ] YAML：`category`, `status`
- [ ] 反模式（Anti-patterns）
- [ ] 引用标准仅指向 `standards/` 已存在文件

## 阶段准出（与 Pipeline 对齐）

见 [id-generation-quantification.md](id-generation-quantification.md) 与 [workflows/e2e-delivery.pipeline.md](../workflows/e2e-delivery.pipeline.md) Quality Gates。

## 审查命令（维护者）

```bash
# 一键全量合规（推荐）
python3 scripts/harness-full-compliance.py

# Prompt 缺 Output Validation
for f in prompts/*.prompt.md; do grep -q "## Output Validation" "$f" || echo "$f"; done

# Scenario 缺 Error Handling
for f in scenarios/*/SCENARIO.md; do grep -q "## Error Handling" "$f" || echo "$f"; done

# Agent 缺 tools
for f in agents/*.agent.md; do grep -q "^tools:" "$f" || echo "$f"; done

# Scenario 缺 Handover Criteria
for f in scenarios/*/SCENARIO.md; do grep -q "## Handover Criteria" "$f" || echo "$f"; done

# Scenario DC-* 不足 3 个
for f in scenarios/*/SCENARIO.md; do
  c=$(grep -oE 'DC-[0-9]{3}' "$f" | sort -u | wc -l | tr -d ' ')
  [ "$c" -lt 3 ] && echo "$f: $c DC"
done
```

## 质量指标

六层模型对齐度通过以下可量化指标衡量：

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| Goal 对齐度 | ≥95% | Scenario.Purpose 包含可量化 KPI 的占比 |
| Strategy 对齐度 | ≥90% | Agent.Working Rules 引用 Scenario.DC 的完整性 |
| Tooling 对齐度 | ≥85% | Agent.tools 声明覆盖率（声明/实际使用） |
| Constraint 对齐度 | ≥90% | Error Handling 覆盖 P0-P4 的完整性 |
| Feedback 对齐度 | ≥80% | Handoff YAML 双向引用完整性 |
| Observability 对齐度 | ≥85% | 输出格式 Schema 定义率 |

总体对齐度 = Σ(各层得分 × 层权重) / Σ权重，目标 ≥88%。

## 相关资产

- [asset-model.md](asset-model.md) — 资产类型与组合公式
- [lifecycle.md](lifecycle.md) — 资产生命周期管理
- [output-quality-rubric.md](output-quality-rubric.md) — 输出质量评分标准
- [version-compatibility-matrix.md](version-compatibility-matrix.md) — 版本兼容性矩阵

## 版本

- **2.0.0** — 添加 YAML frontmatter；增加质量指标与量化公式；补全交叉引用
- **1.1.0** — 对齐六层模型与合规清单；新增 `harness-full-compliance.py` 审查项
