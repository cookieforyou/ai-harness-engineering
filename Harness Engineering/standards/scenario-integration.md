# 场景衔接规范 / Scenario Integration Specification

> **效力等级**: P0（强制）
> **适用范围**: 本资产库全部场景间的数据流转与版本兼容

---

## 1. 阶段衔接总览

```
P1(需求分析) ──→ P2(技术架构) ──→ P3(任务拆分) ──→ P4(开发实现) ──→ P5(部署迭代) ──→ P6(健康监控)
     ↑                                                                                      │
     └──────────────────────────────────── 反馈闭环 ────────────────────────────────────────┘
```

---

## 2. 数据契约矩阵

| 衔接路径 | 上游输出字段 | 下游输入变量 | Schema 版本 | 兼容策略 |
| :--- | :--- | :--- | :--- | :--- |
| **P1 → P2** | `rfc_doc` (JSON) | `{{rfc_doc}}` | `v1.0.0` | 严格匹配 |
| **P2 → P3** | `adr_doc` (JSON) | `{{adr_doc}}` | `v1.0.0` | 严格匹配 |
| **P3 → P4** | `epics[].stories[].tasks[]` | 代码审查范围上下文 | `v1.0.0` | 宽松匹配 |
| **P4 → P5** | 代码合并结果 + 审查报告 | `service_name`, `tech_stack`, `version` | `v1.0.0` | 宽松匹配 |
| **P5 → P6** | `deployment_spec.health_checks` + `deployment_spec.environment` | `service_name`, `tech_stack`, `slo` | `v1.0.0` | 严格匹配 |
| **P6 → P1** | `feedback-package` (JSON) | 需求分析输入补充 | `v1.0.0` | 扩展匹配 |

---

## 3. 衔接详细规范

### 3.1 P1 → P2：需求分析 → 技术架构

**上游输出** (`scenarios/requirements-analysis/`):
```json
{
  "rfc_title": "...",
  "version": "1.0.0",
  "user_stories": [...],
  "requirements": [
    { "id": "REQ-001", "type": "functional|non_functional|compliance|constraint", "description": "...", "priority": "...", "acceptance_criteria": [...] }
  ],
  "conflicts": [...],
  "open_questions": [...]
}
```

**下游输入映射** (`scenarios/tech-arch-design/`):
- `{{rfc_doc}}` ← 完整 RFC JSON
- `{{constraints}}` ← 从 `requirements[].type == "constraint"` 中提取
- `{{focus_areas}}` ← 从 `requirements[].type` 分布推导（如 compliance 多则 focus 为 security）

**兼容性要求**:
- P2 必须能解析 P1 输出的全部字段，允许忽略 `open_questions`（已在 P1 人工澄清阶段处理）
- 若 P1 的 `requirements` 为空数组，P2 必须拒绝执行并回退至 P1

---

### 3.2 P2 → P3：技术架构 → 任务拆分

**上游输出** (`scenarios/tech-arch-design/`):
```json
{
  "adr_title": "...",
  "version": "1.0.0",
  "tech_stack": { "database": {...}, "cache": {...}, ... },
  "architecture": { "layers": [...], "data_flow": "...", "diagram_mermaid": "..." },
  "api_contracts": [...],
  "non_functional_design": { "performance": "...", "availability": "...", "security": "...", "scalability": "..." },
  "adrs": [...],
  "risks": [...]
}
```

**下游输入映射** (`scenarios/task-decomposition/`):
- `{{adr_doc}}` ← 完整 ADR JSON
- `{{team_capacity}}` ← 外部输入，不与 ADR 直接关联但需参考 `tech_stack` 匹配角色
- `{{iteration_constraints}}` ← 外部输入，需参考 `risks` 调整里程碑缓冲

**兼容性要求**:
- P3 必须基于 `architecture.layers` 拆分 Epic，基于 `api_contracts` 拆分 Story
- 若 `tech_stack` 包含未在 `standards/skill-registry.yaml` 登记的技术，需标注为高风险

---

### 3.3 P3 → P4：任务拆分 → 开发实现

**上游输出** (`scenarios/task-decomposition/`):
```json
{
  "epics": [
    { "id": "E-001", "stories": [
      { "id": "S-001", "tasks": [
        { "id": "T-001", "title": "...", "assignee_role": "...", "risk_level": "..." }
      ]}
    ]}
  ],
  "critical_path": ["T-001", "T-003"],
  "risks": [...]
}
```

**下游输入映射** (`scenarios/code-review/`):
- 代码审查的 `focus_areas` 应参考 `critical_path` 上任务的 `risk_level`
- 审查范围应与 `epics[].stories[].tasks[].title` 描述的功能对应

