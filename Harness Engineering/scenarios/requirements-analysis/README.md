# 需求分析场景 / Requirements Analysis Scenario

> **阶段**: P1 — 需求分析
> **核心 Agent**: `agents/product-analyst`
> **目标输出**: 结构化 RFC（用户故事、验收标准、需求条目、冲突分析）
> **效力等级**: P0（强制）

---

## 场景概述

本场景负责将原始需求（PRD、会议纪要、用户访谈）转化为结构化的产品定义文档（RFC），为后续技术架构设计提供清晰、无歧义的需求基线。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `raw_requirements` | `string` | 是 | 原始需求文本 |
| `source_type` | `string` | 是 | 来源类型：`prd` / `meeting_notes` / `user_interview` |
| `project_context` | `string` | 是 | 项目背景、目标用户、技术约束 |
| `focus_areas` | `string` | 否 | 分析重点（如 `compliance`, `performance`, `ux`） |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "rfc_title": "RFC 标题",
  "version": "1.0.0",
  "user_stories": [
    {
      "id": "US-001",
      "story": "As a [角色], I want [需求], so that [价值]",
      "acceptance_criteria": ["Given... When... Then..."],
      "priority": "must_have | should_have | nice_to_have"
    }
  ],
  "requirements": [
    {
      "id": "REQ-001",
      "type": "functional | non_functional | compliance | constraint",
      "description": "...",
      "priority": "must_have | should_have | nice_to_have",
      "acceptance_criteria": ["..."],
      "source_reference": "原文段落或页码"
    }
  ],
  "conflicts": [
    {
      "req_ids": ["REQ-001", "REQ-003"],
      "description": "冲突描述",
      "suggested_resolution": "建议解决方案"
    }
  ],
  "open_questions": ["待澄清问题 1", "待澄清问题 2"]
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **Product Analyst** | 提取显性与隐性需求、编写验收标准、识别冲突与待澄清项 | 结构化 RFC JSON |
| **人类产品经理** | 审阅 `open_questions`，补充业务上下文，确认需求优先级 | 已确认的需求基线 |

---

## 质量检查要点

- [ ] 所有 `must_have` 需求均有明确的验收标准（Given-When-Then）
- [ ] `open_questions` 不为空时，必须触发人工澄清流程，禁止臆测补全
- [ ] 需求分类覆盖 functional / non_functional / compliance / constraint 四类
- [ ] 冲突分析至少覆盖需求间的资源竞争、逻辑矛盾、优先级冲突
- [ ] 输出通过 `evaluations/requirements-analysis-checkpoint.yaml` 质量门禁

---

## 下游衔接

本场景输出直接作为 `scenarios/tech-arch-design/` 的输入（`{{rfc_doc}}`）。
衔接规范详见 `standards/scenario-integration.md#P1→P2`。
