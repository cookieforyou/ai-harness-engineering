---
name: e2e-delivery
type: pipeline
version: "1.1.0"
description: 端到端交付全流程，覆盖从需求分析到监控运维的完整生命周期
stages:
  - analyze-requirement
  - design-system
  - decompose-task
  - implement-feature
  - verify-test
  - deploy-release
  - monitor-operate
---

# E2E Delivery Pipeline

## Overview

端到端交付全流程定义，涵盖软件交付的完整生命周期，确保每个阶段都有明确的输入、输出和质量标准。

## Stage Flow

```
┌─────────────────┐
│  1. 需求分析    │  Analyze Requirement
└────────┬────────┘
         ↓
┌─────────────────┐
│  2. 系统设计     │  Design System
└────────┬────────┘
         ↓
┌─────────────────┐
│  3. 任务拆分     │  Decompose Task
└────────┬────────┘
         ↓
┌─────────────────┐
│  4. 开发实现     │  Implement Feature
└────────┬────────┘
         ↓
┌─────────────────┐
│  5. 测试验证     │  Verify Test
└────────┬────────┘
         ↓
┌─────────────────┐
│  6. 部署发布     │  Deploy Release
└────────┬────────┘
         ↓
┌─────────────────┐
│  7. 监控运维     │  Monitor Operate
└─────────────────┘
```

## Stage Definitions

### Stage 1: 需求分析 (Analyze Requirement)

| 属性 | 值 |
|------|-----|
| **Scenario** | [analyze-requirement](../scenarios/analyze-requirement/SCENARIO.md) |
| **Agent** | [requirement-analyst](../agents/requirement-analyst.agent.md) |
| **Prompt** | [analyze-requirement](../prompts/analyze-requirement.prompt.md) |
| **Instruction** | [analyze-requirement](../instructions/analyze-requirement.instructions.md) |
| **Skill** | [analyze-requirement](../skills/analyze-requirement/SKILL.md) |
| **Entry Criteria** | 业务方提出需求请求 |
| **Exit Criteria** | 需求规格说明书已评审通过 |

**输入**：
- 原始业务需求
- 项目背景信息
- 干系人联系方式

**输出**：
- 需求规格说明书
- 干系人分析报告
- 用例模型

**数据传递到下一阶段**：
```yaml
handoff:
  to: design-system
  artifacts:
    - requirements-spec.md
    - stakeholder-analysis.md
    - use-case-model.md
  context:
    project_name: "{{project_name}}"
    key_stakeholders: ["{{stakeholder_list}}"]
    priority_requirements: ["{{top_requirements}}"]
```

---

### Stage 2: 系统设计 (Design System)

| 属性 | 值 |
|------|-----|
| **Scenario** | [design-system](../scenarios/design-system/SCENARIO.md) |
| **Agent** | [system-designer](../agents/system-designer.agent.md) |
| **Prompt** | [design-system](../prompts/design-system.prompt.md) |
| **Instruction** | [design-system](../instructions/design-system.instructions.md) |
| **Skill** | [design-system](../skills/design-system/SKILL.md) |
| **Entry Criteria** | 需求规格说明书已确认 |
| **Exit Criteria** | 架构设计评审通过 |

**输入**：
- 需求规格说明书
- 技术约束条件
- 团队能力信息

**输出**：
- 架构设计文档
- 组件设计文档
- 接口设计文档

**数据传递到下一阶段**：
```yaml
handoff:
  to: decompose-task
  artifacts:
    - architecture-design.md
    - component-design.md
    - api-spec.md
  context:
    tech_stack: ["{{tech_list}}"]
    key_components: ["{{component_list}}"]
```

---

### Stage 3: 任务拆分 (Decompose Task)

| 属性 | 值 |
|------|-----|
| **Scenario** | [decompose-task](../scenarios/decompose-task/SCENARIO.md) |
| **Agent** | [task-decomposer](../agents/task-decomposer.agent.md) |
| **Prompt** | [decompose-task](../prompts/decompose-task.prompt.md) |
| **Instruction** | [decompose-task](../instructions/decompose-task.instructions.md) |
| **Skill** | [decompose-task](../skills/decompose-task/SKILL.md) |
| **Entry Criteria** | 架构设计已完成 |
| **Exit Criteria** | 迭代计划已评审通过 |

**输入**：
- 架构设计文档
- 团队资源配置
- 交付时间约束

**输出**：
- 任务分解清单
- 迭代计划
- 工作量估算

**数据传递到下一阶段**：
```yaml
handoff:
  to: implement-feature
  artifacts:
    - task-backlog.md
    - iteration-plan.md
    - effort-estimation.md
  context:
    sprint_duration: "{{sprint_weeks}} weeks"
    team_capacity: "{{team_capacity}}"
```

---

### Stage 4: 开发实现 (Implement Feature)

