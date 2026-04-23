# E2E Delivery Harness - AGENTS.md

## 项目概览

**项目名称**: E2E Delivery Harness (端到端交付全流程工作流资产库)

**项目描述**: 基于 AI Harness Engineering 理念设计的模块化交付全流程资产库，覆盖从需求分析到监控运维的完整生命周期，为 AI Agent 提供标准化的执行框架。

**核心目标**: 通过标准化的资产组合（Agent + Skill + Instruction + Prompt），实现交付流程的一致性、可复用性和高质量。

---

## 项目结构

```
e2e-delivery-harness/
├── README.md                    # 项目总说明
├── INTRODUCTION.zh.md           # 中文介绍
├── USAGE.zh.md                  # 中文使用指南
│
├── standards/                    # 规范文件 (5个)
│   ├── asset-model.md           # 资产模型规范
│   ├── lifecycle.md            # 生命周期规范
│   ├── naming-conventions.md    # 命名规范
│   ├── output-quality-rubric.md # 输出质量标准
│   └── authoring-checklist.md   # 编写检查清单
│
├── templates/                    # 模板文件 (4个)
│   ├── agent-template.md        # Agent 模板
│   ├── skill-template.md        # Skill 模板
│   ├── instruction-template.md  # Instruction 模板
│   └── prompt-template.md       # Prompt 模板
│
├── agents/                       # Agent 角色定义 (7个)
│   ├── requirement-analyst.agent.md
│   ├── system-designer.agent.md
│   ├── task-decomposer.agent.md
│   ├── developer.agent.md
│   ├── tester.agent.md
│   ├── devops-engineer.agent.md
│   └── sre-monitor.agent.md
│
├── instructions/                # Instruction 指令文件 (7个)
│   ├── requirement-analysis.instructions.md
│   ├── system-design.instructions.md
│   ├── task-decomposition.instructions.md
│   ├── development.impl.instructions.md
│   ├── testing-verification.instructions.md
│   ├── deployment-release.instructions.md
│   └── monitoring-operations.instructions.md
│
├── prompts/                     # Prompt 提示词文件 (7个)
│   ├── analyze-requirement.prompt.md
│   ├── design-system.prompt.md
│   ├── decompose-task.prompt.md
│   ├── implement-feature.prompt.md
│   ├── verify-test.prompt.md
│   ├── deploy-release.prompt.md
│   └── monitor-operate.prompt.md
│
├── skills/                       # Skill 技能模块 (7个)
│   ├── requirement-analysis/
│   ├── system-design/
│   ├── task-decomposition/
│   ├── development/
│   ├── testing/
│   ├── deployment/
│   └── monitoring/
│
├── scenarios/                    # Scenario 场景定义 (7个)
│   ├── requirement-analysis/
│   ├── system-design/
│   ├── task-decomposition/
│   ├── development/
│   ├── testing/
│   ├── deployment/
│   └── monitoring/
│
└── evaluations/                 # Evaluation 评估文件 (2个)
    ├── regression-checklist.md
    └── scorecard-template.md
```

---

## 交付阶段与资产映射

| 阶段 | Agent | Instruction | Prompt | Skill | Scenario |
|------|-------|------------|--------|-------|----------|
| 1. 需求分析 | requirement-analyst | requirement-analysis | analyze-requirement | requirement-analysis | requirement-analysis |
| 2. 系统设计 | system-designer | system-design | design-system | system-design | system-design |
| 3. 任务拆分 | task-decomposer | task-decomposition | decompose-task | task-decomposition | task-decomposition |
| 4. 开发实现 | developer | development.impl | implement-feature | development | development |
| 5. 测试验证 | tester | testing-verification | verify-test | testing | testing |
| 6. 部署发布 | devops-engineer | deployment-release | deploy-release | deployment | deployment |
| 7. 监控运维 | sre-monitor | monitoring-operations | monitor-operate | monitoring | monitoring |

---

## Handoff 交接规范

### 阶段间产出传递

每个阶段完成后，必须向下一个阶段传递以下产出：

