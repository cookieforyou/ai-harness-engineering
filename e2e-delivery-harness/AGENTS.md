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
├── scenarios/                    # 场景定义 (37个) ← AI 主要入口
│   ├── README.md               # 场景使用指南
│   ├── analyze-requirement/    # 需求分析场景
│   │   └── SCENARIO.md
│   ├── design-system/          # 系统设计场景
│   │   └── SCENARIO.md
│   ├── decompose-task/         # 任务拆分场景
│   │   └── SCENARIO.md
│   ├── implement-feature/      # 开发实现场景
│   │   └── SCENARIO.md
│   ├── verify-test/            # 测试验证场景
│   │   └── SCENARIO.md
│   ├── deploy-release/         # 部署发布场景
│   │   └── SCENARIO.md
│   ├── monitor-operate/        # 监控运维场景
│   │   └── SCENARIO.md
│   ├── manage-change/          # 变更管理场景 (扩展)
│   │   └── SCENARIO.md
│   ├── review-code/            # 代码审查场景 (扩展)
│   │   └── SCENARIO.md
│   ├── audit-security/         # 安全审计场景 (扩展)
│   │   └── SCENARIO.md
│   ├── review-incident/        # 故障复盘场景 (扩展)
│   │   └── SCENARIO.md
│   ├── performance-testing/    # 性能测试场景 (扩展)
│   │   └── SCENARIO.md
│   ├── migrate-data/           # 数据迁移场景 (扩展)
│   │   └── SCENARIO.md
│   ├── hotfix/                # 紧急修复场景 (扩展)
│   │   └── SCENARIO.md
│   ├── review-design/          # 技术方案评审场景 (扩展)
│   │   └── SCENARIO.md
│   ├── plan-capacity/         # 容量规划场景 (扩展)
│   │   └── SCENARIO.md
│   ├── automate-test/         # 自动化测试场景 (扩展)
│   │   └── SCENARIO.md
│   ├── setup-infra/           # 基础设施搭建场景 (扩展)
│   │   └── SCENARIO.md
│   ├── manage-config/         # 配置管理场景 (扩展)
│   │   └── SCENARIO.md
│   ├── prepare-release/       # 发布准备场景 (扩展)
│   │   └── SCENARIO.md
│   ├── backup-data/           # 数据备份场景 (扩展)
│   │   └── SCENARIO.md
│   ├── integrate-api/         # API 集成场景 (扩展)
│   │   └── SCENARIO.md
│   ├── design-database/       # 数据库设计场景 (扩展)
│   │   └── SCENARIO.md
│   ├── implement-cicd/        # CI/CD 实施场景 (扩展)
│   │   └── SCENARIO.md
│   ├── manage-secrets/        # 密钥管理场景 (扩展)
│   │   └── SCENARIO.md
│   ├── design-architecture/   # 架构设计场景 (扩展)
│   │   └── SCENARIO.md
│   ├── optimize-performance/  # 性能优化场景 (扩展)
│   │   └── SCENARIO.md
│   ├── migrate-environment/   # 环境迁移场景 (扩展)
│   │   └── SCENARIO.md
│   ├── plan-sprint/           # 冲刺规划场景 (扩展)
│   │   └── SCENARIO.md
│   ├── document-project/      # 项目文档场景 (扩展)
│   │   └── SCENARIO.md
│   └── integrate-monitor/     # 监控集成场景 (扩展)
│       └── SCENARIO.md
│   ├── manage-dependencies/   # 依赖管理场景 (扩展)
│   │   └── SCENARIO.md
│   ├── manage-tech-debt/      # 技术债务场景 (扩展)
│   │   └── SCENARIO.md
│   ├── plan-rollback/         # 回滚计划场景 (扩展)
│   │   └── SCENARIO.md
│   ├── respond-incident/      # 事件响应场景 (扩展)
│   │   └── SCENARIO.md
│   ├── plan-disaster-recovery/ # 灾备恢复场景 (扩展)
│   │   └── SCENARIO.md
│   └── manage-knowledge/       # 知识管理场景 (扩展)
│       └── SCENARIO.md
│
├── agents/                       # Agent 角色定义 (37个)
│   ├── analyze-requirement.agent.md
│   ├── design-system.agent.md
│   ├── decompose-task.agent.md
│   ├── implement-feature.agent.md
│   ├── verify-test.agent.md
│   ├── deploy-release.agent.md
│   ├── monitor-operate.agent.md
│   ├── manage-change.agent.md
│   ├── review-code.agent.md
│   ├── audit-security.agent.md
│   ├── review-incident.agent.md
│   ├── performance-testing.agent.md
│   ├── migrate-data.agent.md
│   ├── hotfix.agent.md
│   ├── review-design.agent.md
│   ├── plan-capacity.agent.md
│   ├── automate-test.agent.md
│   ├── setup-infra.agent.md
│   ├── manage-config.agent.md
│   ├── prepare-release.agent.md
│   ├── backup-data.agent.md
│   ├── integrate-api.agent.md      # (新增)
│   ├── design-database.agent.md    # (新增)
│   ├── implement-cicd.agent.md     # (新增)
│   ├── manage-secrets.agent.md     # (新增)
│   ├── design-architecture.agent.md # (新增)
│   ├── optimize-performance.agent.md # (新增)
│   ├── migrate-environment.agent.md # (新增)
│   ├── plan-sprint.agent.md        # (新增)
│   ├── document-project.agent.md   # (新增)
│   ├── integrate-monitor.agent.md  # (新增)
│   ├── manage-dependencies.agent.md
│   ├── manage-tech-debt.agent.md
│   ├── plan-rollback.agent.md
│   ├── respond-incident.agent.md
│   ├── plan-disaster-recovery.agent.md
│   └── manage-knowledge.agent.md
│
├── skills/                       # Skill 技能模块 (37个)
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
│   ├── manage-change/
│   │   └── SKILL.md
│   ├── review-code/
│   │   └── SKILL.md
│   ├── audit-security/
│   │   └── SKILL.md
│   ├── review-incident/
│   │   └── SKILL.md
│   ├── performance-testing/
│   │   └── SKILL.md
│   ├── migrate-data/
│   │   └── SKILL.md
│   ├── hotfix/
│   │   └── SKILL.md
│   ├── review-design/
│   │   └── SKILL.md
│   ├── plan-capacity/
│   │   └── SKILL.md
│   ├── automate-test/              # (扩展)
│   │   └── SKILL.md
│   ├── setup-infra/               # (扩展)
│   │   └── SKILL.md
│   ├── manage-config/              # (扩展)
│   │   └── SKILL.md
│   ├── prepare-release/            # (扩展)
│   │   └── SKILL.md
│   ├── backup-data/                # (扩展)
│   │   └── SKILL.md
│   ├── integrate-api/              # (扩展)
│   │   └── SKILL.md
│   ├── design-database/            # (扩展)
│   │   └── SKILL.md
│   ├── implement-cicd/             # (扩展)
│   │   └── SKILL.md
│   ├── manage-secrets/             # (扩展)
│   │   └── SKILL.md
│   ├── design-architecture/       # (扩展)
│   │   └── SKILL.md
│   ├── optimize-performance/        # (扩展)
│   │   └── SKILL.md
│   ├── migrate-environment/         # (扩展)
│   │   └── SKILL.md
│   ├── plan-sprint/                # (扩展)
│   │   └── SKILL.md
│   ├── document-project/            # (扩展)
│   │   └── SKILL.md
│   ├── integrate-monitor/          # (扩展)
│   │   └── SKILL.md
│   ├── manage-dependencies/       # (扩展)
│   │   └── SKILL.md
│   ├── manage-tech-debt/          # (扩展)
│   │   └── SKILL.md
│   ├── plan-rollback/             # (扩展)
│   │   └── SKILL.md
│   ├── respond-incident/          # (扩展)
│   │   └── SKILL.md
│   ├── plan-disaster-recovery/    # (扩展)
│   │   └── SKILL.md
│   └── manage-knowledge/           # (扩展)
│       └── SKILL.md
│
├── instructions/                  # Instruction 指令文件 (37个)
│   ├── README.md
│   ├── analyze-requirement.instructions.md
│   ├── design-system.instructions.md
│   ├── decompose-task.instructions.md
│   ├── implement-feature.instructions.md
│   ├── verify-test.instructions.md
│   ├── deploy-release.instructions.md
│   ├── monitor-operate.instructions.md
│   ├── manage-change.instructions.md
│   ├── review-code.instructions.md
│   ├── audit-security.instructions.md
│   ├── review-incident.instructions.md
│   ├── performance-testing.instructions.md
│   ├── migrate-data.instructions.md
│   ├── hotfix.instructions.md
│   ├── review-design.instructions.md
│   ├── plan-capacity.instructions.md
│   ├── automate-test.instructions.md
│   ├── setup-infra.instructions.md
│   ├── manage-config.instructions.md
│   ├── prepare-release.instructions.md
│   ├── backup-data.instructions.md
│   ├── integrate-api.instructions.md    # (新增)
│   ├── design-database.instructions.md  # (新增)
│   ├── implement-cicd.instructions.md   # (新增)
│   ├── manage-secrets.instructions.md  # (新增)
│   ├── design-architecture.instructions.md # (新增)
│   ├── optimize-performance.instructions.md  # (新增)
│   ├── migrate-environment.instructions.md   # (新增)
│   ├── plan-sprint.instructions.md      # (新增)
│   ├── document-project.instructions.md # (新增)
│   └── integrate-monitor.instructions.md # (新增)
│   ├── manage-dependencies.instructions.md  # (新增)
│   ├── manage-tech-debt.instructions.md     # (新增)
│   ├── plan-rollback.instructions.md        # (新增)
│   ├── respond-incident.instructions.md
│   ├── plan-disaster-recovery.instructions.md
│   └── manage-knowledge.instructions.md
│
├── prompts/                      # Prompt 提示词文件 (37个)
│   ├── README.md
│   ├── analyze-requirement.prompt.md
│   ├── design-system.prompt.md
│   ├── decompose-task.prompt.md
│   ├── implement-feature.prompt.md
│   ├── verify-test.prompt.md
│   ├── deploy-release.prompt.md
│   ├── monitor-operate.prompt.md
│   ├── manage-change.prompt.md
│   ├── review-code.prompt.md
│   ├── audit-security.prompt.md
│   ├── review-incident.prompt.md
│   ├── performance-testing.prompt.md
│   ├── migrate-data.prompt.md
│   ├── hotfix.prompt.md
│   ├── review-design.prompt.md
│   ├── plan-capacity.prompt.md
│   ├── automate-test.prompt.md
│   ├── setup-infra.prompt.md
│   ├── manage-config.prompt.md
│   ├── prepare-release.prompt.md
│   ├── backup-data.prompt.md
│   ├── integrate-api.prompt.md
│   ├── design-database.prompt.md
│   ├── implement-cicd.prompt.md
│   ├── manage-secrets.prompt.md
│   ├── design-architecture.prompt.md
│   ├── optimize-performance.prompt.md
│   ├── migrate-environment.prompt.md
│   ├── plan-sprint.prompt.md
│   ├── document-project.prompt.md
│   ├── integrate-monitor.prompt.md
│   ├── manage-dependencies.prompt.md
│   ├── manage-tech-debt.prompt.md
│   ├── plan-rollback.prompt.md
│   ├── respond-incident.prompt.md
│   ├── plan-disaster-recovery.prompt.md
│   └── manage-knowledge.prompt.md
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

