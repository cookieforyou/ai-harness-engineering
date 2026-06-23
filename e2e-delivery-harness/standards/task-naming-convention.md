---
name: task-naming-convention
description: "任务命名规范标准，定义 {verb}-{noun} kebab-case 命名模式、常用动词枚举、Task ID 生成规则和多级任务树命名规范"
type: standard
version: "1.1.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'task', 'naming', 'convention']
---

# 任务命名规范标准

> 本文件为 E2E Delivery Harness 引用标准。审查基准见 [harness-engineering.md](harness-engineering.md)。

## Overview

### Purpose
Standardize task naming across all project management systems (Jira, Linear, GitHub Issues, etc.) to ensure consistent, searchable, and scannable task identifiers. A unified naming convention reduces cognitive overhead during task creation, triage, and retrieval, and enables automated tooling to parse and route tasks reliably.

### Scope
All tasks, subtasks, backlog items, epics, stories, and task-related identifiers within the E2E Delivery Harness ecosystem. This standard applies to both human-authored and AI-generated tasks.

## Core Content

### 核心命名模式

Every task name MUST follow the `{verb}-{noun}` format in **kebab-case**.

#### Mandatory Rules

| Rule | Description | Correct | Incorrect |
|------|-------------|---------|-----------|
| Lowercase | All characters must be lowercase | `implement-login-api` | `Implement-Login-API` |
| Hyphen separator | Words separated by single hyphens | `deploy-production` | `deploy_production` |
| No spaces | Use hyphens instead of spaces | `design-db-schema` | `design db schema` |
| Verb first | Action verb at the start | `fix-login-redirect` | `login-redirect-fix` |

#### Prohibited Patterns

- `implementLoginApi` (camelCase)
- `implement_login_api` (snake_case)
- `-implement-login-api` (leading hyphen)
- `implement-login-api-` (trailing hyphen)
- `IMPLEMENT-LOGIN-API` (uppercase)

#### Examples

- `implement-login-api`
- `design-user-schema`
- `deploy-production`
- `test-payment-flow`
- `review-auth-pr`

### 常用动词枚举表

Use the following standardised verb table when selecting the action verb for a task name. Choose the **most specific** verb that accurately describes the work.

| 动词 | 适用场景 | 示例 |
|------|---------|------|
| analyze | 分析/调研/评估 | analyze-auth-options |
| design | 设计/架构 | design-db-schema |
| implement | 实现/编码 | implement-login-api |
| test | 测试/验证 | test-payment-flow |
| deploy | 部署/发布 | deploy-v2.3-to-staging |
| configure | 配置/设置 | configure-ci-pipeline |
| document | 文档/记录 | document-api-endpoints |
| refactor | 重构/优化 | refactor-user-service |
| fix | 修复/纠正 | fix-login-redirect-bug |
| review | 评审/审查 | review-auth-pr |
| migrate | 迁移/升级 | migrate-db-to-v2 |
| monitor | 监控/观察 | monitor-error-rates |
| optimize | 优化/性能 | optimize-query-speed |
| integrate | 集成/对接 | integrate-payment-gateway |
| secure | 安全/加固 | secure-api-endpoints |

#### Verb Selection Guidelines

- **Be specific**: Use `migrate` rather than `update`, `fix` rather than `change`.
- **Avoid generic verbs**: `do`, `make`, `update`, `handle`, `process` are rarely precise enough.
- **Prefer action verbs**: Choose verbs that describe *what* is being done, not the state after it is done.
- **Domain alignment**: Use domain-standard verbs (e.g., `deploy` for release engineering, `test` for QA).
- **Novel verbs**: If no verb in the enum fits, use a clear alternative with team consensus, then propose adding it to the enum.

### Task ID 生成规则

Task IDs serve as system-level identifiers for tooling, cross-referencing, and automation. They are distinct from task names, which serve human readability.

#### Format

```
{project-prefix}-{NNNN}
```

Example: `EH-0042`

#### Prefix Table

| Prefix | Domain | Example |
|--------|--------|---------|
| EH | E2E Harness core | EH-0012 |
| DOC | Documentation | DOC-0007 |
| INF | Infrastructure | INF-0031 |
| SEC | Security | SEC-0019 |
| QA | Quality Assurance | QA-0025 |

#### Numbering Rules

- Sequential numbering per prefix, zero-padded to four digits.
- Numbering starts at `0001` per prefix. Upon exhaustion, archive and create `{PREFIX}2-{NNNN}`.

#### Subtask IDs

Subtask IDs extend the parent task ID with a two-digit suffix:

```
{Parent-ID}-{NN}
```

Example: `EH-0042-01`

#### Task ID vs Name

| Aspect | Task ID | Task Name |
|--------|---------|-----------|
| Purpose | Machine identification | Human readability |
| Format | `EH-0042` | `implement-login-api` |
| Uniqueness | Globally unique | Contextually unique within an epic |
| Mutability | Immutable after creation | May be refined during grooming |
| Required | Always | Always |

