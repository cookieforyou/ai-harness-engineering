---
name: naming-conventions
description: "命名规范标准，定义 E2E Delivery Harness 所有资产的 {verb}-{noun} kebab-case 命名模式、动词枚举表、名词后缀约定、多级命名规范及跨平台兼容性限制"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'naming', 'conventions', 'consistency']
---

# 命名规范标准

## Overview

本文件定义了 E2E Delivery Harness 资产库中所有资产的统一命名规范。核心原则是所有资产（Prompt / Instruction / Agent / Skill / Scenario / Standard）统一采用 `{verb}-{noun}` kebab-case 命名模式，确保命名一致性、可识别性和跨平台兼容性。

## Core Naming Pattern（核心命名模式）

```
{verb}-{noun}

格式约束：
- 全小写字母
- 多词间以连字符（-）分隔
- 禁止使用下划线、空格、大写字母
- 名词部分可包含多个单词（如 `disaster-recovery`）
- 总长度建议 8-40 个字符
- 正则校验：^[a-z][a-z0-9-]*$
```

## Verb Enumeration Table（动词枚举表）

以下动词库涵盖了 E2E Delivery Harness 的全部标准业务场景。每个场景名称必须从下表选取一个动词。

| 动词 | 英文用途 | 中文用途 | 命名示例 |
|------|---------|---------|---------|
| `analyze` | Analysis & Assessment | 分析评估 | `analyze-requirement` |
| `design` | Design & Planning | 设计规划 | `design-architecture` |
| `implement` | Implementation & Development | 实施开发 | `implement-feature` |
| `deploy` | Deployment & Release | 部署发布 | `deploy-release` |
| `monitor` | Monitoring & Observation | 监控观测 | `monitor-operate` |
| `audit` | Audit & Inspection | 审计检查 | `audit-security` |
| `review` | Review & Examination | 审查评审 | `review-code` |
| `plan` | Planning & Scheduling | 规划计划 | `plan-rollback` |
| `manage` | Management & Administration | 管理维护 | `manage-config` |
| `migrate` | Migration & Transformation | 迁移转换 | `migrate-environment` |
| `verify` | Verification & Testing | 验证测试 | `verify-test` |
| `integrate` | Integration & Connection | 集成对接 | `integrate-api` |
| `optimize` | Optimization & Improvement | 优化改进 | `optimize-performance` |
| `respond` | Response & Handling | 响应处理 | `respond-incident` |
| `backup` | Backup & Recovery | 备份恢复 | `backup-data` |
| `setup` | Setup & Configuration | 搭建配置 | `setup-infra` |
| `prepare` | Preparation | 准备筹备 | `prepare-release` |
| `document` | Documentation | 文档编写 | `document-project` |
| `decompose` | Decomposition & Breakdown | 分解细化 | `decompose-task` |
| `apply-hotfix` | Hotfix Application | 热修复 | `apply-hotfix` |
| `automate` | Automation | 自动化 | `automate-test` |
| `schedule` | Scheduling & Timing | 调度安排 | `schedule-job` |
| `validate` | Validation & Compliance | 验证合规 | `validate-compliance` |
| `archive` | Archiving & Retention | 归档保存 | `archive-log` |
| `rollback` | Rollback & Revert | 回滚恢复 | `rollback-deployment` |

### 动词选择原则

1. **精确匹配**: 优先选择与资产核心动作最匹配的动词
2. **避免重叠**: 同一场景内不应出现动词接近的资产（如 `monitor-operate` 和 `monitor-track` 选择其一）
3. **动词唯一性**: 每个 `{verb}-{noun}` 组合在整个资产库中必须唯一

## Noun Specification（名词规范）

名词部分应准确反映资产所处理的业务对象。以下为资产后缀约定：

| 资产类型 | 后缀/标识 | 文件模式 | 示例 |
|---------|----------|---------|------|
| **Scenario** | 场景命名（无后缀） | `{verb}-{noun}/SCENARIO.md` | `analyze-requirement/SCENARIO.md` |
| **Agent** | `.agent.md` | `{verb}-{noun}.agent.md` | `analyze-requirement.agent.md` |
| **Prompt** | `.prompt.md` | `{verb}-{noun}.prompt.md` | `analyze-requirement.prompt.md` |
| **Instruction** | `.instructions.md` | `{verb}-{noun}.instructions.md` | `analyze-requirement.instructions.md` |
| **Skill** | `SKILL.md` | `{verb}-{noun}/SKILL.md` | `analyze-requirement/SKILL.md` |
| **Standard** | `.md` | `{verb}-{noun}.md` | `naming-conventions.md` |
| **Template** | `.template.md` | `{verb}-{noun}.template.md` | `scenario.template.md` |
| **Evaluation** | 随场景 | `{verb}-{noun}/evaluation-*.md` | `analyze-requirement/evaluation-checklist.md` |
| **Workflow / Pipeline** | `.pipeline.md` | `{verb}-{noun}.pipeline.md` | `e2e-delivery.pipeline.md` |

