---
name: invest-principle
description: "INVEST 用户故事原则标准，定义 Independent/Negotiable/Valuable/Estimable/Small/Testable 六项原则及故事拆分技术和反模式"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
tags: ['standard', 'agile', 'user-story', 'invest', 'backlog']
---

# INVEST 用户故事原则标准

## Overview

**Purpose**: INVEST 是敏捷软件开发和 Extreme Programming (XP) 方法中用于评估用户故事质量的助记原则。它提供了一套客观标准，帮助产品负责人、业务分析师和开发团队编写、拆分和优先级排序用户故事，确保 backlog 中的每一项都是可操作、可估算且独立交付价值的。

**Scope**: 本标准适用于本项目中所有用户故事（User Story）、场景（Scenario）、特性（Feature）以及任何形式的 backlog 条目（backlog items），包括技术故事（Tech Story）、缺陷修复（Bug Fix）和探索性任务（Spike）。

**Goal**: 确保每一个 backlog 条目都是 actionable（可执行）、estimable（可估算）的，并且能够在无需依赖其他未完成项的前提下独立地向用户或干系人交付价值。遵循 INVEST 实践的团队，其交付节奏更可预测，计划偏差更小，利益相关者满意度更高。

## Core Content

### I - Independent（独立性）

**Definition**: 每个用户故事应该是自包含的，不与其他用户故事存在固有的先后依赖关系。理论上，故事应该可以以任意顺序实现和交付，而不会影响系统的运行或价值交付。

**Practice**:
- 在梳理 backlog 时主动识别故事间的依赖关系。如果两个故事相互依赖，考虑合并为一个故事，或者重新排序 backlog 使得依赖方向是单向且可控的。
- 在 backlog 管理工具中显式标记依赖关系，使用 `blocks` / `blocked by` 标签。依赖链不应超过两层。
- 当故事 A 需要故事 B 的功能时，考虑在故事 A 中先使用 Mock/Stub 来实现独立开发，待 B 完成后替换为真实实现。
- 使用 Feature Toggle（特性开关）来解耦故事的发布依赖。

**Good example**: "作为用户，我可以通过邮箱链接重置密码，以便在我忘记密码时恢复账户访问。"——该故事独立于注册、登录等其他认证故事，可以单独开发、测试和交付。

**Bad example**: "作为用户，我可以登录"——该故事隐含着对"作为用户，我可以注册"的依赖（没有账号如何登录？）。应该拆分为两个独立的、均可独立交付的故事，或在第一个故事中提供预置账号等初始条件。

**Anti-pattern**: 故事链（Story Chain）——故事 A 依赖 B，B 依赖 C，C 依赖 D。当任何一个环节被延迟时，整条链上的故事都陷入阻塞状态，造成 cascading failure，严重影响交付承诺。

### N - Negotiable（可协商性）

**Definition**: 用户故事不是一份不可变更的合同或详尽的需求规格说明书。故事的细节通过团队（PO、BA、Dev、QA）之间的持续对话（conversation）而逐步显现。故事卡片只是一个"对话的令牌"（token for conversation），而不是最终的需求文档。

**Practice**:
- 保持故事表述轻量化（lightweight），足以传达意图（intent）即可，不要在一开始就编写完整的技术规范。
- 使用验收条件（Acceptance Criteria）来框定故事的讨论范围，而不是穷尽所有细节。3-5 条验收条件通常是健康的上限。
- 在 Sprint Planning 或 Backlog Refinement 中预留时间讨论故事细节。讨论结果记录在故事的注释（comments）或验收条件中，而非故事标题或描述本身。
- 拥抱变更：如果在 Sprint 期间发现更好的实现方式或新的需求，允许通过 PO 调整故事的范围。

**Good example**: "作为管理员，我可以在后台启用双因素认证（2FA），以提高账户安全性。*待讨论：使用邮箱验证码还是短信验证码，在 Sprint Planning 中决定。*"——故事传达意图，具体方案留给团队协商。

**Bad example**: 在故事附件中包含一份 10 页签完字的软件需求规格说明书（SRS），规定每一行 UI 文案、所有异常码和数据库表结构。——故事变得不可协商（non-negotiable），团队失去了自主权和创造力，沦为需求执行机器。

**Anti-pattern**: 过度规格化（Over-specification）——PO 在故事中写入了技术方案细节（"使用 Redis 实现缓存"、"调用 XXX API"），剥夺了技术团队的设计自主权。故事应该描述"什么"（what）和"为什么"（why），而不是"如何做"（how）。