Both fields are mandatory. A task MUST NOT be created without both a valid Task ID and a compliant task name.

### 多级任务树命名

Complex work is organised into a three-level hierarchy: Epic, Story, and Subtask. Each level follows its own naming pattern while maintaining consistency across the tree.

#### Hierarchy

```
Epic: [Epic] Auth: SSO Integration
  ├── Story: implement-saml-auth
  │     ├── Subtask: design-saml-xml-schema
  │     ├── Subtask: implement-saml-parser
  │     ├── Subtask: test-saml-response-handling
  │     └── Subtask: document-saml-config
  ├── Story: implement-oauth-integration
  └── Story: implement-session-mapping
```

#### Naming by Level

| Level | Format | Example |
|-------|--------|---------|
| Epic | `[Epic] {domain}: {feature-area}` | `[Epic] Auth: SSO Integration` |
| Story | `{verb}-{noun}` | `implement-saml-auth` |
| Subtask | `{verb}-{noun}` | `design-saml-xml-schema` |

#### Epic Naming Rules

- Always prefixed with `[Epic]` for instant recognisability.
- Domain and feature area separated by a colon and single space.
- Use Title Case for the feature area description.
- Domain must map to a recognised engineering domain (Auth, CI/CD, Database, API, Frontend, Observability, etc.).

#### Story Naming Rules

- Follows the standard `{verb}-{noun}` kebab-case pattern.
- Noun MAY include the epic domain for disambiguation (`implement-saml-auth` within the `Auth: SSO Integration` epic).
- Stories SHOULD be independently deliverable and testable.

#### Subtask Naming Rules

- Follows the standard `{verb}-{noun}` kebab-case pattern.
- Must be more specific than the parent story verb-noun pair.
- Subtasks SHOULD represent work completable in a single session (4-8 hours).

#### Tree Depth Guideline

- Maximum depth: Epic > Story > Subtask (3 levels).
- Sub-subtasks are prohibited. Work deeper than 3 levels should be split into additional stories.
- A story SHOULD have 2-8 subtasks. More than 8 suggests the story should be further decomposed.

### 命名质量规则

Adhering to these quality rules ensures task names are consistently scannable, searchable, and unambiguous.

#### Length

| Quality | Word count | Example |
|---------|-----------|---------|
| Ideal | 3-6 words | `implement-password-reset` |
| Maximum | 8 words | `migrate-user-accounts-to-v2-schema` |
| Too short | < 3 words | `fix-bug` (generic) |
| Too long | > 8 words | `implement-new-user-authentication-flow-with-okta-and-saml` (split into two tasks) |

#### Acronym and Abbreviation Rules

- **Allowed without definition**: API, DB, UI, CLI, CI/CD, SDK, SQL, HTML, CSS, JSON, YAML.
- **Disallowed**: Uncommon or team-specific acronyms without definition in the task description.
- **Ambiguous acronyms**: Spell out the first time (e.g., `implement-rbac-role-check` works only if RBAC is widely known; otherwise prefer `implement-role-based-access-control`).

#### Domain Context

- Include domain context when the noun segment could be ambiguous.
- Good: `test-payment-gateway-timeout` (domain: payment)
- Avoid: `test-timeout-handling` (unclear which system)
- Prefer domain nouns over generic nouns.
- Good: `design-mongodb-sharding-strategy`
- Avoid: `design-database-strategy` (too generic)

## Examples

### Example 1: Good Task Name

`implement-password-reset`
- Follows `{verb}-{noun}` kebab-case (verb: `implement`, noun: `password-reset`).
- 3 words (ideal range). Clearly describes a password reset feature.

### Example 2: Bad Task Name (with corrections)

`fix-stuff`
- Issue: Generic noun `stuff` conveys no domain context; only 2 words.
- Correction: `fix-login-redirect-bug` (specific verb, domain noun, 4 words).

### Example 3: Multi-word precision

`migrate-user-data-to-v2-schema`
- 7 words (within the 8-word maximum). Every word adds specificity.
- Verb `migrate` precisely describes the operation vs a generic `update`.

## Compliance Checklist

Use this checklist during task creation and review to ensure full compliance with this standard.

- [ ] 任务名是否遵循 {verb}-{noun} kebab-case 模式？
- [ ] 动词是否从标准动词枚举表中选取？
- [ ] 任务名长度是否在 3-6 个单词范围内？
- [ ] 是否避免了大写、空格和下划线？
- [ ] Task ID 是否使用正确的项目前缀？
- [ ] 多级任务树（Epic → Story → Subtask）是否层级清晰？
- [ ] 是否避免了过度缩写和晦涩术语？
- [ ] 名词是否足够具体以区分相似任务？

## Related Standards

- [harness-engineering.md](harness-engineering.md)
- [authoring-checklist.md](authoring-checklist.md)
- [asset-model.md](asset-model.md)
