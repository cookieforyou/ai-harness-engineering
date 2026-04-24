# Naming Conventions - 命名规范

## 概述

本文档定义了 E2E Delivery Harness 资产库的命名规范，确保资产命名的一致性和可识别性。

## 通用命名原则

1. **清晰性**：名称应清晰表达资产内容和用途
2. **一致性**：同类资产采用统一的命名模式
3. **简洁性**：避免不必要的冗长
4. **可搜索性**：支持通过名称快速定位资产

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

### 资产命名规范

> **核心原则**: 资产命名采用 `{action}-{object}` 模式，确保 Prompt/Instruction/Agent/Skill/Scenario 命名对齐

#### 命名模式定义

| 资产类型 | 模式 | 说明 |
|----------|------|------|
| Prompt | `{verb}-{noun}` | 动词-名词，如 `analyze-requirement` |
| Instruction | `{verb}-{noun}` | 与 Prompt 对齐，如 `analyze-requirement` |
| Agent | `{noun}-{role}` | 名词-角色，如 `requirement-analyst` |
| Skill | `{noun}-{domain}` | 名词-领域，如 `requirement-analysis` |
| Scenario | `{noun}-{noun}` | 与 Skill 对齐，如 `requirement-analysis` |

#### 命名对齐表

> **核心原则**: Prompt/Instruction/Skill/Scenario 采用统一的 `{verb}-{noun}` 命名模式，Agent 采用 `{noun}-{role}` 模式

| 场景 | Prompt | Instruction | Agent | Skill | Scenario |
|------|--------|------------|-------|-------|----------|
| 需求分析 | `analyze-requirement` | `analyze-requirement` | `requirement-analyst` | `analyze-requirement` | `analyze-requirement` |
| 系统设计 | `design-system` | `design-system` | `system-designer` | `design-system` | `design-system` |
| 任务分解 | `decompose-task` | `decompose-task` | `task-decomposer` | `decompose-task` | `decompose-task` |
| 开发实现 | `implement-feature` | `implement-feature` | `developer` | `implement-feature` | `implement-feature` |
| 测试验证 | `verify-test` | `verify-test` | `tester` | `verify-test` | `verify-test` |
| 部署发布 | `deploy-release` | `deploy-release` | `devops-engineer` | `deploy-release` | `deploy-release` |
| 监控运维 | `monitor-operate` | `monitor-operate` | `sre-monitor` | `monitor-operate` | `monitor-operate` |
| 变更管理 | `manage-change` | `manage-change` | `change-manager` | `manage-change` | `manage-change` |
| 代码审查 | `review-code` | `review-code` | `code-reviewer` | `review-code` | `review-code` |
| 安全审计 | `audit-security` | `audit-security` | `security-auditor` | `audit-security` | `audit-security` |
| 故障复盘 | `review-incident` | `review-incident` | `incident-reviewer` | `review-incident` | `review-incident` |

#### Agent 文件

```regex
^[a-z][a-z0-9-]*\.agent\.md$

示例：
- requirement-analyst.agent.md
- system-designer.agent.md
- developer.agent.md
- change-manager.agent.md
- code-reviewer.agent.md
```

#### Skill 目录与文件

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
├── monitor-operate/
│   └── SKILL.md
├── manage-change/
│   └── SKILL.md
├── review-code/
│   └── SKILL.md
├── audit-security/
│   └── SKILL.md
└── review-incident/
    └── SKILL.md
```

#### Instruction 文件

```regex
^[a-z][a-z0-9-]*\.instructions\.md$

示例：
- analyze-requirement.instructions.md
- design-system.instructions.md
- implement-feature.instructions.md
- verify-test.instructions.md
- deploy-release.instructions.md
- monitor-operate.instructions.md
- manage-change.instructions.md
- review-code.instructions.md
- audit-security.instructions.md
- review-incident.instructions.md
```

#### Prompt 文件

```regex
^[a-z][a-z0-9-]*\.prompt\.md$

示例：
- analyze-requirement.prompt.md
- design-system.prompt.md
- implement-feature.prompt.md
- verify-test.prompt.md
- deploy-release.prompt.md
- monitor-operate.prompt.md
- manage-change.prompt.md
- review-code.prompt.md
- audit-security.prompt.md
- review-incident.prompt.md
```

#### Scenario 目录与文件

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
├── monitor-operate/
│   └── SCENARIO.md
├── manage-change/
│   └── SCENARIO.md
├── review-code/
│   └── SCENARIO.md
├── audit-security/
│   └── SCENARIO.md
├── review-incident/
│   └── SCENARIO.md
└── _template/
    └── SCENARIO.template.md
```

### 编号命名规范

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

### Workflow 文件

```regex
^[a-z][a-z0-9-]*\.pipeline\.md$

示例：
workflows/
├── e2e-delivery.pipeline.md
├── incident-response.pipeline.md
└── _template/
    └── PIPELINE.template.md
```

### Context 文件

```regex
^[a-z][a-z0-9-]*\.md$

示例：
contexts/
├── global-context.md
├── handover-context.template.md
└── unified-handover-template.md
```

### Evaluations 文件

```regex
^[a-z][a-z0-9-]*\.md$

示例：
evaluations/
├── regression-checklist.md
├── scorecard-template.md
├── output-validation-checklist.md
└── common-error-patterns.md
```

### Standards 文件

```regex
^[a-z][a-z0-9-]*\.md$

示例：
standards/
├── asset-model.md
├── naming-conventions.md
├── id-generation-quantification.md
└── output-quality-rubric.md
```

## 变量命名

### YAML 元数据

```yaml
name: <kebab-case>        # 名称
description: <string>    # 描述
category: <kebab-case>    # 分类
version: <semver>        # 版本
```

### Markdown 标题

```markdown
# 页面标题 (Title Case)
## 二级标题 (Title Case)
### 三级标题 (Title Case)
```

## 标签命名

### 标签格式

```regex
^[a-z][a-z0-9-]*$

示例：
- requirement
- design
- development
- testing
- deployment
```

### 常用标签

| 标签 | 用途 |
|------|------|
| requirement | 需求相关 |
| design | 设计相关 |
| development | 开发相关 |
| testing | 测试相关 |
| deployment | 部署相关 |
| monitoring | 监控相关 |
| critical | 关键资产 |
| deprecated | 已废弃 |

## 命名检查清单

### 文件命名检查

- [ ] 使用小写字母
- [ ] 使用连字符分隔单词
- [ ] 包含正确的文件扩展名
- [ ] 不包含特殊字符
- [ ] 不超过 100 字符

### 目录命名检查

- [ ] 使用小写字母
- [ ] 使用连字符分隔单词
- [ ] 不包含空格
- [ ] 不以数字开头
- [ ] 不超过 50 字符

## 反面示例

```markdown
# 错误
Requirement Analyst.md        # 包含空格
requirement_analysis.md       # 使用下划线
REQ-001.md                   # 使用大写
analyze requirement.md       # 包含空格

# 正确
requirement-analyst.agent.md
requirement-analysis.instructions.md
```

## 多语言支持

### 文件命名（中文环境）

```regex
^[a-z][a-z0-9-]*\.[a-z]{2}\.md$

示例：
- introduction.zh.md
- usage.zh.md
- introduction.en.md
- usage.en.md
```

### 资源标识（统一英文）

```yaml
name: requirement-analysis  # 始终使用英文
description: "需求分析相关"  # 描述可使用本地语言
```
