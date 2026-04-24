# E2E Delivery Harness - AGENTS.md

## 项目概览

**项目名称**: E2E Delivery Harness (端到端交付全流程工作流资产库)

**项目描述**: 基于 AI Harness Engineering 理念设计的模块化交付全流程资产库，覆盖从需求分析到监控运维的完整生命周期，为 AI Agent 提供标准化的执行框架。

**核心目标**: 通过标准化的资产组合（Agent + Skill + Instruction + Prompt + Scenario），实现交付流程的一致性、可复用性和高质量。

---

## 设计理念

### 核心原则

1. **AI-First**: 所有资产设计以 AI 驾驭为核心
   - 每个 Scenario 包含 Chain of Thought 引导 AI 逐步思考
   - 每个 Prompt 包含变量定义、错误处理和输出验证
   - Scenario 和 Prompt 职责分离，Scenario 作为快速入口

2. **Pipeline 驱动**: 通过 Workflow 定义端到端流程，确保阶段间的有序衔接

3. **Context 传递**: 通过 Handover Context 实现阶段间的数据传递和上下文继承

4. **Quality Gate**: 每个阶段都有明确的准入准出标准，确保交付质量

### Prompt 增强结构

每个 Prompt 必须包含以下增强结构：

| 章节 | 用途 | 重要性 |
|------|------|--------|
| 变量定义 (Variables) | 明确输入参数 | 必填 |
| 思维链 (Chain of Thought) | 强制逐步推理 | 必填 |
| 错误处理 (Error Handling) | 异常情况处理 | 必填 |
| 输出验证 (Output Validation) | 质量自我检查 | 必填 |
| Handover 准备 | 阶段间交接 | 必填 |

详情见 [standards/asset-model.md](standards/asset-model.md)。

### ID 生成规范

使用统一 ID 编号体系：

| 前缀 | 用途 | 示例 |
|------|------|------|
| REQ | 需求项 | REQ-001 |
| DES | 设计项 | DES-001 |
| TASK | 任务项 | TASK-001 |
| TC | 测试用例 | TC-001 |
| BUG | 缺陷 | BUG-001 |
| DC | 决策点 | DC-001 |
| V | 验证项 | V-001 |

详情见 [standards/id-generation-quantification.md](standards/id-generation-quantification.md)。

### 量化标准

| 指标 | 标准值 | 说明 |
|------|--------|------|
| REQ-COVER | ≥95% | 需求覆盖率 |
| TEST-PASS | ≥90% | 测试通过率 |
| DEV-COVERAGE | ≥80% | 单元测试覆盖率 |
| DEPLOY-SUCCESS | ≥99% | 部署成功率 |
| MON-SLO | ≥99.5% | SLO 达成率 |

### 资产层级

```
Workflow (工作流层)
    ↓
Scenario (场景层) ← AI 的快速入口
    ├── Chain of Thought (思维链)
    ├── Decision Checkpoints (决策检查点)
    ├── Error Handling (错误处理)
    └── 引用 → Agent + Skill + Prompt

Prompt (执行层) ← AI 的执行脚本
    ├── 变量定义
    ├── 思维链
    ├── 错误处理
    ├── 输出验证
    └── Handover 准备

Context (上下文层)
    ├── Global Context (全局上下文)
    └── Handover Context (交接上下文)
```

---

## 项目结构