**兼容性要求**:
- P4 不直接消费 P3 的 JSON Schema，但审查报告应标注关联的 Task ID（如 `T-001`）
- 若代码变更与任务描述严重不符，审查报告应标记为 `scope_mismatch`

---

### 3.4 P4 → P5：开发实现 → 部署迭代

**上游输出** (`scenarios/code-review/`):
```json
{
  "summary": "...",
  "severity_score": 1,
  "findings": [...],
  "action_required": false,
  "human_escalation_reason": null
}
```

**下游准入条件**:
- P5 仅在 P4 的 `action_required == false` 时方可启动
- 若 `severity_score >= 4`（即使 `action_required == false`），P5 应降级为 staging 环境部署，禁止直接生产部署

**下游输入映射** (`scenarios/deployment-pipeline/`):
- `{{service_name}}` ← 从代码仓库元数据或外部输入获取
- `{{tech_stack}}` ← 从 P2 ADR 的 `tech_stack` 获取
- `{{version}}` ← 从代码标签（git tag）获取

---

### 3.5 P5 → P6：部署迭代 → 健康监控

**上游输出** (`scenarios/deployment-pipeline/`):
```json
{
  "deployment_spec": {
    "service_name": "...",
    "environment": "...",
    "strategy": "...",
    "health_checks": { "readiness": "...", "liveness": "...", "startup": "..." },
    "compliance_notes": [...]
  }
}
```

**下游输入映射** (`scenarios/health-monitoring/`):
- `{{service_name}}` ← `deployment_spec.service_name`
- `{{tech_stack}}` ← 从 P2 ADR 的 `tech_stack` 传递（或外部输入）
- `{{slo}}` ← 从 P1 RFC 的 `non_functional` 需求推导，或外部输入
- `{{existing_monitoring}}` ← 外部输入

**兼容性要求**:
- P6 的 `health_checks` 必须与 P5 的 `deployment_spec.health_checks` 端点一致
- P6 的告警规则 `expr` 必须兼容 P5 部署的技术栈指标暴露方式

---

### 3.6 P6 → P1：健康监控 → 需求分析（反馈闭环）

**上游输出** (`scenarios/health-monitoring/`):
```json
{
  "feedback_package": {
    "feedback_id": "FB-001",
    "source_stage": "P6",
    "target_stage": "P1",
    "type": "performance|reliability|usability|security",
    "severity": "low|medium|high|critical",
    "description": "...",
    "evidence": { "metric_name": "...", "threshold": "...", "actual_value": "..." },
    "suggested_action": "..."
  }
}
```

**下游输入映射** (`scenarios/requirements-analysis/`):
- 反馈包作为 `{{project_context}}` 的补充材料输入
- 多条反馈应聚类后按优先级插入新 RFC 的 `requirements` 或 `open_questions`

**兼容性要求**:
- P1 必须能识别 `feedback_package.type` 并映射至正确的需求分类
- `performance` → `non_functional`
- `reliability` → `non_functional` 或 `compliance`
- `usability` → `functional`
- `security` → `compliance`

---

## 4. 版本兼容策略

### 4.1 向后兼容（Backward Compatible）

当下游场景升级但保持输入 Schema 不变时：
- 上游无需变更
- 下游在 `assets.lock` 中声明兼容的上游版本范围

### 4.2 不兼容变更（Breaking Change）

当上游输出 Schema 发生破坏性变更时：
1. 升级上游主版本号（如 `v1.0.0` → `v2.0.0`）
2. 同步更新下游输入映射逻辑
3. 在 `standards/scenario-integration.md` 中更新契约矩阵
4. 冻结旧版本流水线，直至所有下游完成迁移

### 4.3 兼容性矩阵

| 上游版本 | P2 兼容 | P3 兼容 | P4 兼容 | P5 兼容 | P6 兼容 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P1 v1.0.0 | ✅ | - | - | - | - |
| P2 v1.0.0 | - | ✅ | - | - | - |
| P3 v1.0.0 | - | - | ✅ | - | - |
| P4 v1.0.0 | - | - | - | ✅ | - |
| P5 v1.0.0 | - | - | - | - | ✅ |
| P6 v1.0.0 | ✅(反馈) | - | - | - | - |

---

## 5. 异常与回退

| 异常类型 | 触发条件 | 处理策略 |
| :--- | :--- | :--- |
| Schema 不匹配 | 上游输出字段缺失或类型错误 | 阻塞流转，触发 `schema-validator` 错误，回退至上游重试 |
| 版本冲突 | `assets.lock` 中依赖版本不一致 | 暂停执行，通知资产维护者确认升级路径 |
| 下游拒绝 | 下游准入条件不满足（如 P4 action_required=true） | 阻塞下游启动，回退至上游修复 |
| 反馈闭环阻塞 | P6 反馈包无法映射至 P1 需求分类 | 降级为 `open_questions`，由人工产品经理分类 |
