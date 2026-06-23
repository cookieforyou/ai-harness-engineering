---
name: cot-framework
description: "规范的思维链 (Chain of Thought) 执行框架，定义 AI Agent 逐步推理的通用步骤标签和验证协议"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'cot', 'execution-protocol']
---

# Chain of Thought 执行框架

## 概述

本文件定义了 E2E Delivery Harness 中所有场景的 **通用思维链 (Chain of Thought) 执行框架**。各场景的 Scenario 和 Prompt 文件应**引用本框架**，然后在其基础上添加领域特定的推理步骤，而非逐字复制通用步骤。

## 通用步骤标签 (Step Tags)

所有 CoT 步骤必须使用以下标准化标签，确保 AI Agent 行为一致且可审计：

| 标签 | 含义 | 强制动作 | 典型输入 | 典型输出 |
|------|------|---------|---------|---------|
| `[THINK]` | 理解和分析任务上下文 | 阐述对任务目标、约束、边界的理解 | 用户输入、上下文变量 | 任务分析摘要 |
| `[ANALYZE]` | 深度分析需求和约束 | 识别关键决策点、风险、依赖关系 | 任务分析摘要 | 分析报告（含风险清单） |
| `[GATHER]` | 收集必要信息和数据 | 搜索代码库、读取文档、查询外部系统 | 分析报告 | 收集到的信息汇总 |
| `[DESIGN]` | 设计解决方案 | 生成方案、评估备选、权衡利弊 | 分析报告 + 收集的信息 | 设计方案（含备选方案对比） |
| `[IMPLEMENT]` | 执行和实施 | 编写代码、执行命令、创建交付物 | 设计方案 | 实施成果 |
| `[VERIFY]` | 验证结果和质量 | 对照需求检查、运行测试、质量评分 | 实施成果 | 验证报告 |
| `[HANDOVER]` | 准备阶段交接 | 生成 Handover Context、更新 Global Context | 验证通过的交付物 | Handover YAML + 更新的上下文 |

## 每步强制协议

每个 CoT 步骤必须包含以下四个子项：

```
Step N: [TAG] 步骤描述
   ├─ 输入: <上一步的输出 + 相关变量>
   ├─ 思考: <推理过程：关键问题？可选方案？>
   ├─ 验证: <自检：是否正确？是否完整？是否符合约束？>
   └─ 输出: <本步骤的产出物>
```

### 验证失败处理

当 `[VALIDATE]` 步骤自检不通过时：

```yaml
validation_failure_protocol:
  step_1_self_check: "检查当前步骤输出是否满足验证条件"
  step_2_retry: "IF 小问题 THEN 修正后重新验证 (最多 2 次)"
  step_3_rollback: "IF 无法修正 THEN 回退到上一正确步骤"
  step_4_escalate: "IF 回退后仍失败 THEN 升级到人工决策"
  max_retries_per_step: 2
  max_total_retries: 5
```

## 领域特定步骤扩展

场景可以在通用步骤之外添加领域特定标签。常见扩展标签：

| 扩展标签 | 适用阶段 | 含义 |
|---------|---------|------|
| `[MODEL]` | Design | 数据建模或架构建模 |
| `[SPECIFY]` | Design/Dev | 编写详细规格说明 |
| `[ASSESS]` | Governance | 风险评估或影响分析 |
| `[LOCATE]` | Governance | 问题定位和根因分析 |
| `[DEPLOY]` | Deployment | 执行部署操作 |
| `[WATCH]` | Operations | 持续监控观察 |
| `[RESPOND]` | Operations | 响应告警或事件 |
| `[IMPROVE]` | Operations | 提出改进措施 |
| `[REPORT]` | Governance | 生成报告和总结 |

## 场景 CoT 引用方式

各场景的 SCENARIO.md 和 Prompt 文件应按如下方式引用：

```markdown
## Chain of Thought (思维链)

> **基础框架**: 遵循 [CoT 执行框架](../../standards/cot-framework.md) 的通用步骤协议。
> 每步包含 输入→思考→验证→输出 四个子项，验证失败时回退修正。

### 领域特定 Think-Aloud Protocol

[THINK] Step 1: 理解{领域}任务目标和约束
   ...
```

## 与决策点的关系

CoT 中的特定步骤会触发决策检查点 (DC-*)：

```
[ANALYZE] → 触发 DC-001 (范围/优先级决策)
[DESIGN]  → 触发 DC-002 (方案选择决策)
[VERIFY]  → 触发 DC-003 (质量门禁决策)
```

## 反模式 (Anti-patterns)

| 反模式 | 表现 | 正确做法 |
|--------|------|---------|
| 跳步推理 | 直接从输入到输出，跳过分析 | 严格按步骤顺序执行，不允许跳过 |
| 汇总幻觉 | 多步骤合并为一个笼统结论 | 每步独立输出，步骤间有明确的输入/输出 |
| 验证缺失 | `[VERIFY]` 步骤无实质检查 | 每步结束后对照检查清单验证 |
| 重试无限 | 验证失败后不断重试 | 最多重试 2 次，之后升级 |
| 标签混用 | 领域标签和通用标签含义不清 | 扩展标签必须在 Scenario 开头声明定义 |

## 相关资产

- [AGENTS.md](../AGENTS.md) - 执行协议和质量契约
- [error-classification.md](error-classification.md) - 错误分类体系
- [id-generation-quantification.md](id-generation-quantification.md) - KPI 和量化门禁