```
e2e-delivery-harness/
├── README.md                    # 项目总说明
├── INTRODUCTION.zh.md           # 中文介绍
├── USAGE.zh.md                  # 中文使用指南
│
├── workflows/                   # 工作流定义 (2个)
│   ├── README.md               # 工作流说明
│   ├── e2e-delivery.pipeline.md # E2E 交付全流程
│   └── incident-response.pipeline.md # 故障响应流程
│
├── contexts/                     # 共享上下文 (3个)
│   ├── README.md               # 上下文说明
│   ├── global-context.md        # 全局上下文定义
│   └── handover-context.template.md # 交接上下文模板
│
├── scenarios/                    # 场景定义 (11个) ← AI 主要入口
│   ├── README.md               # 场景使用指南
│   ├── analyze-requirement/    # 需求分析场景
│   │   └── SCENARIO.md
│   ├── design-system/          # 系统设计场景
│   │   └── SCENARIO.md
│   ├── decompose-task/     # 任务拆分场景
│   │   └── SCENARIO.md
│   ├── implement-feature/            # 开发实现场景
│   │   └── SCENARIO.md
│   ├── verify-test/                # 测试验证场景
│   │   └── SCENARIO.md
│   ├── deploy-release/            # 部署发布场景
│   │   └── SCENARIO.md
│   ├── monitor-operate/             # 监控运维场景
│   │   └── SCENARIO.md
│   ├── manage-change/       # 变更管理场景 (新增)
│   │   └── SCENARIO.md
│   ├── review-code/            # 代码审查场景 (新增)
│   │   └── SCENARIO.md
│   ├── audit-security/         # 安全审计场景 (新增)
│   │   └── SCENARIO.md
│   └── review-incident/         # 故障复盘场景 (新增)
│       └── SCENARIO.md
│
├── agents/                       # Agent 角色定义 (11个)
│   ├── README.md
│   ├── requirement-analyst.agent.md
│   ├── design-systemer.agent.md
│   ├── task-decomposer.agent.md
│   ├── developer.agent.md
│   ├── tester.agent.md
│   ├── devops-engineer.agent.md
│   ├── sre-monitor.agent.md
│   ├── change-manager.agent.md        # (新增)
│   ├── code-reviewer.agent.md          # (新增)
│   ├── security-auditor.agent.md       # (新增)
│   └── incident-reviewer.agent.md      # (新增)
│
├── skills/                       # Skill 技能模块 (11个)
│   ├── README.md
│   ├── analyze-requirement/
│   │   └── SKILL.md
│   ├── design-system/
│   │   └── SKILL.md
│   ├── decompose-task/
│   │   └── SKILL.md
│   ├── implement-feature/
│   │   └── SKILL.md
│   ├── verify-test/
│   │   └── SKILL.md
│   ├── deploy-release/
│   │   └── SKILL.md
│   ├── monitor-operate/
│   │   └── SKILL.md
│   ├── manage-change/              # (新增)
│   │   └── SKILL.md
│   ├── review-code/                    # (新增)
│   │   └── SKILL.md
│   ├── audit-security/                 # (新增)
│   │   └── SKILL.md
│   └── review-incident/                # (新增)
│       └── SKILL.md
│
├── instructions/                  # Instruction 指令文件 (11个)
│   ├── README.md
│   ├── analyze-requirement.instructions.md
│   ├── design-system.instructions.md
│   ├── decompose-task.instructions.md
│   ├── development.instructions.md
│   ├── verify-test.instructions.md
│   ├── deploy-release.instructions.md
│   ├── monitor-operate.instructions.md
│   ├── change-management.instructions.md         # (新增)
│   ├── code-review.instructions.md               # (新增)
│   ├── security-audit.instructions.md            # (新增)
│   └── incident-review.instructions.md           # (新增)
│
├── prompts/                      # Prompt 提示词文件 (11个)
│   ├── README.md
│   ├── analyze-requirement.prompt.md
│   ├── design-system.prompt.md
│   ├── decompose-task.prompt.md
│   ├── implement-feature.prompt.md
│   ├── verify-test.prompt.md
│   ├── deploy-release.prompt.md
│   ├── monitor-operate.prompt.md
│   ├── manage-change.prompt.md                    # (新增)
│   ├── review-code.prompt.md                      # (新增)
│   ├── audit-security.prompt.md                   # (新增)
│   └── review-incident.prompt.md                  # (新增)
│
├── standards/                    # 规范文件 (5个)
│   ├── README.md
│   ├── asset-model.md
│   ├── lifecycle.md
│   ├── naming-conventions.md
│   ├── output-quality-rubric.md
│   └── authoring-checklist.md
│
├── templates/                     # 模板文件 (4个)
│   ├── README.md
│   ├── agent-template.agent.md
│   ├── instruction-template.instructions.md
│   ├── prompt-template.prompt.md
│   └── skill-template/
│       └── SKILL.md
│
└── evaluations/                  # Evaluation 评估文件 (4个)
    ├── README.md
    ├── regression-checklist.md
    ├── scorecard-template.md
    ├── output-validation-checklist.md      # (新增) 输出验证清单
    └── common-error-patterns.md           # (新增) 常见错误模式
```

