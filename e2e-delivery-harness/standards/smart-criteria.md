---
name: smart-criteria
description: "SMART 目标标准，定义 Specific/Measurable/Achievable/Relevant/Time-bound 五项原则及其在 OKR/KPI 体系中的映射，含反模式和合规检查"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'smart', 'goal', 'okr', 'kpi', 'requirements']
---

# SMART 目标标准

## Overview

**Purpose**: SMART 是一套用于定义清晰、可执行目标的框架，确保每个目标、关键结果或需求验收标准经过结构化思考，消除模糊性和不可衡量性。五项原则——Specific（具体）、Measurable（可衡量）、Achievable（可达成）、Relevant（相关）、Time-bound（有时限）——共同构成目标质量的检查基线。

**Scope**: 适用于本组织所有项目目标、OKR、KPI 及其对应的需求验收标准。通过 Harness Goal 层创建的目标和 REQ-* 需求均须符合 SMART 标准。

**Origin**: 源于 Peter Drucker 的目标管理（MBO）理论，后经 George T. Doran 系统化为 SMART 缩写法。

---

## SMART 核心定义

| 字母 | 英文 | 中文 | 检查问题 |
|------|------|------|----------|
| S | Specific | 具体 | 是否明确「谁、做什么、在哪」？ |
| M | Measurable | 可衡量 | 是否有数字、比例或可追溯指标？ |
| A | Achievable | 可达成 | 在约束内是否现实？ |
| R | Relevant | 相关 | 是否支撑业务目标 OBJ-*？ |
| T | Time-bound | 有时限 | 是否有截止日期或迭代？ |

---

## S — Specific (具体)

**定义**: 目标必须清晰无歧义，回答 Who（谁）？What（做什么）？Where（范围/模块）？When（何时）？Why（为什么）？

**正例**: "将结账页面的加载时间从 3 秒降至 1 秒以内"
**反例**: "提升网站性能"

**OKR 映射**: Key Result 的描述须明确作用对象和维度，如"降低购物车模块的接口 P95 延迟"。

**检查**: 目标对象是否明确？操作动词是否可执行？是否指定了范围边界？

---

## M — Measurable (可衡量)

**定义**: 目标必须附带可量化指标以追踪进度和完成状态。没有数字的目标无法判断是否达成。

**正例**: "将 NPS（净推荐值）从 42 提升至 55"
**反例**: "提升客户满意度"

**KPI 映射**: 每个 SMART 目标关联且仅关联一个主 KPI，避免多头指标导致责任不清。

**测量数据源**: 产品分析平台（GA、Amplitude）、用户调研工具、可观测性工具（Datadog、Prometheus）、覆盖率报告（JaCoCo、Istanbul）。

**检查**: 指标是否有基准值和目标值？数据源是否可获取且成本合理？测量结果是否可重复验证？

---

## A — Achievable (可达成)

**定义**: 目标在给定约束（时间、资源、技能）下应当现实可行。SMART 鼓励有挑战性（stretch）但不脱离实际的目标。

**正例**: "Q3 内将测试覆盖率从 65% 提升至 80%"（配备 2 名专职 QA）
**反例**: "下个 Sprint 实现 100% 覆盖"（无资源变化，遗留代码庞大）

**可达成性检查三要素**:
1. **Authority**：团队是否有权独立推进？
2. **Resources**：预算、人力、工具是否充足？
3. **Skills**：团队是否具备所需领域知识和技术能力？

任意一项严重不足，须分解为更小里程碑或优先解决依赖。

---

## R — Relevant (相关)

**定义**: 目标必须与更广泛的业务目标对齐。任何不服务于业务目标的努力都是浪费。

**正例**: 目标直接映射到业务目标 ID（如 OBJ-003：收入增长）
**反例**: "重构用户详情页代码"（无对应的性能、安全或功能价值驱动）

