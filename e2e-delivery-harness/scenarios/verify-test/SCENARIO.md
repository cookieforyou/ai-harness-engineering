---
name: verify-test
description: 测试验证场景，负责设计测试用例、执行测试并报告缺陷
type: scenario
category: quality
stage: testing
version: "1.1.0"
---

# Verify Test

## Purpose

设计并执行测试用例，验证功能实现是否满足需求，发现并跟踪缺陷，确保交付质量。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成测试验证工作

### Think-Aloud Protocol

```
[THINK] 理解测试范围和目标
   ↓
[DESIGN] 设计测试用例
   ↓
[PREPARE] 准备测试环境
   ↓
[EXECUTE] 执行测试用例
   ↓
[REPORT] 报告和跟踪缺陷
   ↓
[VALIDATE] 验证修复结果
```

### Step-by-Step Reasoning

**Step 1: 测试范围理解**
- 问：需要测试哪些功能？
- 验证：与需求规格对照
- 检查：覆盖所有验收标准

**Step 2: 用例设计**
- 问：测试用例是否覆盖所有场景？
- 验证：正向、反向、边界
- 检查：用例可重复执行

**Step 3: 环境准备**
- 问：测试环境是否就绪？
- 验证：数据、配置就位
- 检查：环境与生产一致

**Step 4: 执行测试**
- 问：测试用例是否全部执行？
- 验证：记录执行结果
- 检查：截获测试证据

**Step 5: 缺陷管理**
- 问：发现的缺陷是否清晰记录？
- 验证：缺陷描述完整
- 检查：复现步骤准确

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 用例覆盖 | 是否覆盖所有验收标准？ |
| DC-002 | 环境就绪 | 测试环境是否准备完成？ |
| DC-003 | 执行完成 | 测试用例是否全部执行？ |
| DC-004 | 缺陷确认 | 缺陷是否可复现？ |

## Error Handling

### 测试环境问题

| 属性 | 值 |
|------|-----|
| **识别信号** | 测试环境无法正常工作 |
| **处理方式** | 1. 诊断环境问题；2. 与运维协调；3. 使用替代环境；4. 记录环境限制 |
| **升级条件** | 环境问题超过1天未解决 |

### 测试数据不足

| 属性 | 值 |
|------|-----|
| **识别信号** | 缺少必要的测试数据 |
| **处理方式** | 1. 识别数据需求；2. 请求数据准备；3. 使用模拟数据；4. 标注数据限制 |
| **升级条件** | 影响核心功能测试 |

### 缺陷争议

| 属性 | 值 |
|------|-----|
| **识别信号** | 开发认为不是缺陷 |
| **处理方式** | 1. 引用需求规格；2. 讨论验收标准；3. 寻求产品确认；4. 记录讨论结果 |
| **升级条件** | 无法达成共识超过1轮 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `TEST-PASS` | ≥90% | 测试通过率 |
| `DEFECT-DETECTION` | ≥95% | 缺陷检出率 |
| `REQ-TRACE` | 100% | 需求可追溯性：所有需求有测试覆盖 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 测试用例已设计完成
✅ 测试环境已就绪
✅ 测试用例已全部执行
✅ 缺陷报告已提交
✅ 测试报告已编写
✅ 质量评估已完成
```

### 交付物清单

1. **测试用例**：测试用例集
2. **测试报告**：执行结果和质量评估
3. **缺陷报告**：缺陷列表和状态
4. **测试数据**：测试数据集

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/verify-test.agent.md` | 测试验证角色 |
| **Prompt** | `../../prompts/verify-test.prompt.md` | 测试验证提示词 |
| **Instruction** | `../../instructions/verify-test.instructions.md` | 测试验证技术指令 |
| **Skill** | `../../skills/verify-test/SKILL.md` | 测试验证技能 |

## Prerequisites

### 必需前置条件

1. 功能开发已完成
2. 测试环境已部署
3. 测试数据已准备

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `test_scope` | 是 | 测试范围 |
| `requirements_spec` | 是 | 需求规格说明书 |
| `test_environment` | 是 | 测试环境信息 |