## E2E Delivery Phase Mapping (E2E 环节分组映射)

All 37 scenarios are grouped by E2E delivery phase:

### Phase 1: Requirement (需求)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 1 | analyze-requirement | analyze-requirement | Analyze and clarify requirements |
| 2 | plan-sprint | plan-sprint | Sprint planning and estimation |

### Phase 2: Design (设计)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 3 | design-system | design-system | System architecture design |
| 4 | design-architecture | design-architecture | Architecture patterns design |
| 5 | design-database | design-database | Database schema design |
| 6 | review-design | review-design | Technical design review |

### Phase 3: Development (开发)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 7 | decompose-task | decompose-task | Task decomposition and estimation |
| 8 | implement-feature | implement-feature | Feature development |
| 9 | integrate-api | integrate-api | API integration |
| 10 | manage-dependencies | manage-dependencies | Dependency management |
| 11 | manage-config | manage-config | Configuration management |
| 12 | manage-secrets | manage-secrets | Secrets and credential management |
| 13 | document-project | document-project | Project documentation |

### Phase 4: Testing (测试)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 14 | verify-test | verify-test | Test execution and verification |
| 15 | automate-test | automate-test | Automated test creation |
| 16 | performance-testing | performance-testing | Performance and load testing |
| 17 | review-code | review-code | Code review and quality gate |

