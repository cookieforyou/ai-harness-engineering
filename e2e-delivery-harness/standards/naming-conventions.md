# Naming Conventions - 命名规范

## 概述

本文档定义了 E2E Delivery Harness 资产库的命名规范，确保资产命名的一致性和可识别性。

## 通用命名原则

1. **清晰性**：名称应清晰表达资产内容和用途
2. **一致性**：同类资产采用统一的命名模式
3. **简洁性**：避免不必要的冗长
4. **可搜索性**：支持通过名称快速定位资产

## 命名统一模式

> **核心原则**: 所有资产（Prompt/Instruction/Agent/Skill/Scenario）统一采用 `{verb}-{noun}` 命名模式，确保命名完全对齐

### 统一命名模式表

| 资产类型 | 模式 | 说明 |
|----------|------|------|
| Prompt | `{verb}-{noun}` | 动词-名词，如 `analyze-requirement` |
| Instruction | `{verb}-{noun}` | 与 Prompt 对齐，如 `analyze-requirement` |
| Agent | `{verb}-{noun}` | 与 Prompt 对齐，如 `analyze-requirement` |
| Skill | `{verb}-{noun}` | 与 Prompt 对齐，如 `analyze-requirement` |
| Scenario | `{verb}-{noun}` | 与 Prompt 对齐，如 `analyze-requirement` |

### 命名对齐示例

> **核心原则**: 所有 5 类资产使用统一的 `{verb}-{noun}` 命名

| 场景 | Prompt | Instruction | Agent | Skill | Scenario |
|------|--------|------------|-------|-------|----------|
| 需求分析 | `analyze-requirement` | `analyze-requirement` | `analyze-requirement` | `analyze-requirement` | `analyze-requirement` |
| 系统设计 | `design-system` | `design-system` | `design-system` | `design-system` | `design-system` |
| 任务分解 | `decompose-task` | `decompose-task` | `decompose-task` | `decompose-task` | `decompose-task` |
| 开发实现 | `implement-feature` | `implement-feature` | `implement-feature` | `implement-feature` | `implement-feature` |
| 测试验证 | `verify-test` | `verify-test` | `verify-test` | `verify-test` | `verify-test` |
| 部署发布 | `deploy-release` | `deploy-release` | `deploy-release` | `deploy-release` | `deploy-release` |
| 监控运维 | `monitor-operate` | `monitor-operate` | `monitor-operate` | `monitor-operate` | `monitor-operate` |
| API 集成 | `integrate-api` | `integrate-api` | `integrate-api` | `integrate-api` | `integrate-api` |
| 数据库设计 | `design-database` | `design-database` | `design-database` | `design-database` | `design-database` |
| 架构设计 | `design-architecture` | `design-architecture` | `design-architecture` | `design-architecture` | `design-architecture` |
| CI/CD 实施 | `implement-cicd` | `implement-cicd` | `implement-cicd` | `implement-cicd` | `implement-cicd` |
| 密钥管理 | `manage-secrets` | `manage-secrets` | `manage-secrets` | `manage-secrets` | `manage-secrets` |
| 性能优化 | `optimize-performance` | `optimize-performance` | `optimize-performance` | `optimize-performance` | `optimize-performance` |
| 环境迁移 | `migrate-environment` | `migrate-environment` | `migrate-environment` | `migrate-environment` | `migrate-environment` |
| 依赖管理 | `manage-dependencies` | `manage-dependencies` | `manage-dependencies` | `manage-dependencies` | `manage-dependencies` |
| 技术债务 | `manage-tech-debt` | `manage-tech-debt` | `manage-tech-debt` | `manage-tech-debt` | `manage-tech-debt` |
| 回滚计划 | `plan-rollback` | `plan-rollback` | `plan-rollback` | `plan-rollback` | `plan-rollback` |
| 事件响应 | `respond-incident` | `respond-incident` | `respond-incident` | `respond-incident` | `respond-incident` |
| 灾备恢复 | `plan-disaster-recovery` | `plan-disaster-recovery` | `plan-disaster-recovery` | `plan-disaster-recovery` | `plan-disaster-recovery` |
| 知识管理 | `manage-knowledge` | `manage-knowledge` | `manage-knowledge` | `manage-knowledge` | `manage-knowledge` |
| 冲刺规划 | `plan-sprint` | `plan-sprint` | `plan-sprint` | `plan-sprint` | `plan-sprint` |
| 项目文档 | `document-project` | `document-project` | `document-project` | `document-project` | `document-project` |
| 监控集成 | `integrate-monitor` | `integrate-monitor` | `integrate-monitor` | `integrate-monitor` | `integrate-monitor` |

## 文件命名

### 目录命名

| 目录 | 命名规范 | 示例 |
|------|----------|------|
| 角色目录 | agents | agents |
| 指令目录 | instructions | instructions |
| 提示词目录 | prompts | prompts |
| 技能目录 | skills | skills |
| 场景目录 | scenarios | scenarios |
| 工作流目录 | workflows | workflows |
| 上下文目录 | contexts | contexts |
| 规范目录 | standards | standards |
| 模板目录 | templates | templates |
| 评估目录 | evaluations | evaluations |

### Agent 文件

```regex
^[a-z][a-z0-9-]*\.agent\.md$

示例：
- analyze-requirement.agent.md
- design-system.agent.md
- implement-feature.agent.md
- verify-test.agent.md
- deploy-release.agent.md
- manage-dependencies.agent.md
- respond-incident.agent.md
- plan-disaster-recovery.agent.md
```

### Skill 目录与文件