---

## 快速开始

### AI Agent 执行流程

```
1. 选择 Scenario (场景入口)
   │  阅读 Chain of Thought + Error Handling
   ↓
2. 加载 Prompt (执行脚本)
   │  确认变量定义
   ↓
3. 填充变量 (Variables)
   │  准备输入数据
   ↓
4. 按 Chain of Thought 逐步执行
   │  [THINK] 思考
   │  [VALIDATE] 验证
   ↓
5. 遇到异常 → 执行 Error Handling
   │  处理不了 → 升级
   ↓
6. 完成执行 → 输出验证 (Output Validation)
   │  验证不通过 → 修复
   ↓
7. 生成 Handover Context
   │  准备交接数据
   ↓
8. 进入下一阶段
```

### 职责分离

| 资产 | 职责 | AI 阅读时机 |
|------|------|-------------|
| **Scenario** | 快速入口 + 思维链 + 错误处理 | 首先阅读 |
| **Prompt** | 完整执行逻辑 + 验证 + 交接 | 详细阅读 |
| **Instruction** | 技术规范细节 | 按需参考 |
| **Skill** | 领域知识 | 按需参考 |
| **Agent** | 角色定义 | 首先阅读 |

### 使用示例

#### 需求分析场景

```markdown
# 1. 选择场景
→ scenarios/analyze-requirement/SCENARIO.md
→ 阅读 Purpose, Chain of Thought, Error Handling

# 2. 加载 Prompt
→ prompts/analyze-requirement.prompt.md
→ 确认变量: project_name, raw_requirements, stakeholders...

# 3. 填充变量
→ 准备好项目名称和原始需求

# 4. 执行
→ 按 Chain of Thought 逐步思考
→ 遇到模糊需求 → 执行 Error Handling

# 5. 验证
→ 完成自我验证报告

# 6. 交接
→ 生成 Handover Context
→ 进入系统设计阶段
```

---

## 交付阶段与资产映射

| 阶段 | Agent | Instruction | Prompt | Skill | Scenario |
|------|-------|------------|--------|-------|----------|
| 1. 需求分析 | requirement-analyst | analyze-requirement | analyze-requirement | analyze-requirement | analyze-requirement |
| 2. 系统设计 | system-designer | design-system | design-system | design-system | design-system |
| 3. 任务拆分 | task-decomposer | decompose-task | decompose-task | decompose-task | decompose-task |
| 4. 开发实现 | developer | implement-feature | implement-feature | implement-feature | implement-feature |
| 5. 测试验证 | tester | verify-test | verify-test | verify-test | verify-test |
| 6. 部署发布 | devops-engineer | deploy-release | deploy-release | deploy-release | deploy-release |
| 7. 监控运维 | sre-monitor | monitor-operate | monitor-operate | monitor-operate | monitor-operate |

---

## 扩展场景资产映射

| 场景 | Agent | Instruction | Prompt | Skill | Scenario |
|------|-------|------------|--------|-------|----------|
| 变更管理 | change-manager | manage-change | manage-change | manage-change | manage-change |
| 代码审查 | code-reviewer | review-code | review-code | review-code | review-code |
| 安全审计 | security-auditor | audit-security | audit-security | audit-security | audit-security |
| 故障复盘 | incident-reviewer | review-incident | review-incident | review-incident | review-incident |

