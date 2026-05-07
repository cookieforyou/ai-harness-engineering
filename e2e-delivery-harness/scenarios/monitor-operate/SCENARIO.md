---
name: monitor-operate
description: "监控运维场景，负责系统上线后的监控、告警和运维支持"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Monitor Operate

## Purpose

监控系统运行状态，处理告警和故障，确保系统稳定运行和SLO达成。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成监控运维工作

### Think-Aloud Protocol

```
[THINK] 了解系统基线和SLO
   ↓
[SETUP] 配置监控和告警
   ↓
[WATCH] 监控系统状态
   ↓
[RESPOND] 响应告警和事件
   ↓
[IMPROVE] 优化监控体系
   ↓
[REPORT] 产出运维报告
```

### Step-by-Step Reasoning

**Step 1: 系统理解**
- 问：系统的基线和SLO是什么？
- 验证：与业务确认指标
- 检查：识别核心监控点

**Step 2: 监控配置**
- 问：需要监控哪些指标？
- 验证：覆盖核心路径
- 检查：告警阈值合理

**Step 3: 状态监控**
- 问：系统当前状态如何？
- 验证：指标在正常范围
- 检查：无异常告警

**Step 4: 告警响应**
- 问：告警是否需要处理？
- 验证：判断告警级别
- 检查：按流程响应

**Step 5: 问题诊断**
- 问：问题的根本原因是什么？
- 验证：定位问题根因
- 检查：彻底解决问题

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 监控覆盖 | 核心指标是否全覆盖？ |
| DC-002 | 告警配置 | 告警阈值是否合理？ |
| DC-003 | 响应及时性 | 告警是否及时处理？ |
| DC-004 | 问题解决 | 问题是否彻底解决？ |

## Error Handling

### 告警风暴

| 属性 | 值 |
|------|-----|
| **识别信号** | 大量告警同时触发 |
| **处理方式** | 1. 识别根本告警；2. 抑制次要告警；3. 优先处理核心问题；4. 优化告警规则 |
| **升级条件** | 影响核心服务 |

### 告警误报

| 属性 | 值 |
|------|-----|
| **识别信号** | 告警触发但无实际问题 |
| **处理方式** | 1. 验证告警真伪；2. 调整告警阈值；3. 优化告警条件；4. 减少误报 |
| **升级条件** | 误报率超过20% |

### 服务降级

| 属性 | 值 |
|------|-----|
| **识别信号** | 系统性能下降但未宕机 |
| **处理方式** | 1. 评估影响范围；2. 触发降级预案；3. 通知相关方；4. 持续监控 |
| **升级条件** | SLO 面临违约风险 |




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
| `MTTD` | ≤5min | 平均检测时间：异常发生到告警触发 |
| `ALERT-NOISE` | ≤20% | 告警噪声率：无效告警占比 |
| `SLO-COMPLY` | ≥99.5% | SLO合规率：服务水平目标达成 |

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
✅ 监控系统已配置
✅ 告警规则已设置
✅ 运维手册已编写
✅ 应急预案已准备
✅ SLO 监控面板已就绪
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "operations"
    to_stage: "requirement-analysis"
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
| **Agent** | `../../agents/monitor-operate.agent.md` | 监控运维角色 |
| **Prompt** | `../../prompts/monitor-operate.prompt.md` | 监控运维提示词 |
| **Instruction** | `../../instructions/monitor-operate.instructions.md` | 监控运维技术指令 |
| **Skill** | `../../skills/monitor-operate/SKILL.md` | 监控运维技能 |

## Prerequisites

### 必需前置条件

1. 系统已部署上线
2. 具备监控工具
3. 明确 SLO 指标

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `system_info` | 是 | 系统信息 |
| `slo_targets` | 是 | SLO 目标 |
| `monitoring_tools` | 是 | 监控工具 |