### V - Valuable（有价值）

**Definition**: 每一个用户故事必须能够向最终用户、客户或其他干系人交付明确的价值。价值的表述应该是具体的、可感知的，而不是笼统的"改进系统"。如果故事无法回答"为什么用户/业务需要这个？"那么它可能不应该出现在当前的 Sprint 中。

**Practice**:
- 每个故事必须包含"以便..."（so that）子句，明确指出价值的接收者和价值本身。
- 将每一个故事映射到一个业务目标（OBJ-*），确保投资有迹可循。没有业务目标映射的故事应受到质疑。
- 区分直接价值（用户可见的功能）和间接价值（技术改进带来的稳定性/性能提升）。间接价值故事应显式标注为 Tech Story 并说明最终用户收益。
- 使用 Impact Mapping 或 Value Stream Mapping 工具追溯故事的业务价值。

**Good example**: "作为顾客，我可以将购物车中的商品保存为草单，以便在我关闭浏览器后不会丢失已选商品，下次访问时可以继续选购。"——价值清晰明确：减少用户流失、提升购物体验。

**Bad example**: "作为开发者，我可以重构 UserController 类的方法签名。"——该故事没有清晰表述对用户或业务的价值。重构（Refactoring）类属于技术债务管理，应当有一个关联的用户价值故事（如"提高登录页面的响应速度"）作为 Tech Debt 的父级，并说明技术改进如何最终惠及用户。

**Anti-pattern**: 纯技术故事（Technical Stories）没有用户价值阐述——例如"迁移数据库到 PostgreSQL 13"、"从 Webpack 迁移到 Vite"。这些应当作为 Enabler Story 与一个功能故事绑定，或者明确标注为"以提升构建速度，为开发团队节省 X 小时/周"。

### E - Estimable（可估算）

**Definition**: 团队必须能够在 Sprint Planning 中对该故事的工作量做出具有合理置信度的估算。如果一个故事无法被估算，通常意味着团队对该故事的理解不够充分，或者故事的范围过于庞大/模糊。

**Practice**:
- 如果团队无法估算一个故事（"我们不知道该怎么做"或"这可能需要 1 天也可能需要 3 周"），意味着需要进一步拆分（split）故事，或者先安排一个 Spike 来消除不确定性。
- 使用标准的故事点（Story Points）估算方法（Fibonacci 序列：1, 2, 3, 5, 8, 13, 21）或 T-Shirt 尺寸（XS, S, M, L, XL）。同一团队应保持估算基准的一致性。
- 故事应附有足够的上下文（Context）和 3-5 条明确的验收条件，以及清晰的"完成定义"（Definition of Done）。
- 可以使用 Planning Poker（计划扑克）来集体估算，减少个人偏差。

**Good example**: 一个有充分上下文描述、3 条明确验收条件、以及 DoD 的故事。团队能够在 5 分钟内给出相对一致的估算（如 3 个 Story Points）。

**Bad example**: "提升系统性能"——范围过于模糊，无法估算。应该拆分为具体的故事："将用户列表页面的 P95 响应时间从 3s 降低至 500ms，通过添加数据库索引和缓存层实现。"

**Anti-pattern**: 故事规模超过一个 Sprint——如果一个故事被估算为 21 个 Story Points（对应一个 2 周的 Sprint 都无法完成），它实际上是一个 Epic（史诗），需要进行拆分。通常，单故事的估算不应超过团队一个 Sprint 总容量的 50%。

### S - Small（小粒度）

**Definition**: 用户故事必须足够小，能够在单个 Sprint/迭代内完成。小故事意味着风险低、可预测性高、交付频率快。Small 是 Estimable 的自然结果——通常一个故事如果可估算且估算结果合理（1-5 个 Story Points），则它自然就是 Small 的。

**Practice**:
- 每个故事应当在 2-3 天内完成（对于大多数成熟团队）。超过这个时间范围的故事应该被质疑。
- 使用"Sprint 规则"：如果一个故事的估算超过 Sprint 总容量的 50%，必须拆分。例如，2 周 Sprint（10 个工作日）中，单故事不应超过 5 个工作日的工作量。
- 拆分后的故事应保持"每个子故事仍然有独立价值"——避免产生"必须收集所有碎片才能交付价值"的情况。
- 故事拆分的合理粒度判断标准：完成该故事后能否触发一次发布（release）？如果不能，说明粒度仍然过大。

**Good example**: 一个 3 个 Story Points、预计 2 天完成的用户故事。描述聚焦、验收条件明确、边界清晰。

