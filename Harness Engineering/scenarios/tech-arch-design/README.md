# 技术架构设计场景 / Technical Architecture Design Scenario

> **阶段**: P2 — 技术架构
> **核心 Agent**: `agents/solution-architect`
> **目标输出**: 架构决策记录 ADR（技术选型、系统架构、接口契约、非功能性设计）
> **效力等级**: P0（强制）

---

## 场景概述

本场景基于 P1 阶段输出的结构化 RFC，设计完整的技术架构方案。输出物为架构决策记录（ADR），包含技术选型、分层架构、接口契约、非功能性设计及风险清单，为后续任务拆分提供可执行的技术基线。

---

## 输入规范

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :--- | :--- |
| `rfc_doc` | `object` | 是 | P1 阶段输出的结构化 RFC JSON |
| `constraints` | `string` | 是 | 约束条件（预算、团队技能、合规、性能 SLO） |
| `existing_system` | `string` | 否 | 现有系统描述（如有技术债或存量服务） |
| `focus_areas` | `string` | 否 | 设计重点（如 `scalability`, `security`, `cost-efficiency`） |

---

## 输出规范

主输出为 JSON 格式，Schema 定义如下：

```json
{
  "adr_title": "架构决策记录标题",
  "version": "1.0.0",
  "tech_stack": {
    "database": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" },
    "cache": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" },
    "message_queue": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" },
    "framework": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" },
    "deployment": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" },
    "observability": { "primary": "...", "rationale": "...", "risk_level": "low|medium|high" }
  },
  "architecture": {
    "description": "架构概述",
    "layers": [
      { "name": "...", "components": ["..."], "responsibilities": "..." }
    ],
    "data_flow": "Mermaid 语法的文本描述",
    "diagram_mermaid": "graph TD; A[客户端] --> B[API Gateway]; ..."
  },
  "api_contracts": [
    {
      "name": "...",
      "method": "GET|POST|PUT|DELETE",
      "path": "/api/v1/...",
      "request_schema": { },
      "response_schema": { }
    }
  ],
  "non_functional_design": {
    "performance": "...",
    "availability": "...",
    "security": "...",
    "scalability": "..."
  },
  "adrs": [
    {
      "id": "ADR-001",
      "title": "...",
      "context": "...",
      "decision": "...",
      "consequences": "..."
    }
  ],
  "risks": [
    { "description": "...", "mitigation": "...", "severity": "low|medium|high" }
  ]
}
```

---

## 角色职责

| 角色 | 职责 | 输出物 |
| :--- | :--- | :--- |
| **Solution Architect** | 技术选型、架构设计、接口契约定义、ADR 撰写 | 架构决策记录 ADR JSON |
| **人类技术负责人** | 审阅技术选型合理性、确认架构风险接受度、批准关键 ADR | 已批准的架构方案 |

---

## 质量检查要点

- [ ] 每个技术维度均有 Primary 推荐及选型理由，风险等级标注清晰
- [ ] 接口契约包含核心 API 的请求/响应 Schema 及错误码定义
- [ ] ADR 数量 >= 3，覆盖关键技术决策及其权衡分析
- [ ] 风险清单包含至少一个技术风险与一个团队能力风险
- [ ] 若存在存量系统，架构设计明确迁移路径与兼容性策略
- [ ] 输出通过 `evaluations/tech-arch-checkpoint.yaml` 质量门禁

---

## 上游衔接

接收 `scenarios/requirements-analysis/` 的输出（`{{rfc_doc}}`）。
衔接规范详见 `standards/scenario-integration.md#P1→P2`。

## 下游衔接

本场景输出直接作为 `scenarios/task-decomposition/` 的输入（`{{adr_doc}}`）。
衔接规范详见 `standards/scenario-integration.md#P2→P3`。