**可追溯性要求**: 每个需求（REQ-*）须映射到至少一个业务目标（OBJ-*），追溯矩阵中维护，REQ-COVER KPI 要求 ≥95%。

**追溯矩阵示意**:
```yaml
traceability:
  - req: REQ-001
    objectives: [OBJ-001, OBJ-002]
```

---

## T — Time-bound (有时限)

**定义**: 目标必须有明确的截止时间或迭代边界。没有时限的目标只是愿望清单。

**正例**: "在 Sprint 3 结束前（2024-06-30）完成"
**反例**: "以后再说" 或 "逐步优化"

**反模式 — 无期限延期**: 无 scope change 的情况下反复推迟截止日期使目标失去约束力。单次延期 ≤2 周：负责人批准；>2 周：须目标创建者与利益相关者重新审核。

**时态建议**: 季度目标用 Q1-Q4 + 日期；Sprint 目标用 Sprint End Date；持续性目标（如 SLO）用滚动窗口（如 "30 天滚动窗口 ≥99.9%"）。

---

## SMART 反模式（Anti-patterns）

| 反模式 | 描述 | 后果 | 预防 |
|--------|------|------|------|
| Fake SMART（假 SMART） | 看似具体却缺乏基线（如"提升性能 10%"无当前值） | 无法判断达成 | 百分化目标必须附带基准值 |
| Goal Creep（目标蔓延） | 不断扩大范围，不调时间线 | 资源分散、延迟 | 范围变更触发时间/资源重评估 |
| Metric Manipulation（指标操纵） | 优化指标数值而非业务结果 | 指标好看但价值未实现 | 增加结果性 KPI 作为补充 |
| Wishful Thinking（一厢情愿） | 未做可达成性分析的激进目标 | 挫败、放弃 | 执行前置的 Achievability Check |
| Goal Overload（目标过多） | 同时追踪超过 5 个 SMART 目标 | 注意力分散、均未做好 | 每季度 ≤3 个目标 |

---

## SMART OKR/KPI 映射表

| 要素 | OKR 对应 | KPI 对应 | 检查方法 |
|------|----------|----------|----------|
| S | Key Result 的描述 | KPI 定义文档 | 是否写清对象和维度？ |
| M | KR 含数字目标和单位 | KPI 有基准和目标值 | 数据源是否可获取？ |
| A | KR 有 stretch 但现实 | 历史趋势分析 | 团队是否 Review 承诺？ |
| R | 对齐 Mission / 战略 OBJ | KPI 树关联 | 是否可追溯到 OBJ-*？ |
| T | 季度/月度交付节点 | 数据采集周期 | 截止日期是否明确？ |

---

## 业务目标写法（OBJ-*）

**格式**: `OBJ-{NNN}: {动词}{对象} — KPI: {指标名} — Target: {数值} — By: {日期/迭代}`

**字段说明**:
- `OBJ-{NNN}`：三位数 ID，从 001 递增，不重复
- `{动词}{对象}`：动作与对象组合，如"将结账完成率从 62% 提至 75%"
- `KPI: {指标名}`：主 KPI 标识符，snake_case
- `Target: {数值}`：目标值（百分比/绝对值/比率）
- `By: {日期/迭代}`：截止时间（ISO 日期 YYYY-MM-DD 或 Sprint 标识）

**正例**:
```markdown
- OBJ-001: 将结账完成率从 62% 提升至 75% — KPI: checkout_completion_rate — Target: 75% — By: 2024-08-30
- OBJ-002: 将注册流程耗时从 120s 降至 45s — KPI: registration_duration_p95 — Target: 45s — By: Sprint 3
```

**反例**: "提升用户体验"（缺少 S、M、T）；"OBJ-001: 改进性能"（缺少 Target 和 By）

---

## 功能需求（REQ-*）