---

## 端到端 Pipeline

完整的 E2E 交付流程定义在 [workflows/e2e-delivery.pipeline.md](workflows/e2e-delivery.pipeline.md)

```
┌─────────────────┐
│  1. 需求分析     │  Requirement Analysis
└────────┬────────┘
         ↓
┌─────────────────┐
│  2. 系统设计     │  System Design
└────────┬────────┘
         ↓
┌─────────────────┐
│  3. 任务拆分     │  Task Decomposition
└────────┬────────┘
         ↓
┌─────────────────┐
│  4. 开发实现     │  Development
└────────┬────────┘
         ↓
┌─────────────────┐
│  5. 测试验证     │  Testing
└────────┬────────┘
         ↓
┌─────────────────┐
│  6. 部署发布     │  Deployment
└────────┬────────┘
         ↓
┌─────────────────┐
│  7. 监控运维     │  Monitoring
└─────────────────┘
```

---

## Handoff 交接规范

### 交接流程

每个阶段完成后，必须：

1. **验证产出**：确保所有交付物符合质量标准
2. **生成 Handover Context**：使用 [contexts/unified-handover-template.md](contexts/unified-handover-template.md)
3. **更新 Global Context**：记录阶段完成状态
4. **通知下游**：告知下一阶段负责人

### 交接内容

```yaml
handoff:
  artifacts:           # 交付物清单
  decisions:          # 关键决策记录
  open_issues:        # 未解决问题
  risks:              # 已知风险
  context_updates:     # 上下文更新
```

---

## 命名规范摘要

| 资产类型 | 命名模式 | 示例 |
|----------|----------|------|
| Agent | `{role}.agent.md` | `requirement-analyst.agent.md` |
| Instruction | `{phase}.instructions.md` | `analyze-requirement.instructions.md` |
| Prompt | `{action}.prompt.md` | `analyze-requirement.prompt.md` |
| Skill | `skills/{phase}/SKILL.md` | `skills/analyze-requirement/SKILL.md` |
| Scenario | `scenarios/{phase}/SCENARIO.md` | `scenarios/analyze-requirement/SCENARIO.md` |
| Pipeline | `{name}.pipeline.md` | `e2e-delivery.pipeline.md` |
| Context | `{type}-{name}.md` | `global-context.md` |

---

## 质量控制

### 阶段质量门禁

| 阶段 | 准入检查 | 准出检查 |
|------|----------|----------|
| 需求分析 | 有明确需求 | 干系人评审通过 |
| 系统设计 | 需求已确认 | 技术评审通过 |
| 任务拆分 | 设计已完成 | 计划评审通过 |
| 开发实现 | 任务已分配 | 代码审查通过 |
| 测试验证 | 开发已完成 | 测试报告签发 |
| 部署发布 | 测试已通过 | 部署验证通过 |
| 监控运维 | 应用已上线 | 监控配置完成 |

### 评估工具

- **regression-checklist.md**: 每个阶段的详细检查清单
- **scorecard-template.md**: 质量评分卡模板

---

## 维护指南

### 添加新资产

1. 选择适当的目录
2. 复制对应模板
3. 遵循命名规范
4. 包含 YAML 元数据头
5. 按 Asset Model 填充内容
6. 更新相关引用

### 扩展新阶段

1. 在 `standards/lifecycle.md` 添加阶段定义
2. 创建目录：`agents/`, `instructions/`, `prompts/`, `skills/`, `scenarios/`
3. 创建资产文件
4. 在 `workflows/e2e-delivery.pipeline.md` 添加阶段
5. 更新本 AGENTS.md

---

## 参考文档

- [Workflows](workflows/) - 端到端工作流定义
- [Contexts](contexts/) - 共享上下文管理
- [Scenarios](scenarios/) - 场景定义和使用指南
- [Standards](standards/) - 资产模型和编写规范
- [USAGE.zh.md](USAGE.zh.md) - 中文使用指南