### 名词短语构造指南

- 名词短语使用单数形式（`requirement` 而非 `requirements`）
- 使用连字符连接复合名词（`disaster-recovery` 而非 `disasterrecovery`）
- 避免无信息量的通用名词（`thing`, `data`, `info`）
- 同一场景内，名词部分必须在 5 类资产中保持一致

## Multi-level Naming（多级命名）

### 场景内文件命名

场景目录内的子文件命名遵循：

```
{verb}-{noun}/
├── SCENARIO.md                     # 场景主文件（固定名称）
├── evaluation-checklist.md         # 评估清单
├── sub-task-{n}.md                 # 子任务文件（n 为序号，如 01, 02）
├── context-{description}.md        # 上下文文件
└── resources/                      # 资源目录
    ├── {verb}-{noun}-template.md
    └── {verb}-{noun}-reference.md
```

### 子任务命名约定

子任务采用二层命名模式：

```
{verb}-{noun}/sub-task-{seq}-{short-description}.md

示例：
design-system/sub-task-01-api-contract.md
design-system/sub-task-02-data-model.md
implement-feature/sub-task-01-database-schema.md
implement-feature/sub-task-02-service-layer.md
```

### 编排编号规则

| 编号前缀 | 用途 | 模式 | 示例 |
|---------|------|------|------|
| `REQ-` | 需求项 | `REQ-{NNN}` | `REQ-001` |
| `DES-` | 设计项 | `DES-{NNN}` | `DES-001` |
| `TASK-` | 任务项 | `TASK-{NNN}` | `TASK-001` |
| `AC-` | 验收条件 | `AC-{REQ#}-{N}` | `AC-042-1` |
| `TC-` | 测试用例 | `TC-{NNN}` | `TC-001` |
| `BUG-` | 缺陷 | `BUG-{NNN}` | `BUG-001` |
| `RISK-` | 风险项 | `RISK-{NNN}` | `RISK-001` |
| `DC-` | 决策点 | `DC-{NNN}` | `DC-001` |
| `QG-` | 质量门禁 | `QG-{NNN}` | `QG-001` |
| `MET-` | 指标项 | `MET-{NNN}` | `MET-001` |
| `EH-` | 错误处理 | `EH-{NNN}` | `EH-001` |
| `INC-` | 故障项 | `INC-{NNN}` | `INC-001` |
| `CHG-` | 变更项 | `CHG-{NNN}` | `CHG-001` |
| `HANDOVER-` | 交接项 | `HANDOVER-{NNN}` | `HANDOVER-001` |
| `NFR-` | 非功能需求 | `NFR-{NNN}` | `NFR-001` |
| `V-` | 验证项 | `V-{NNN}` | `V-001` |
| `IMPROVE-` | 改进项 | `IMPROVE-{NNN}` | `IMPROVE-001` |

所有编号统一采用三位数字（从 `001` 开始），步长为 1。

## Good vs Bad Naming Examples

| 分类 | 不良命名（Bad） | 问题 | 正确命名（Good） |
|------|----------------|------|----------------|
| 动词位置错误 | `requirement-analyst` | 动词在后，不符 `{verb}-{noun}` | `analyze-requirement` |
| 角色命名 | `developer` | 非 `{verb}-{noun}`，无动词 | `implement-feature` |
| 角色命名 | `tester` | 非 `{verb}-{noun}`，无动词 | `verify-test` |
| 角色命名 | `devops-engineer` | 角色词而非动作+对象 | `deploy-release` |
| 下划线分隔 | `analyze_requirement` | 使用下划线而非连字符 | `analyze-requirement` |
| 大写字母 | `AnalyzeRequirement` | 使用 PascalCase | `analyze-requirement` |
| 空格分隔 | `analyze requirement` | 包含空格 | `analyze-requirement` |
| 动词不精确 | `do-requirement` | `do` 不是标准动词 | `analyze-requirement` |
| 名词复数 | `analyze-requirements` | 名词使用了复数形式 | `analyze-requirement` |
| 无信息名词 | `manage-stuff` | `stuff` 无业务含义 | `manage-config` |
| 过于冗长 | `implement-user-authentication-and-authorization-module` | 超过 40 字符 | `implement-auth` |
| 过于简短 | `run` | 缺少名词 | `run-task` |
| 动词重叠 | `integrate-monitor` + `monitor-integrate` | 同一场景两个不同动词 | 统一选择一个 |
| 中文命名 | `分析需求` | 混入中文字符 | `analyze-requirement` |
| 特殊字符 | `analyze-requirement-v2-final` | 含 `v2`, `final` 等版本标记 | 用 Git tag 管理版本 |
| 多动词 | `analyze-and-design-system` | 一个名称含两个动词 | 拆分为两个资产 |