**格式定义**:
```markdown
### REQ-{NNN}: {标题}

**Story**: As a {角色}, I want {能力}, so that {价值}.
**Priority**: P0|P1|P2|P3
**Related OBJ**: OBJ-{NNN}, OBJ-{NNN}

**Acceptance** (Given-When-Then):
- AC-001: Given {前置条件}, When {触发动作}, Then {期望结果}.
```

**字段**:
- `REQ-{NNN}`：三位数唯一需求 ID
- `Priority`：P0 阻塞级，P1 高优，P2 中优，P3 低优
- `Related OBJ`：满足 R — Relevant 的业务目标 ID 列表
- `Acceptance`：Given-When-Then 验收标准，每条以 AC-{NNN} 编号

**正例**:
```markdown
### REQ-001: 结账页面性能优化

**Story**: As a 购物用户, I want 结账页面在 1 秒内加载, so that 我不因等待而放弃购买.
**Priority**: P1
**Related OBJ**: OBJ-001, OBJ-003

**Acceptance**:
- AC-001: Given 用户已登录且购物车有商品, When 点击"结算", Then 页面在 1s 内完全渲染.
```

**详细格式**参见 [user-story-format.md](user-story-format.md)。

---

## Examples

### 完整 SMART 目标（符合标准）

```markdown
OBJ-004: 提升 API 可用性至 99.95% — KPI: api_availability — Target: 99.95% — By: 2024-Q4

S — 对象为核心 API 网关，维度为可用性
M — 可用性 = (成功响应数 / 总请求数) × 100%，Prometheus 自动采集
A — 当前 99.5%，Q4 内通过冗余部署和限流优化可实现 99.95%
R — 对齐 OBJ-002（系统可靠性），直接支撑 SLA
T — Q4 截止日期与年度可靠性目标对齐
```

### 不符合 SMART 的目标

```markdown
"持续优化系统质量"

S — 缺失："系统"指哪个子系统？"质量"指性能、可用性还是可维护性？
M — 缺失：无数值或比例，无法衡量
A — 不确定：无当前基线，无法判断是否现实
R — 不明确：看不到与 OBJ-* 的关联
T — 缺失：无截止日期，"持续"是无终止指令
```

### 从模糊到 SMART 的改写

| 模糊版本 | SMART 版本 |
|-----------|------------|
| 加强监控 | OBJ-005: 实现核心交易链路全量可观测性 — Target: ≥95% 链路被追踪 — By: Sprint 4 |
| 写更多测试 | OBJ-006: 微服务 A 测试覆盖率从 40% 至 85% — KPI: unit_test_coverage — Target: 85% — By: 2024-09-30 |

---

## Compliance Checklist

在提交 OBJ-* 或 REQ-* 前逐项检查：

```
- [ ] S: 目标是否明确描述了谁、做什么、在何处？
- [ ] M: 目标是否有可量化的指标和具体数值（含基准值）？
- [ ] A: 目标在当前约束（时间、资源、技能）下是否现实可实现？
- [ ] R: 目标是否可追溯到业务目标（OBJ-*）？
- [ ] T: 目标是否有明确的截止日期或迭代边界？
- [ ] 是否有明确的数据源来衡量进度？数据是否可获取？
- [ ] 目标是否避免了指标操纵或 goal creep 风险？
- [ ] 目标是否经过团队 Review 和承诺（尤其是 A — Achievable）？
```

**使用方式**: 在 OBJ Review、需求评审和 Sprint Planning 中使用。目标须满足 ≥5/8（S、M、T 为必选）。不满足项须补充说明或重新修订。

---

## Related Standards

- **[invest-principle.md](invest-principle.md)** — 用户故事 INVEST 原则，与 SMART 互补
- **[user-story-format.md](user-story-format.md)** — REQ-* 详细模板和示例
- **[harness-engineering.md](harness-engineering.md)** — AI Harness Engineering 总体规范
- **[id-generation-quantification.md](id-generation-quantification.md)** — OBJ-ID、REQ-ID 和指标 ID 的生成规则
