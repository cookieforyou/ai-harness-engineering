# E2E Delivery Harness - AGENTS.md

## 项目概览

**项目名称**: E2E Delivery Harness (端到端交付全流程工作流资产库)

**项目描述**: 基于 AI Harness Engineering 理念设计的模块化交付全流程资产库，覆盖从需求分析到监控运维的完整生命周期，为 AI Agent 提供标准化的执行框架。

**核心目标**: 通过标准化的资产组合（Agent + Skill + Instruction + Prompt + Scenario），实现交付流程的一致性、可复用性和高质量。

---

## 设计理念

### 核心原则

1. **AI-First**: 所有资产设计以 AI 驾驭为核心，每个 Scenario 包含 Chain of Thought 引导 AI 逐步思考
2. **Pipeline 驱动**: 通过 Workflow 定义端到端流程，确保阶段间的有序衔接
3. **Context 传递**: 通过 Handover Context 实现阶段间的数据传递和上下文继承
4. **Quality Gate**: 每个阶段都有明确的准入准出标准，确保交付质量

### 资产层级

```
Workflow (工作流层)
    ↓
Scenario (场景层) ← AI 的主要入口
    ├── Agent (角色定义)
    ├── Instruction (操作指令)
    ├── Prompt (提示词)
    └── Skills[] (技能组合)
        └── Skill (技能模块)

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
├── workflows/                   # 工作流定义 (1个)
│   ├── README.md               # 工作流说明
│   └── e2e-delivery.pipeline.md # E2E 交付全流程
│
├── contexts/                     # 共享上下文 (3个)
│   ├── README.md               # 上下文说明
│   ├── global-context.md        # 全局上下文定义
│   └── handover-context.template.md # 交接上下文模板
│
├── scenarios/                    # 场景定义 (7个) ← AI 主要入口
│   ├── README.md               # 场景使用指南
│   ├── requirement-analysis/    # 需求分析场景
│   │   └── SCENARIO.md
│   ├── system-design/          # 系统设计场景
│   │   └── SCENARIO.md
│   ├── task-decomposition/     # 任务拆分场景
│   │   └── SCENARIO.md
│   ├── development/            # 开发实现场景
│   │   └── SCENARIO.md
│   ├── testing/                # 测试验证场景
│   │   └── SCENARIO.md
│   ├── deployment/            # 部署发布场景
│   │   └── SCENARIO.md
│   └── monitoring/             # 监控运维场景
│       └── SCENARIO.md
│
├── agents/                       # Agent 角色定义 (7个)
│   ├── README.md
│   ├── requirement-analyst.agent.md
│   ├── system-designer.agent.md
│   ├── task-decomposer.agent.md
│   ├── developer.agent.md
│   ├── tester.agent.md
│   ├── devops-engineer.agent.md
│   └── sre-monitor.agent.md
│
├── skills/                       # Skill 技能模块 (7个)
│   ├── README.md
│   ├── requirement-analysis/
│   │   └── SKILL.md
│   ├── system-design/
│   │   └── SKILL.md
│   ├── task-decomposition/
│   │   └── SKILL.md
│   ├── development/
│   │   └── SKILL.md
│   ├── testing/
│   │   └── SKILL.md
│   ├── deployment/
│   │   └── SKILL.md
│   └── monitoring/
│       └── SKILL.md
│
├── instructions/                  # Instruction 指令文件 (7个)
│   ├── README.md
│   ├── requirement-analysis.instructions.md
│   ├── system-design.instructions.md
│   ├── task-decomposition.instructions.md
│   ├── development.instructions.md
│   ├── testing-verification.instructions.md
│   ├── deployment-release.instructions.md
│   └── monitoring-operations.instructions.md
│
├── prompts/                      # Prompt 提示词文件 (7个)
│   ├── README.md
│   ├── analyze-requirement.prompt.md
│   ├── design-system.prompt.md
│   ├── decompose-task.prompt.md
│   ├── implement-feature.prompt.md
│   ├── verify-test.prompt.md
│   ├── deploy-release.prompt.md
│   └── monitor-operate.prompt.md
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
└── evaluations/                  # Evaluation 评估文件 (2个)
    ├── README.md
    ├── regression-checklist.md
    └── scorecard-template.md
```

---

## 快速开始

### AI Agent 执行流程

```
1. 选择 Scenario (场景入口)
   ↓
2. 加载 Agent (角色定义)
   ↓
3. 加载 Skill (技能模块)
   ↓
4. 执行 Instruction (操作指令)
   ↓
5. 生成 Prompt (提示词)
   ↓
6. 按 Chain of Thought 逐步执行
   ↓
7. 验证输出 (Quality Gate)
   ↓
8. 生成 Handover Context
   ↓
9. 进入下一阶段
```

### 使用示例

#### 需求分析场景

```markdown
# 1. 选择场景
→ 进入 scenarios/requirement-analysis/

# 2. 阅读场景定义
→ 查看 SCENARIO.md，包含：
   - Purpose (目的)
   - Chain of Thought (思维链) ← AI 逐步思考引导
   - Primary Assets (主要资产)
   - Expected Output (预期输出)
   - Quality Gates (质量门禁)

# 3. 加载资产组合
→ Agent: agents/requirement-analyst.agent.md
→ Skill: skills/requirement-analysis/SKILL.md
→ Instruction: instructions/requirement-analysis.instructions.md
→ Prompt: prompts/analyze-requirement.prompt.md

# 4. 按思维链执行
→ THINK: 理解业务目标
→ THINK: 识别干系人和诉求
→ ...
```

---

## 交付阶段与资产映射

| 阶段 | Agent | Instruction | Prompt | Skill | Scenario |
|------|-------|------------|--------|-------|----------|
| 1. 需求分析 | requirement-analyst | requirement-analysis | analyze-requirement | requirement-analysis | requirement-analysis |
| 2. 系统设计 | system-designer | system-design | design-system | system-design | system-design |
| 3. 任务拆分 | task-decomposer | task-decomposition | decompose-task | task-decomposition | task-decomposition |
| 4. 开发实现 | developer | development | implement-feature | development | development |
| 5. 测试验证 | tester | testing-verification | verify-test | testing | testing |
| 6. 部署发布 | devops-engineer | deployment-release | deploy-release | deployment | deployment |
| 7. 监控运维 | sre-monitor | monitoring-operations | monitor-operate | monitoring | monitoring |

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
2. **生成 Handover Context**：使用 [contexts/handover-context.template.md](contexts/handover-context.template.md)
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
| Instruction | `{phase}.instructions.md` | `requirement-analysis.instructions.md` |
| Prompt | `{action}.prompt.md` | `analyze-requirement.prompt.md` |
| Skill | `skills/{phase}/SKILL.md` | `skills/requirement-analysis/SKILL.md` |
| Scenario | `scenarios/{phase}/SCENARIO.md` | `scenarios/requirement-analysis/SCENARIO.md` |
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
