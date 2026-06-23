---
name: version-compatibility-matrix
description: "资产间接口契约定义和版本兼容性矩阵，规范变量↔工具↔输出的接口约定和语义化版本升级影响分析"
type: standard
version: "2.0.0"
author: AI Harness Engineering Team
created: 2026-06-23
updated: 2026-06-23
status: active
language: "zh-CN"
tags: ['standard', 'versioning', 'compatibility', 'contract', 'semver']
---

# 资产版本兼容性矩阵

## 概述

本文件定义了 E2E Delivery Harness 五类执行资产之间的**接口契约**和**版本兼容性规则**。通过显式定义资产间的输入/输出契约和版本依赖关系，确保资产升级时不会破坏下游兼容性。

## 资产接口契约

### 契约维度

每个资产组合（Scenario + Agent + Prompt + Instruction + Skill）存在以下接口契约：

```yaml
asset_contract:
  scenario:
    provides: ["purpose", "cot_steps", "decision_checkpoints", "kpi_definitions", "handover_template"]
    consumes: ["pipeline_stage_order", "from_stage_artifacts"]
    
  agent:
    provides: ["role_definition", "working_rules", "io_schema", "quality_checklist"]
    consumes: ["scenario.cot_steps", "scenario.decision_checkpoints", "prompt.variables"]
    
  prompt:
    provides: ["input_variables", "cot_detail", "output_template", "handover_yaml"]
    consumes: ["scenario.purpose", "agent.working_rules", "instruction.steps"]
    
  instruction:
    provides: ["technical_steps", "tool_commands", "quality_standards"]
    consumes: ["scenario.decision_checkpoints", "prompt.variables", "skill.best_practices"]
    
  skill:
    provides: ["domain_knowledge", "best_practices", "anti_patterns", "code_examples"]
    consumes: []  # Skill 是最底层资产，不依赖其他资产
```

### 变量 → 工具 → 输出契约

```yaml
contract_example_deploy_release:
  # Prompt 声明的输入变量
  input_contract:
    variables:
      - name: "target_environment"
        type: "enum [prod, staging, dev]"
        required: true
        consumed_by: ["agent.working_process.step_2", "instruction.step_4"]
        
  # Agent 声明可用的工具
  tool_contract:
    tools:
      - name: "deploy"
        capabilities: ["kubectl_apply", "helm_install", "terraform_apply"]
        constraints: ["需生产环境访问权限", "部署前需审批"]
        
  # 期望的输出格式
  output_contract:
    artifacts:
      - name: "deployment_log"
        format: "YAML"
        schema: "{timestamp, step, status, duration, error}"
        consumed_by: "monitor-operate.handover"
```

## 语义化版本规范

### 版本号格式

```
MAJOR.MINOR.PATCH
  ↑     ↑     ↑
  │     │     └─ PATCH: 向后兼容的修复（错字、小改进、Bug修复）
  │     └─────── MINOR: 向后兼容的新增（新章节、新字段、增强内容）
  └───────────── MAJOR: 不兼容的变更（删除字段、重命名、契约变更）
```

### 变更影响矩阵

| 变更类型 | 版本增量 | 影响范围 | 需要同步的资产 |
|---------|---------|---------|-------------|
| 修正错字/格式 | PATCH | 无 | 无 |
| 增加 KPI | MINOR | Scenario.quality_metrics | Prompt.output_validation |
| 增加 CoT 步骤 | MINOR | Scenario.cot | Agent.working_process, Prompt.cot |
| 新增可选变量 | MINOR | Prompt.variables | Agent.io_schema |
| 新增必填变量 | MINOR | Prompt.variables | Agent.io_schema, Instruction.steps |
| 删除 KPI | MAJOR | Scenario.quality_metrics | Prompt, Agent, Handover Template |
| 重命名 stage ID | MAJOR | Scenario, Agent, Pipeline | 所有引用该 stage 的资产 |
| 变更 Handover YAML 字段 | MAJOR | 所有 Handoff 段 | 上下游 Agent |
| 删除 CoT 步骤 | MAJOR | Scenario, Prompt | Agent.working_process |
| 删除必填变量 | MAJOR | Prompt | Agent, Instruction |

## 跨资产兼容性检查清单

### 升级 Scenario 时的检查

```yaml
scenario_upgrade_checklist:
  - check: "新增的 DC-* 是否在 Agent.decision_criteria 中有对应行？"
  - check: "新增的 KPI 是否在 Prompt.output_validation 中有验证项？"
  - check: "Handover 字段变更是否与 unified-handover-template.md 对齐？"
  - check: "CoT 步骤变更是否更新了 Agent.working_process？"
  - check: "Error Handling 场景是否在 Prompt.error_handling 中有对应？"
```

### 升级 Prompt 时的检查

```yaml
prompt_upgrade_checklist:
  - check: "新增的 Required=true 变量是否在 Agent.expected_input 中有定义？"
  - check: "变更的输出模板是否更新了对应的 Template 文件？"
  - check: "CoT 步骤是否与 Scenario.cot 映射一致？"
  - check: "变量 Schema 是否满足 variable-schema-standard.md？"
```

### 升级 Agent 时的检查

```yaml
agent_upgrade_checklist:
  - check: "Working Rules 是否引用了最新的 Scenario.decision_checkpoints？"
  - check: "I/O Schema 是否与 Prompt.variables 一致？"
  - check: "Handoff YAML 字段是否与 unified-handover-template.md 兼容？"
  - check: "Quality Checklist 是否覆盖了所有 Scenario.KPIs？"
```

## 版本依赖锁定

```yaml
version_lock:
  core_7_scenarios:
    analyze-requirement:
      locked_versions:
        agent: ">=1.2.0"
        prompt: ">=1.2.0"
        instruction: ">=1.2.0"
        skill: ">=1.2.0"
        
  pipeline_contract:
    e2e_delivery:
      version: "1.1.0"
      compatible_scenario_versions: ">=1.2.0"
      compatible_handover_format: "v2"
      
  standards_contract:
    cot_framework: ">=2.0.0"
    error_classification: ">=2.0.0"
    variable_schema: ">=2.0.0"
```

## 升级影响分析脚本

配套脚本 `scripts/check-version-compat.py` 可自动分析升级影响：

```bash
# 检查升级影响
python3 scripts/check-version-compat.py --from 1.2.0 --to 2.0.0 --scenario deploy-release

# 输出示例：
# ⚠️  MAJOR impact detected:
#   - Scenario.design-system: Handover YAML 新增字段
#   - 需要同步更新: agents/design-system.agent.md (Handoff 段)
#   - 需要同步更新: prompts/design-system.prompt.md (Output Format)
```

## 相关资产

- [asset-model.md](asset-model.md) - 资产类型与组合公式
- [lifecycle.md](lifecycle.md) - 资产生命周期管理
- [naming-conventions.md](naming-conventions.md) - 命名规范
- [variable-schema-standard.md](variable-schema-standard.md) - 变量 Schema 规范
- [traceability-mapping.md](traceability-mapping.md) - 跨资产可追溯性