### Phase 5: Deployment (部署)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 18 | setup-infra | setup-infra | Infrastructure setup |
| 19 | implement-cicd | implement-cicd | CI/CD pipeline implementation |
| 20 | prepare-release | prepare-release | Release preparation |
| 21 | deploy-release | deploy-release | Deployment and release |
| 22 | plan-rollback | plan-rollback | Rollback planning |

### Phase 6: Operations (运维)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 23 | backup-data | backup-data | Data backup and recovery |
| 24 | migrate-data | migrate-data | Data migration |
| 25 | migrate-environment | migrate-environment | Environment migration |
| 26 | monitor-operate | monitor-operate | Monitoring and alerting |
| 27 | integrate-monitor | integrate-monitor | Monitoring integration |
| 28 | manage-change | manage-change | Change management |
| 29 | optimize-performance | optimize-performance | Performance optimization |
| 30 | plan-capacity | plan-capacity | Capacity planning |

### Phase 7: Governance (治理)
| # | Scenario | Agent | Description |
|---|----------|-------|-------------|
| 31 | audit-security | audit-security | Security audit and compliance |
| 32 | manage-tech-debt | manage-tech-debt | Technical debt management |
| 33 | manage-knowledge | manage-knowledge | Knowledge management |
| 34 | respond-incident | respond-incident | Incident response |
| 35 | review-incident | review-incident | Incident postmortem review |
| 36 | plan-disaster-recovery | plan-disaster-recovery | Disaster recovery planning |
| 37 | hotfix | hotfix | Emergency hotfix deployment |