| 属性 | 值 |
|------|-----|
| **Scenario** | [implement-feature](../scenarios/implement-feature/SCENARIO.md) |
| **Agent** | [developer](../agents/developer.agent.md) |
| **Prompt** | [implement-feature](../prompts/implement-feature.prompt.md) |
| **Instruction** | [implement-feature](../instructions/implement-feature.instructions.md) |
| **Skill** | [implement-feature](../skills/implement-feature/SKILL.md) |
| **Entry Criteria** | 任务已分配 |
| **Exit Criteria** | 代码审查通过，单元测试通过 |

**输入**：
- 任务分解清单
- 技术规范
- 编码标准

**输出**：
- 源代码
- 单元测试代码
- 技术文档

**数据传递到下一阶段**：
```yaml
handoff:
  to: verify-test
  artifacts:
    - source-code/
    - unit-test-report.md
    - technical-docs/
  context:
    build_instructions: "{{build_steps}}"
    test_credentials: "{{test_accounts}}"
```

---

### Stage 5: 测试验证 (Verify Test)

| 属性 | 值 |
|------|-----|
| **Scenario** | [verify-test](../scenarios/verify-test/SCENARIO.md) |
| **Agent** | [tester](../agents/tester.agent.md) |
| **Prompt** | [verify-test](../prompts/verify-test.prompt.md) |
| **Instruction** | [verify-test](../instructions/verify-test.instructions.md) |
| **Skill** | [verify-test](../skills/verify-test/SKILL.md) |
| **Entry Criteria** | 代码开发完成 |
| **Exit Criteria** | 测试通过率 ≥ 90% |

**输入**：
- 源代码
- 需求规格说明书
- 测试计划

**输出**：
- 测试用例
- 测试报告
- 缺陷报告

**数据传递到下一阶段**：
```yaml
handoff:
  to: deploy-release
  artifacts:
    - test-report.md
    - defect-list.md
    - test-sign-off.md
  context:
    test_pass_rate: "{{pass_rate}}%"
    critical_defects: ["{{critical_bugs}}"]
```

---

### Stage 6: 部署发布 (Deploy Release)

| 属性 | 值 |
|------|-----|
| **Scenario** | [deploy-release](../scenarios/deploy-release/SCENARIO.md) |
| **Agent** | [devops-engineer](../agents/devops-engineer.agent.md) |
| **Prompt** | [deploy-release](../prompts/deploy-release.prompt.md) |
| **Instruction** | [deploy-release](../instructions/deploy-release.instructions.md) |
| **Skill** | [deploy-release](../skills/deploy-release/SKILL.md) |
| **Entry Criteria** | 测试验证已通过 |
| **Exit Criteria** | 部署成功，SLO 达成 |

**输入**：
- 部署包
- 部署环境信息
- 回滚方案

**输出**：
- 部署记录
- 回滚脚本
- 发布报告

**数据传递到下一阶段**：
```yaml
handoff:
  to: monitor-operate
  artifacts:
    - deployment-record.md
    - rollback-script.sh
    - release-notes.md
  context:
    deployed_version: "{{version}}"
    deployment_time: "{{timestamp}}"
```

---

### Stage 7: 监控运维 (Monitor Operate)

| 属性 | 值 |
|------|-----|
| **Scenario** | [monitor-operate](../scenarios/monitor-operate/SCENARIO.md) |
| **Agent** | [sre-monitor](../agents/sre-monitor.agent.md) |
| **Prompt** | [monitor-operate](../prompts/monitor-operate.prompt.md) |
| **Instruction** | [monitor-operate](../instructions/monitor-operate.instructions.md) |
| **Skill** | [monitor-operate](../skills/monitor-operate/SKILL.md) |
| **Entry Criteria** | 系统已部署上线 |
| **Exit Criteria** | SLO 达成率 ≥ 99.5% |

**输入**：
- 系统架构文档
- SLO 目标
- 监控工具

**输出**：
- 监控配置
- 告警规则
- 运维手册

---

## Quality Gates

每个阶段之间的质量门禁：

| 阶段 | 质量门禁 | 标准 |
|------|----------|------|
| 需求分析 → 系统设计 | 需求完整性 | REQ-COVER ≥ 95% |
| 系统设计 → 任务拆分 | 设计评审通过 | 评审通过率 100% |
| 任务拆分 → 开发实现 | 任务覆盖率 | TASK-COVER ≥ 98% |
| 开发实现 → 测试验证 | 代码质量 | DEV-COVERAGE ≥ 80% |
| 测试验证 → 部署发布 | 测试通过率 | TEST-PASS ≥ 90% |
| 部署发布 → 监控运维 | 部署成功率 | DEPLOY-SUCCESS ≥ 99% |

## Handoff Context

阶段间的上下文传递标准：

```yaml
handoff_context:
  header:
    from_stage: "{{source_stage}}"
    to_stage: "{{target_stage}}"
    timestamp: "{{ISO8601_timestamp}}"
    handover_id: "{{handover_id}}"

  artifacts:
    documents: []
    files: []
    configurations: []

  context:
    key_decisions: []
    open_issues: []
    risks: []
    assumptions: []

  quality_metrics:
    metrics: {}
```