```
Requirement Analysis → System Design:
  - 需求规格说明书
  - 干系人分析表
  - 用例模型

System Design → Task Decomposition:
  - 架构设计文档
  - 组件设计文档
  - 接口设计文档

Task Decomposition → Development:
  - 任务分解清单
  - 迭代计划
  - 工作量估算

Development → Testing:
  - 源代码
  - 单元测试代码
  - 测试报告

Testing → Deployment:
  - 测试通过报告
  - 部署包
  - 变更清单

Deployment → Monitoring:
  - 部署报告
  - 配置清单
  - 监控需求
```

### 交接检查清单

- [ ] 产出文档齐全
- [ ] 文档格式符合规范
- [ ] 干系人评审通过
- [ ] 遗留问题已记录
- [ ] 下游阶段已确认接收

---

## 命名规范

### 文件命名

| 资产类型 | 命名模式 | 示例 |
|----------|----------|------|
| Agent | `{role}.agent.md` | `requirement-analyst.agent.md` |
| Instruction | `{phase}.instructions.md` | `requirement-analysis.instructions.md` |
| Prompt | `{action}.prompt.md` | `analyze-requirement.prompt.md` |
| Skill | `skills/{phase}/SKILL.md` | `skills/requirement-analysis/SKILL.md` |
| Scenario | `scenarios/{phase}/SCENARIO.md` | `scenarios/requirement-analysis/SCENARIO.md` |
| Standard | `{topic}.md` | `asset-model.md` |
| Template | `{type}-template.md` | `agent-template.md` |
| Evaluation | `{type}.md` | `regression-checklist.md` |

### 目录命名

- 所有目录名使用**小写字母 + 连字符 (-)**
- 复数形式使用单数（避免复数）
- 场景目录：`scenarios/{phase-name}/`
- 技能目录：`skills/{phase-name}/`

---

## 质量控制

### 阶段质量门禁

每个阶段在准出前必须通过质量门禁：

| 阶段 | 质量门禁检查项 |
|------|----------------|
| 需求分析 | 需求完整性 > 95%，干系人评审通过 |
| 系统设计 | 需求覆盖率 100%，技术评审通过 |
| 任务拆分 | 任务粒度 90% 在 1-3 天，依赖关系清晰 |
| 开发实现 | 代码规范合规 100%，单元测试通过 |
| 测试验证 | 用例执行率 > 95%，缺陷修复率 > 95% |
| 部署发布 | 部署成功率 100%，验证检查通过 |
| 监控运维 | 系统可用率 > 99.9%，告警响应 < 5 分钟 |

### 评估工具

- **regression-checklist.md**: 每个阶段的详细检查清单
- **scorecard-template.md**: 质量评分卡模板

---

## 快速开始

### 1. 选择场景

根据当前任务类型，选择对应的场景目录。

### 2. 加载资产组合

按顺序加载该场景的四类资产：

```
1. Agent (角色定义)
2. Skill (技能模块)
3. Instruction (指令指导)
4. Prompt (提示词生成)
```

### 3. 执行并产出

按照 Instruction 的指导，使用 Prompt 生成提示词，调用 Skill 执行任务。

### 4. 质量检查

完成后使用 `evaluations/regression-checklist.md` 进行自检。

---

## 维护指南

### 添加新资产

1. 遵循命名规范
2. 包含 YAML 元数据头
3. 更新本 AGENTS.md 的资产映射表
4. 添加到对应的 Scenario

### 更新现有资产

1. 更新版本号
2. 记录变更日志
3. 通知相关干系人
4. 重新执行质量检查

### 扩展新阶段

1. 在 `standards/lifecycle.md` 添加阶段定义
2. 创建对应目录（agents, instructions, prompts, skills, scenarios）
3. 创建资产文件
4. 更新本 AGENTS.md

---

## 参考文档

- [Standards/asset-model.md](standards/asset-model.md) - 资产模型详解
- [Standards/lifecycle.md](standards/lifecycle.md) - 生命周期定义
- [Standards/naming-conventions.md](standards/naming-conventions.md) - 命名规范
- [USAGE.zh.md](USAGE.zh.md) - 中文使用指南
