---
name: deploy-release
description: 部署发布场景，负责将软件部署到目标环境并完成发布
type: scenario
category: operations
stage: deployment
version: "1.1.0"
---

# Deploy Release

## Purpose

将软件部署到目标环境，执行发布流程，确保部署成功并建立回滚机制。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成部署发布工作

### Think-Aloud Protocol

```
[THINK] 确认发布范围和计划
   ↓
[PREPARE] 准备部署环境
   ↓
[DEPLOY] 执行部署操作
   ↓
[VERIFY] 验证部署结果
   ↓
[MONITOR] 监控发布后状态
   ↓
[COMPLETE] 完成发布确认
```

### Step-by-Step Reasoning

**Step 1: 发布确认**
- 问：发布范围和计划是什么？
- 验证：与产品确认
- 检查：回滚计划就绪

**Step 2: 环境准备**
- 问：目标环境是否就绪？
- 验证：检查依赖服务
- 检查：资源配置充足

**Step 3: 执行部署**
- 问：部署步骤是否正确？
- 验证：按检查清单执行
- 检查：记录每个步骤

**Step 4: 结果验证**
- 问：部署是否成功？
- 验证：功能验证通过
- 检查：无错误告警

**Step 5: 状态监控**
- 问：系统运行是否正常？
- 验证：监控指标正常
- 检查：错误率无异常

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 发布确认 | 是否获得发布授权？ |
| DC-002 | 环境就绪 | 目标环境是否准备完成？ |
| DC-003 | 回滚就绪 | 回滚方案是否就绪？ |
| DC-004 | 验证通过 | 部署验证是否通过？ |

## Error Handling

### 部署失败

| 属性 | 值 |
|------|-----|
| **识别信号** | 部署过程出现错误 |
| **处理方式** | 1. 分析错误原因；2. 尝试修复；3. 如无法修复，执行回滚；4. 记录失败原因 |
| **升级条件** | 需要回滚 |

### 验证不通过

| 属性 | 值 |
|------|-----|
| **识别信号** | 部署后功能验证失败 |
| **处理方式** | 1. 定位问题原因；2. 评估影响范围；3. 修复或回滚；4. 重新验证 |
| **升级条件** | 核心功能异常 |

### 性能下降

| 属性 | 值 |
|------|-----|
| **识别信号** | 发布后性能指标异常 |
| **处理方式** | 1. 评估性能影响；2. 分析原因；3. 优化或回滚；4. 持续监控 |
| **升级条件** | SLA 面临违约风险 |


## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `DEPLOY-SUCCESS` | ≥99% | 部署成功率 |
| `ROLLBACK-TIME` | ≤15min | 回滚时间：触发回滚到恢复服务 |
| `ZERO-DOWNTIME` | 100% | 零停机达成：生产环境无感知切换 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识

## Handover Criteria

```
✅ 部署清单已执行完成
✅ 功能验证已通过
✅ 监控告警已配置
✅ 回滚方案已就绪
✅ 发布记录已存档
```

### 交付物清单

1. **部署包**：发布版本
2. **部署记录**：部署过程日志
3. **回滚方案**：回滚脚本和步骤
4. **发布报告**：发布总结

## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/deploy-release.agent.md` | 部署发布角色 |
| **Prompt** | `../../prompts/deploy-release.prompt.md` | 部署发布提示词 |
| **Instruction** | `../../instructions/deploy-release.instructions.md` | 部署发布技术指令 |
| **Skill** | `../../skills/deploy-release/SKILL.md` | 部署发布技能 |

## Prerequisites

### 必需前置条件

1. 测试验证已通过
2. 部署环境已准备
3. 发布计划已确认

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `release_version` | 是 | 发布版本号 |
| `release_scope` | 是 | 发布范围 |
| `target_environment` | 是 | 目标环境 |
| `rollback_plan` | 否 | 回滚方案 |