**Bad example**: 一个 21 个 Story Points 的"故事"——实际上是 Epic。包含登录、注册、密码重置、OAuth 集成等全部认证功能。无法在一个 Sprint 内完成，且风险极高。

**Anti-pattern**: 大杂烩故事（Soup Story）——将一个功能的方方面面（包括基础功能、高级功能、异常处理、性能优化、日志审计等）全部塞入一个故事中。正确的做法是按"最小可行增量"（Minimum Viable Increment）进行拆分，先交付核心价值，再通过后续故事迭代增强。

### T - Testable（可测试）

**Definition**: 每个用户故事必须具有清晰、客观的验收标准（Acceptance Criteria），使得 QA 和 PO 能够以"通过/不通过"的二元结果判断故事是否完成。Testable 直接影响到质量保障和"完成"的可信度。

**Practice**:
- 验收条件推荐使用 Given-When-Then 格式（行为驱动开发 BDD 模式）：
  - **Given**（给定）：初始上下文/前置条件
  - **When**（当）：用户执行某个操作
  - **Then**（那么）：期望的系统行为/输出
- 验收条件应同时覆盖：
  - Happy Path（正常流程）—— 1-2 条
  - 负面测试用例（异常流程）—— 1-2 条
  - 边界条件（Boundary Conditions）—— 0-1 条
  - 非功能需求（如性能、安全）—— 按需添加
- 验收条件应避免使用主观形容词（"友好的"、"快速的"、"美观的"），除非有明确的量化指标。

**Good example**: "Given 用户已登录且有商品在购物车中, When 用户点击'结算'按钮, Then 页面跳转到支付页面并显示订单金额汇总。Given 用户购物车为空, When 用户点击'结算'按钮, Then 页面提示'您的购物车为空'。Given 用户在结算页面, When 用户关闭浏览器, Then 再次访问时购物车内容保持不变。"

**Bad example**: "UI 应该更加用户友好"——该描述是主观的（subjective），不具备可测试性。应该重新表述为："用户登录后能在 3 次点击以内到达个人资料页面"或"注册表单的错误提示应出现在对应输入框下方，并以红色字体显示"。

**Anti-pattern**: 没有验收条件的故事（No Acceptance Criteria）——团队直到开发完成后才与 PO 对齐预期，导致返工（rework）和浪费。验收条件应当是故事的必要组成部分，缺失验收条件的故事不应进入 Sprint。

### 故事拆分技术

以下技术可用于将大故事拆分为符合 INVEST 原则的小故事。拆分的目标不是"把故事变小"，而是"让每个子故事独立交付价值并满足 INVEST 原则"。

| 拆分技术 | 说明 | 示例 |
|---|---|---|
| By Workflow Step（按工作流步骤） | 按用户操作流程的步骤拆分 | 注册流程拆分为：输入表单 → 邮箱验证 → 欢迎页 |
| By CRUD Operation（按 CRUD 操作） | 按创建/读取/更新/删除拆分 | 用户管理：创建用户 → 查看用户列表 → 编辑用户 → 删除用户 |
| By Business Rule Variant（按业务规则变体） | 按功能场景拆分 | 订单审核：人工审核（Happy Path）→ 自动规则审核 → 异常订单处理 |
| By UI / Platform（按平台） | 按界面或终端拆分 | 商品展示功能：桌面端 → 移动端 → 平板端；或 Web App → Mobile App → API |
| By Functionality Complexity（按功能复杂度） | 按功能的基本版和高级版拆分 | 搜索功能：关键词搜索（基本）→ 高级筛选（进阶）→ 语义搜索（高级） |
| Spike-first（先探索后拆分） | 对未知技术先行探索 | 如果团队对某项技术不确定（如"OAuth 集成"），先做 Spike 再拆分 |
| By Role（按角色） | 按用户角色拆分 | 订单功能：买家下单 → 卖家接单 → 管理员审核 |
| By Acceptance Criteria（按验收条件拆分） | 将多条验收条件拆分为独立故事 | 从"用户可搜索并筛选商品"拆分为"用户可按关键词搜索商品"和"用户可按价格范围筛选商品" |

## Examples

### Example 1: INVEST-Compliant Good Story

**Title**: 用户可以通过邮箱验证重置密码

**Description** (User Story format):
作为注册用户，我想要在忘记密码时通过注册邮箱链接重置密码，以便我在无法登录时仍可恢复账户访问。

