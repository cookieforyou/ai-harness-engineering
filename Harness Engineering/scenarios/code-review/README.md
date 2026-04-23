# 开发实现场景 / Code Review Scenario

> **阶段**: P4 — 开发实现
> **核心 Agent**: `agents/senior-engineer`
> **目标输出**: 结构化代码审查报告（问题发现、修复建议、安全扫描结果）
> **效力等级**: P0（强制）

---

## 场景概述

本场景负责对已提交的代码变更（Pull Request）进行自动化审查，识别安全、逻辑、性能、可维护性问题，生成结构化审查报告，并通过质量门禁决定代码是否可合并进入主分支。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `pr_id` | `string` | 是 | Pull Request 唯一标识 |
| `repo` | `string` | 是 | 代码仓库名 |
| `diff` | `string` | 是 | 统一 diff 格式的代码变更 |
| `context` | `string` | 否 | 项目技术栈与背景说明 |
| `focus_areas` | `string` | 否 | 审查重点（如 `security`, `performance`） |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "summary": "一句话总结",
  "severity_score": 1,
  "findings": [
    {
      "id": "F001",
      "severity": "critical|high|medium|low|info",
      "category": "security|logic|performance|maintainability",
      "file_path": "...",
      "line_range": "...",
      "message": "...",
      "suggestion": "..."
    }
  ],
  "action_required": true,
  "human_escalation_reason": null
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **Senior Engineer** | 代码逻辑审查、性能分析、可维护性评估、安全扫描复核 | 结构化审查报告 JSON |
| **人类技术负责人** | 审阅 Critical/High 级别问题、确认架构风险、批准合并 | 已批准的代码变更 |

---

## 质量检查要点

- [ ] 无 Critical 级别安全漏洞（如密钥泄露、注入、权限绕过）
- [ ] 每个 finding 的 `suggestion` 具体、可执行
- [ ] 审查覆盖安全、逻辑、性能、可维护性四个维度
- [ ] 若发现架构风险类问题，必须触发回退至 P2 流程
- [ ] 输出通过 `evaluations/code-review-checkpoint.yaml` 质量门禁

---

## 上游衔接

接收 `scenarios/task-decomposition/` 的输出作为审查范围上下文（任务清单用于确定代码变更是否与计划一致）。
衔接规范详见 `standards/scenario-integration.md#P3→P4`。

## 下游衔接

本场景通过结果决定是否能进入 `scenarios/deployment-pipeline/`：
- `action_required == false` 且 `severity_score < 4` → 允许进入 P5
- 否则 → 阻塞部署，需修复或人工审批
衔接规范详见 `standards/scenario-integration.md#P4→P5`。

---

## 流程概览

1. **Diff 解析** — 将统一 Diff 拆分为按文件组织的结构化数据
2. **安全扫描** — 并行执行密钥泄露检测与漏洞模式匹配
3. **深度审查** — 资深工程师 Agent 对代码逻辑、性能、可维护性进行综合评审
4. **报告合并** — 合并安全扫描与深度审查结果，去重并排序
5. **质量门禁** — 运行评估脚本，判断是否通过
6. **通知与归档** — 通过或人工升级

## 成功标准

- 安全漏洞检出率 >= 95%（基于 evaluations/code-review-dataset.jsonl）
- 误报率 <= 15%
- 平均响应延迟 <= 60s（单文件 <200 行）
- Critical 级别问题 100% 触发人工介入

## 依赖资产

- Agent: `agents/senior-engineer`
- Skills: `skills/diff-parser`, `skills/security-audit`, `skills/report-merger`
- Prompts: `prompts/code-review/v1.md`
- Instructions: `instructions/system/code-review-system.md`, `instructions/safety/*`
- Evaluations: `evaluations/code-review-checkpoint.yaml`

## 版本历史

| 版本 | 日期 | 变更 |
| :--- | :--- | :--- |
| 1.0.0 | 2026-04 | 初版，覆盖基础审查流程 |