```regex
# 目录
^[a-z][a-z0-9-]*$

# 文件
SKILL.md

示例：
skills/
├── analyze-requirement/
│   └── SKILL.md
├── design-system/
│   └── SKILL.md
├── implement-feature/
│   └── SKILL.md
├── verify-test/
│   └── SKILL.md
├── deploy-release/
│   └── SKILL.md
├── manage-dependencies/
│   └── SKILL.md
├── respond-incident/
│   └── SKILL.md
└── plan-disaster-recovery/
    └── SKILL.md
```

### Instruction 文件

```regex
^[a-z][a-z0-9-]*\.instructions\.md$

示例：
- analyze-requirement.instructions.md
- design-system.instructions.md
- implement-feature.instructions.md
- verify-test.instructions.md
- deploy-release.instructions.md
- manage-dependencies.instructions.md
- respond-incident.instructions.md
- plan-disaster-recovery.instructions.md
```

### Prompt 文件

```regex
^[a-z][a-z0-9-]*\.prompt\.md$

示例：
- analyze-requirement.prompt.md
- design-system.prompt.md
- implement-feature.prompt.md
- verify-test.prompt.md
- deploy-release.prompt.md
- manage-dependencies.prompt.md
- respond-incident.prompt.md
- plan-disaster-recovery.prompt.md
```

### Scenario 目录与文件

```regex
# 目录
^[a-z][a-z0-9-]*$

# 文件
SCENARIO.md

示例：
scenarios/
├── analyze-requirement/
│   └── SCENARIO.md
├── design-system/
│   └── SCENARIO.md
├── implement-feature/
│   └── SCENARIO.md
├── verify-test/
│   └── SCENARIO.md
├── deploy-release/
│   └── SCENARIO.md
├── manage-dependencies/
│   └── SCENARIO.md
├── respond-incident/
│   └── SCENARIO.md
├── plan-disaster-recovery/
│   └── SCENARIO.md
└── _template/
    └── SCENARIO.template.md
```

### Workflow 文件

```regex
^[a-z][a-z0-9-]*\.pipeline\.md$

示例：
- e2e-delivery.pipeline.md
- incident-response.pipeline.md
```

## 编号命名规范

| 类型 | 模式 | 示例 |
|------|------|------|
| 需求项 | `REQ-{NNN}` | `REQ-001` |
| 设计项 | `DES-{NNN}` | `DES-001` |
| 任务项 | `TASK-{NNN}` | `TASK-001` |
| 测试用例 | `TC-{NNN}` | `TC-001` |
| 缺陷 | `BUG-{NNN}` | `BUG-001` |
| 风险 | `RISK-{NNN}` | `RISK-001` |
| 改进项 | `IMPROVE-{NNN}` | `IMPROVE-001` |
| 决策点 | `DC-{NNN}` | `DC-001` |
| 验证项 | `V-{NNN}` | `V-001` |
| 错误处理 | `EH-{NNN}` | `EH-001` |
| 故障项 | `INC-{NNN}` | `INC-001` |
| 变更项 | `CHG-{NNN}` | `CHG-001` |
| 质量门禁 | `QG-{NNN}` | `QG-001` |
| 指标项 | `MET-{NNN}` | `MET-001` |
| 交接项 | `HANDOVER-{NNN}` | `HANDOVER-001` |

## 命名动词表

| 动词 | 用途 | 示例 |
|------|------|------|
| analyze | 分析评估 | `analyze-requirement` |
| design | 设计规划 | `design-system`, `design-architecture` |
| decompose | 分解细化 | `decompose-task` |
| implement | 实施开发 | `implement-feature`, `implement-cicd` |
| verify | 验证测试 | `verify-test` |
| review | 审查评审 | `review-code`, `review-design`, `review-incident` |
| deploy | 部署发布 | `deploy-release` |
| monitor | 监控运维 | `monitor-operate` |
| manage | 管理工作 | `manage-change`, `manage-config`, `manage-dependencies`, `manage-secrets`, `manage-knowledge` |
| audit | 审计检查 | `audit-security` |
| integrate | 集成对接 | `integrate-api`, `integrate-monitor` |
| optimize | 优化改进 | `optimize-performance` |
| migrate | 迁移转换 | `migrate-environment`, `migrate-data` |
| automate | 自动化 | `automate-test` |
| setup | 搭建配置 | `setup-infra` |
| backup | 备份 | `backup-data` |
| plan | 规划计划 | `plan-sprint`, `plan-capacity`, `plan-rollback`, `plan-disaster-recovery` |
| prepare | 准备 | `prepare-release` |
| document | 文档化 | `document-project` |
| respond | 响应处理 | `respond-incident` |
| hotfix | 热修复 | `hotfix` |

## 禁止的命名模式

| 旧模式 | 问题 | 正确模式 |
|--------|------|----------|
| `requirement-analyst` | 与其他资产不一致 | `analyze-requirement` |
| `system-designer` | 与其他资产不一致 | `design-system` |
| `developer` | 不符合 `{verb}-{noun}` | `implement-feature` |
| `tester` | 不符合 `{verb}-{noun}` | `verify-test` |
| `devops-engineer` | 与其他资产不一致 | `deploy-release` |
| `code-reviewer` | 与其他资产不一致 | `review-code` |
| `security-auditor` | 与其他资产不一致 | `audit-security` |
| `change-manager` | 不符合 `{verb}-{noun}` | `manage-change` |
| `incident-reviewer` | 与其他资产不一致 | `review-incident` |

## 版本历史

| 版本 | 日期 | 变更说明 |
|------|------|----------|
| 2.0.0 | - | 统一所有资产为 `{verb}-{noun}` 命名模式 |
| 1.0.0 | - | 初始版本 |