**Acceptance Criteria**:
- Given 用户未登录, When 用户点击"忘记密码", Then 显示输入邮箱的表单
- Given 用户输入了已注册的邮箱, When 用户点击"发送重置链接", Then 系统发送包含重置链接的邮件
- Given 用户点击邮件中的有效重置链接（24 小时内）, When 用户设置新密码并提交, Then 密码更新成功且用户被重定向到登录页
- Given 用户点击已过期的重置链接（超过 24 小时）, When 用户尝试设置新密码, Then 显示"链接已过期，请重新申请"

**INVEST Analysis**:
- **Independent**: 不依赖其他认证故事，可使用 Mock 的邮件服务独立开发
- **Negotiable**: 描述了功能意图和验收条件，但邮件模板内容和发送策略留待团队讨论
- **Valuable**: 解决用户"忘记密码"的真实痛点，减少客服工单量
- **Estimable**: 团队可以基于 4 条清晰地验收条件给出合理的估算（3-5 Story Points）
- **Small**: 可在 2-3 天内完成
- **Testable**: Given-When-Then 格式使每个验收条件都可以客观验证

### Example 2: Non-INVEST-Compliant Story (Violates Multiple Principles)

**Title**: 实现完整的用户管理系统

**Description (原文)**: 用户可以在系统里管理账号，包括全部使用者功能。需要做得好看好用。

**INVEST Analysis** (Violations marked):

| Principle | Status | Explanation |
|---|---|---|
| Independent | FAIL | 隐含着大量未说明的前置依赖（如权限系统、组织架构、通知服务、审计日志），实际上是一个大型 Epic |
| Negotiable | FAIL | "需要做得好看好用"过于模糊，且无讨论空间 |
| Valuable | FAIL | "用户管理账号"价值未聚焦到特定用户/场景，so that 子句缺失 |
| Estimable | WARN | 范围太广，无法估算——团队无法给出合理的 Story Points |
| Small | FAIL | 估算远超过一个 Sprint 的容量，属于典型的反模式 |
| Testable | FAIL | "好看好用"是主观标准，无法客观验证 |

**Corrective Action**: 应拆分为多个独立的 INVEST-compliant 故事，例如：
1. "作为管理员，我可以创建新用户账号"（3 pt）
2. "作为用户，我可以修改我的个人资料"（2 pt）
3. "作为管理员，我可以禁用某个用户账号"（3 pt）
4. "作为用户，我可以重置我的密码"（5 pt）
5. "作为管理员，我可以查看所有活跃用户列表"（2 pt）

## Compliance Checklist

以下清单用于在 Backlog Refinement 和 Sprint Planning 中逐项审查每个用户故事是否符合 INVEST 标准：

- [ ] **Independent**: Story 是否独立于其他 stories，不存在硬依赖或隐式依赖？
- [ ] **Negotiable**: Story 的描述是否避免过度规格化，保留团队协商和设计自主的空间？
- [ ] **Valuable**: Story 是否有明确的用户或业务价值（so that 子句），且能否映射到业务目标（OBJ-*）？
- [ ] **Estimable**: 团队是否能对 story 进行合理的估算，且所有参与者对估算基准达成一致？
- [ ] **Small**: Story 是否可在一个 sprint 内完成，且估算不超过 sprint 总容量的 50%？
- [ ] **Testable**: 验收标准是否清晰、可测试（推荐 Given-When-Then 格式），是否同时覆盖正常和异常流程？
- [ ] **Negotiable (bis)**: Story 是否有过多技术细节导致不可协商，是否应当删除实现细节？
- [ ] **Definition of Done**: Story 的完成定义（Definition of Done）是否明确？是否包含代码审查、测试覆盖率和文档要求？

**使用建议**: 上述清单应当在 Backlog Refinement 会议中逐条审查。任何一条标记为 FAIL 的故事应当立即进行修正（拆分、重新描述或补充信息），不得未经修正而进入 Sprint 队列。

## Related Standards

本标准是 E2E Delivery Harness 质量管理体系的一部分。执行和审计时应结合以下相关标准：

- [smart-criteria.md](smart-criteria.md) — SMART 验收条件标准，与 INVEST 的 T（Testable）紧密结合
- [user-story-format.md](user-story-format.md) — 用户故事标准格式模板，提供 INVEST 的载体结构
- [harness-engineering.md](harness-engineering.md) — E2E Delivery Harness 总体标准和工程规范
- [authoring-checklist.md](authoring-checklist.md) — 故事编写检查清单，整合 INVEST 合规检查
