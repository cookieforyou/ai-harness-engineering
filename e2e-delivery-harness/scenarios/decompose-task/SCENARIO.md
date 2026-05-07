---
name: decompose-task
description: "任务拆分场景，负责将需求分解为可执行的技术任务"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Decompose Task

## Purpose

将需求规格说明书分解为可执行、可跟踪的技术任务，为开发团队提供明确的工作项。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成任务拆分工作

### Think-Aloud Protocol

```
[THINK] 分析需求范围
   ↓
[IDENTIFY] 识别任务项
   ↓
[ESTIMATE] 估算工作量和优先级
   ↓
[DEPEND] 分析依赖关系
   ↓
[ASSIGN] 分配任务
   ↓
[VALIDATE] 验证任务分解
```

### Step-by-Step Reasoning

**Step 1: 需求分析**
- 问：需求的范围和边界是什么？
- 验证：与需求规格对照
- 检查：识别核心功能点

**Step 2: 任务识别**
- 问：需要完成哪些技术工作？
- 验证：覆盖所有功能点
- 检查：无遗漏项

**Step 3: 工作量估算**
- 问：每个任务需要多少时间？
- 验证：参考历史数据
- 检查：考虑风险系数

**Step 4: 依赖分析**
- 问：任务间的依赖关系是什么？
- 验证：识别关键路径
- 检查：并行可能性

**Step 5: 任务分配**
- 问：任务如何分配给团队？
- 验证：匹配技能需求
- 检查：负载均衡

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 覆盖完整性 | 是否覆盖所有需求？ |
| DC-002 | 任务粒度 | 任务粒度是否合适？ |
| DC-003 | 依赖清晰 | 依赖关系是否明确？ |
| DC-004 | 优先级合理 | 优先级是否经过共识？ |

## Error Handling

### 任务粒度不当

| 属性 | 值 |
|------|-----|
| **识别信号** | 任务过大或过小 |
| **处理方式** | 1. 评估当前粒度；2. 拆分或合并任务；3. 确保可跟踪；4. 验证粒度合适 |
| **升级条件** | 影响开发效率 |

### 依赖不清晰

| 属性 | 值 |
|------|-----|
| **识别信号** | 任务间依赖关系不明确 |
| **处理方式** | 1. 梳理任务间关系；2. 绘制依赖图；3. 识别阻塞点；4. 调整任务顺序 |
| **升级条件** | 影响开发计划 |

### 估算分歧

| 属性 | 值 |
|------|-----|
| **识别信号** | 团队对估算有分歧 |
| **处理方式** | 1. 讨论估算依据；2. 参考历史数据；3. 使用 Planning Poker；4. 达成共识 |
| **升级条件** | 无法达成共识 |




## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误，无法继续 | 立即停止，升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误，影响核心功能 | 尝试修复，失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误，可降级处理 | 记录并继续，后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息，不影响执行 | 记录并继续 |

### Error Scenario 1: 通用错误处理

**识别信号**: 
- 检测到异常情况
- 验证失败

**处理流程**:
```
IF 检测到错误
THEN
  1. 识别错误类型和严重程度
  2. 记录错误详情
  3. 根据错误级别采取相应措施
  4. IF P0/P1 级别 THEN 升级到人工处理
  5. 更新状态并继续或停止
END
```

**降级方案**: 根据具体情况选择适当的降级策略

**升级条件**: P0 或 P1 级别错误

**错误日志格式**:
```yaml
error_log:
  error_id: "ERR-{timestamp}-XXX"
  timestamp: "{{ISO8601}}"
  level: "P0/P1/P2/P3"
  type: "{错误类型}"
  description: "{详细描述}"
  action_taken: "{已采取的行动}"
  result: "resolved/blocked/degraded/escalated"
```



## Quality Metrics

> Quality metrics for measuring scenario execution success.

| KPI | Target | Description |
|-----|--------|-------------|
| `TASK-CLARITY` | ≥95% | 任务清晰度：满足DoR的任务占比 |
| `EST-ACCURACY` | ±20% | 估算准确度：实际/估算偏差 |
| `DEPENDENCY-COVER` | 100% | 依赖覆盖率：所有跨任务依赖已识别 |

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Timestamp**: `{{execution.started_at}}` — 执行开始时间
- **Agent**: `{{agent.name}}` — 执行Agent标识



## Quality Metrics (质量指标)

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | COMPLETION-RATE | ≥95% | (已完成项/总项数) × 100% | 完成情况检查 | 30% |
| KPI-002 | QUALITY-SCORE | ≥85/100 | 综合质量评分 | 质量评估表 | 30% |
| KPI-003 | COMPLIANCE | 100% | (符合规范项/总检查项) × 100% | 规范检查清单 | 20% |
| KPI-004 | EFFICIENCY | 按时完成 | 实际时间/计划时间 | 时间跟踪 | 20% |

**综合评分计算**: 
```
Quality Score = (KPI-001 × 0.30) + (KPI-002 × 0.30) + (KPI-003 × 0.20) + (KPI-004 × 0.20)
合格: ≥70分 | 优秀: ≥85分 | 卓越: ≥95分
```

### Validation Checklist (验证清单)

**完整性验证 (Completeness)**:
- [ ] 所有必需内容已完成
- [ ] 无遗漏的关键步骤
- [ ] 交付物完整

**一致性验证 (Consistency)**:
- [ ] 术语和命名统一
- [ ] 风格一致
- [ ] 与其他资产协调

**准确性验证 (Accuracy)**:
- [ ] 信息准确无误
- [ ] 数据和计算正确
- [ ] 链接和引用有效

**可执行性验证 (Executability)**:
- [ ] 步骤清晰可执行
- [ ] 资源和要求明确
- [ ] 无模糊或不确定的内容

**规范性验证 (Compliance)**:
- [ ] 遵循标准和规范
- [ ] 符合最佳实践
- [ ] 满足合规要求



## Handover Criteria

```
✅ 任务清单已完成
✅ 工作量已估算
✅ 优先级已排序
✅ 依赖关系已明确
✅ 任务已分配到人
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "task-decomposition"
    to_stage: "development"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    
  artifacts:
    delivered:
      - name: "{{artifact_name}}"
        path: "{{file_path}}"
        version: "{{version}}"
        checksum: "{{SHA256}}"
      
  decisions:
    - id: "DC-XXX"
      description: "{{决策描述}}"
      rationale: "{{决策理由}}"
      alternatives_considered: ["选项1", "选项2"]
      
  open_issues:
    blocking: []
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{{问题描述}}"
        
  risks:
    - id: "RISK-XXX"
      description: "{{风险描述}}"
      probability: "low/medium/high"
      impact: "low/medium/high"
      mitigation: "{{缓解措施}}"
      
  recommendations:
    - "{{建议1}}"
    - "{{建议2}}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{actual_value}}
        target: {{target_value}}
        status: "pass/fail"
```
## Primary Assets

| 资产类型 | 路径 | 说明 |
|----------|------|------|
| **Agent** | `../../agents/decompose-task.agent.md` | 任务分解角色 |
| **Prompt** | `../../prompts/decompose-task.prompt.md` | 任务拆分提示词 |
| **Instruction** | `../../instructions/decompose-task.instructions.md` | 任务拆分技术指令 |
| **Skill** | `../../skills/decompose-task/SKILL.md` | 任务拆分技能 |

## Prerequisites

### 必需前置条件

1. 需求规格说明书已确认
2. 技术方案已确定
3. 团队成员已明确

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `requirements_spec` | 是 | 需求规格说明书 |
| `tech_design` | 是 | 技术设计方案 |
| `team_members` | 是 | 团队成员列表 |