---

## Complete Asset Mapping Table

| Phase | Scenario | Agent | Instruction | Prompt | Skill |
|-------|----------|-------|------------|--------|-------|
| Requirement | analyze-requirement | analyze-requirement | analyze-requirement | analyze-requirement | analyze-requirement |
| Requirement | plan-sprint | plan-sprint | plan-sprint | plan-sprint | plan-sprint |
| Design | design-system | design-system | design-system | design-system | design-system |
| Design | design-architecture | design-architecture | design-architecture | design-architecture | design-architecture |
| Design | design-database | design-database | design-database | design-database | design-database |
| Design | review-design | review-design | review-design | review-design | review-design |
| Development | decompose-task | decompose-task | decompose-task | decompose-task | decompose-task |
| Development | implement-feature | implement-feature | implement-feature | implement-feature | implement-feature |
| Development | integrate-api | integrate-api | integrate-api | integrate-api | integrate-api |
| Development | manage-dependencies | manage-dependencies | manage-dependencies | manage-dependencies | manage-dependencies |
| Development | manage-config | manage-config | manage-config | manage-config | manage-config |
| Development | manage-secrets | manage-secrets | manage-secrets | manage-secrets | manage-secrets |
| Development | document-project | document-project | document-project | document-project | document-project |
| Testing | verify-test | verify-test | verify-test | verify-test | verify-test |
| Testing | automate-test | automate-test | automate-test | automate-test | automate-test |
| Testing | performance-testing | performance-testing | performance-testing | performance-testing | performance-testing |
| Testing | review-code | review-code | review-code | review-code | review-code |
| Deployment | setup-infra | setup-infra | setup-infra | setup-infra | setup-infra |
| Deployment | implement-cicd | implement-cicd | implement-cicd | implement-cicd | implement-cicd |
| Deployment | prepare-release | prepare-release | prepare-release | prepare-release | prepare-release |
| Deployment | deploy-release | deploy-release | deploy-release | deploy-release | deploy-release |
| Deployment | plan-rollback | plan-rollback | plan-rollback | plan-rollback | plan-rollback |
| Operations | backup-data | backup-data | backup-data | backup-data | backup-data |
| Operations | migrate-data | migrate-data | migrate-data | migrate-data | migrate-data |
| Operations | migrate-environment | migrate-environment | migrate-environment | migrate-environment | migrate-environment |
| Operations | monitor-operate | monitor-operate | monitor-operate | monitor-operate | monitor-operate |
| Operations | integrate-monitor | integrate-monitor | integrate-monitor | integrate-monitor | integrate-monitor |
| Operations | manage-change | manage-change | manage-change | manage-change | manage-change |
| Operations | optimize-performance | optimize-performance | optimize-performance | optimize-performance | optimize-performance |
| Operations | plan-capacity | plan-capacity | plan-capacity | plan-capacity | plan-capacity |
| Governance | audit-security | audit-security | audit-security | audit-security | audit-security |
| Governance | manage-tech-debt | manage-tech-debt | manage-tech-debt | manage-tech-debt | manage-tech-debt |
| Governance | manage-knowledge | manage-knowledge | manage-knowledge | manage-knowledge | manage-knowledge |
| Governance | respond-incident | respond-incident | respond-incident | respond-incident | respond-incident |
| Governance | review-incident | review-incident | review-incident | review-incident | review-incident |
| Governance | plan-disaster-recovery | plan-disaster-recovery | plan-disaster-recovery | plan-disaster-recovery | plan-disaster-recovery |
| Governance | hotfix | hotfix | hotfix | hotfix | hotfix |

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

> **核心原则**: 所有资产统一采用 `{verb}-{noun}` 命名模式

| 资产类型 | 命名模式 | 示例 |
|----------|----------|------|
| Agent | `{verb}-{noun}.agent.md` | `analyze-requirement.agent.md` |
| Instruction | `{verb}-{noun}.instructions.md` | `analyze-requirement.instructions.md` |
| Prompt | `{verb}-{noun}.prompt.md` | `analyze-requirement.prompt.md` |
| Skill | `skills/{verb}-{noun}/SKILL.md` | `skills/analyze-requirement/SKILL.md` |
| Scenario | `scenarios/{verb}-{noun}/SCENARIO.md` | `scenarios/analyze-requirement/SCENARIO.md` |
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

## References文档

- [Workflows](workflows/) - 端到端工作流定义
- [Contexts](contexts/) - 共享上下文管理
- [Scenarios](scenarios/) - 场景定义和使用指南
- [Standards](standards/) - 资产模型和编写规范
- [USAGE.zh.md](USAGE.zh.md) - 中文使用指南