## Cross-platform Compatibility（跨平台兼容性）

文件名在不同操作系统上的限制对照表：

| 限制项 | Windows (NTFS) | macOS (APFS/HFS+) | Linux (Ext4/XFS) | 影响 |
|--------|---------------|-------------------|-----------------|------|
| 保留字符 | `\ / : * ? " < > |` | `:`（HFS+）, `/` | 仅 `/`（路径分隔符） | 命名中禁止出现 `\ / : * ? " < > |` |
| 区分大小写 | 不区分（`A.txt` = `a.txt`） | HFS+ 不区分 / APFS 默认区分 | 严格区分 | 推荐保持全小写避免冲突 |
| 最大路径长度 | 260 字符（可启用长路径至 32767） | 255 字符（单组件） | 255 字符（单组件） | 总路径（含目录）建议 ≤ 200 字符 |
| 保留名称 | `CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9` | 无 | 无 | 资产名避免使用 DOS 保留名 |
| 尾随空格/点 | 自动去除尾随空格和 `.` | 允许 | 允许 | 文件名首尾不应有空格或 `.` |
| 编码 | UTF-16（转 UTF-8 有限） | UTF-8 | UTF-8 | 仅使用 ASCII 字母/数字/连字符 |

### 命名兼容性推荐

1. **全小写**: 避免 macOS 大小写不敏感导致的碰撞
2. **仅 ASCII**: 避免不同系统编码差异
3. **单组件 ≤ 100 字符**: 为嵌套路径预留空间
4. **避免 `-` 开头**: 部分工具可能误识别为命令行参数
5. **后缀明确**: 使用 `.md`, `.agent.md`, `.instructions.md`, `.prompt.md`, `.pipeline.md`, `.template.md` 六种标准后缀
6. **禁止尾随连字符**: 文件名不应以连字符结尾（如 `analyze-`）

### 目录命名规范

| 目录 | 命名规范 | 示例 |
|------|----------|------|
| Agent 目录 | `agents` | `agents/` |
| Instruction 目录 | `instructions` | `instructions/` |
| Prompt 目录 | `prompts` | `prompts/` |
| Skill 目录 | `skills` | `skills/` |
| Scenario 目录 | `scenarios` | `scenarios/` |
| Workflow 目录 | `workflows` | `workflows/` |
| Context 目录 | `contexts` | `contexts/` |
| Standard 目录 | `standards` | `standards/` |
| Template 目录 | `templates` | `templates/` |
| Evaluation 目录 | `evaluations` | `evaluations/` |
| Archive 目录 | `archive` | `archive/` |
| 资源目录 | `resources` | `{scenario}/resources/` |

目录名采用全小写英文复数形式，不含连字符。

## Compliance Checklist

- [ ] 资产文件名符合 `^[a-z][a-z0-9-]*$` 正则
- [ ] 资产类型后缀正确（`.agent.md` / `.instructions.md` / `.prompt.md` / `.pipeline.md` / `.template.md` / `.md` for Standard）
- [ ] 动词选自标准动词枚举表
- [ ] 同一场景内 5 类资产命名完全一致
- [ ] 不包含下划线、大写字母、空格
- [ ] 名词使用单数形式
- [ ] 总长度在 8-40 字符之间
- [ ] 不包含 DOS 保留名称（CON, PRN, AUX, etc.）
- [ ] 不以连字符或数字开头
- [ ] 不以连字符结尾
- [ ] 不包含版本标记（v1, final, draft 等后缀）
- [ ] 跨平台兼容：仅使用 ASCII + 连字符

## Related Standards

- [lifecycle.md](lifecycle.md) - 资产生命周期管理标准（文件名质量门禁）
- [output-quality-rubric.md](output-quality-rubric.md) - 产出质量评估标准（命名规范作为评估维度）
- [error-classification.md](error-classification.md) - 错误分类与处理策略（EH-* 编号）
- [user-story-format.md](user-story-format.md) - 用户故事格式标准（编号格式 REQ-*, AC-*）
