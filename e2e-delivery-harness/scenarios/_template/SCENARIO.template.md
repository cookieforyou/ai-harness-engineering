---
name: <scenario-name>
type: scenario
version: "1.2.0"
description: <scenario-description>
category: <category>
stage: <stage-name>
author: AI Harness Engineering Team
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
status: active
tags: [<tag1>, <tag2>]
---

# {scenario-name}

## Purpose

{场景目标描述，1-3句话说明此场景的核心目标}

## Chain of Thought

> **AI 执行时的强制性思维引导**,确保逐步完成场景工作并自我验证

### Think-Aloud Protocol (强制遵循)

```
[THINK] Step 1: <理解目标和上下文>
   ├─ 问：<关键自问1>？
   ├─ 验证：<验证方式1>
   └─ 检查：<检查点1>
   ↓
[ANALYZE] Step 2: <分析和分解>
   ├─ 问：<关键自问2>？
   ├─ 验证：<验证方式2>
   └─ 检查：<检查点2>
   ↓
[DESIGN] Step 3: <设计方案>
   ├─ 问：<关键自问3>？
   ├─ 验证：<验证方式3>
   └─ 检查：<检查点3>
   ↓
[IMPLEMENT] Step 4: <执行实现>
   ├─ 问：<关键自问4>？
   ├─ 验证：<验证方式4>
   └─ 检查：<检查点4>
   ↓
[VERIFY] Step 5: <验证输出>
   ├─ 问：输出是否符合质量标准？
   ├─ 验证：执行 Output Validation
   └─ 检查：所有交付物完整且达标
   ↓
[HANDOVER] Step 6: <准备交接>
   ├─ 生成 Handover Context
   ├─ 更新 Global Context
   └─ 通知下一阶段
```

### Step-by-Step Reasoning (详细推理)

**Step 1: {子步骤名称}**
- **目标**: {该步骤要达成的具体目标}
- **思考**: 
  - 问：{自问1}？
  - 问：{自问2}？
- **验证**: {如何验证此步骤正确完成}
- **检查点**: 
  - [ ] {检查项1}
  - [ ] {检查项2}
- **产出**: {此步骤的中间产物}

**Step 2: {子步骤名称}**
- **目标**: {该步骤要达成的具体目标}
- **思考**: 
  - 问：{自问1}？
  - 问：{自问2}？
- **验证**: {如何验证此步骤正确完成}
- **检查点**: 
  - [ ] {检查项1}
  - [ ] {检查项2}
- **产出**: {此步骤的中间产物}

**Step 3: {子步骤名称}**
- **目标**: {该步骤要达成的具体目标}
- **思考**: 
  - 问：{自问1}？
  - 问：{自问2}？
- **验证**: {如何验证此步骤正确完成}
- **检查点**: 
  - [ ] {检查项1}
  - [ ] {检查项2}
- **产出**: {此步骤的中间产物}

## Decision Checkpoints

> **执行过程中必须确认的关键决策点**,每个决策点都需要明确记录

| ID | 决策点 | 触发条件 | 决策选项 | 选择标准 | 记录位置 |
|----|--------|----------|----------|----------|----------|
| DC-001 | {决策名称} | {条件描述} | {选项A}/{选项B} | {选择依据} | {记录在哪个文档} |
| DC-002 | {决策名称} | {条件描述} | {选项A}/{选项B}/{选项C} | {选择依据} | {记录在哪个文档} |
| DC-003 | {决策名称} | {条件描述} | {是}/{否} | {判断标准} | {记录在哪个文档} |

**决策记录要求**:
- 每个决策必须记录：决策时间、决策人(或AI)、选择理由、备选方案评估
- 重大决策需要干系人确认
- 决策变更必须记录变更原因和影响分析

## Error Handling

> **遇到异常情况时的标准化处理流程**,AI 必须严格按照此流程执行

### 错误分类体系

| 级别 | 标识 | 描述 | 处理方式 |
|------|------|------|----------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误,无法继续执行 | 立即停止,升级人工处理 |
| P1 - Major | ERR-MAJOR | 严重错误,影响核心功能 | 尝试修复,失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误,可降级处理 | 记录并继续,后续修复 |
| P3 - Warning | ERR-WARNING | 警告信息,不影响执行 | 记录并继续 |

### 错误类型 1：{错误名称}

| 属性 | 值 |
|------|-----|
| **错误级别** | P0/P1/P2/P3 |
| **识别信号** | {明确的触发条件或异常表现} |
| **根本原因** | {可能的原因列表} |
| **自动处理** | 1. {步骤1}<br>2. {步骤2}<br>3. {步骤3} |
| **降级方案** | {如果自动处理失败的备选方案} |
| **升级条件** | {什么情况下需要人工介入} |
| **升级对象** | {应该联系谁} |
| **恢复验证** | {如何验证问题已解决} |

### 错误类型 2：{错误名称}

| 属性 | 值 |
|------|-----|
| **错误级别** | P0/P1/P2/P3 |
| **识别信号** | {明确的触发条件或异常表现} |
| **根本原因** | {可能的原因列表} |
| **自动处理** | 1. {步骤1}<br>2. {步骤2}<br>3. {步骤3} |
| **降级方案** | {如果自动处理失败的备选方案} |
| **升级条件** | {什么情况下需要人工介入} |
| **升级对象** | {应该联系谁} |
| **恢复验证** | {如何验证问题已解决} |

### 错误日志要求

```yaml
error_log:
  - error_id: "ERR-{timestamp}-{sequence}"
    timestamp: "{{ISO8601}}"
    level: "P0/P1/P2/P3"
    type: "{错误类型}"
    description: "{详细描述}"
    context: "{发生时的上下文}"
    action_taken: "{采取的行动}"
    result: "{处理结果}"
    escalated: true/false
    resolved: true/false
```

## Quality Metrics & Validation

> **量化的质量评估标准和自动化验证机制**

### Key Performance Indicators (KPIs)

| KPI ID | 指标名称 | 目标值 | 计算公式 | 验证方法 | 权重 |
|--------|----------|--------|----------|----------|------|
| KPI-001 | {指标名称} | ≥{目标值}% | {计算方式} | {如何测量} | {权重}% |
| KPI-002 | {指标名称} | ≤{目标值} | {计算方式} | {如何测量} | {权重}% |
| KPI-003 | {指标名称} | ={目标值} | {计算方式} | {如何测量} | {权重}% |

**综合评分计算**:
```
Score = Σ(KPI_i × Weight_i) / ΣWeight_i
合格线: ≥80分
优秀线: ≥90分
卓越线: ≥95分
```

### Output Validation Checklist (强制验证)

**V-001: 完整性验证**
- [ ] 所有必需交付物已生成
- [ ] 所有章节/字段已填充(无空白)
- [ ] 引用的资产都存在且可访问
- [ ] 前置条件都已满足

**V-002: 一致性验证**
- [ ] 术语使用一致(对照术语表)
- [ ] 数据在各处保持一致
- [ ] 逻辑无矛盾
- [ ] 与上游阶段的输出一致

**V-003: 准确性验证**
- [ ] 数据和事实准确无误
- [ ] 计算和推导正确
- [ ] 引用来源可靠
- [ ] 符合行业标准和最佳实践

**V-004: 可执行性验证**
- [ ] 方案可落地实施
- [ ] 资源需求合理
- [ ] 时间估算可行
- [ ] 风险可控

**V-005: 规范性验证**
- [ ] 符合命名规范
- [ ] 符合格式规范
- [ ] 符合编码/文档规范
- [ ] 元数据完整准确

### Validation Failure Handling

```
IF 任何验证项未通过
THEN
  1. 记录未通过的验证项及原因
  2. 评估影响程度(P0/P1/P2/P3)
  3. P0/P1: 必须修复后才能继续
  4. P2/P3: 可记录为已知问题,但需在Handover中说明
  5. 重新执行验证直到全部通过或确认可接受
END
```

### Traceability

- **Trace ID**: `{{execution.trace_id}}` — 唯一标识本次场景执行
- **Execution ID**: `{{execution.id}}` — 执行实例标识
- **Started At**: `{{execution.started_at}}` — ISO8601格式开始时间
- **Completed At**: `{{execution.completed_at}}` — ISO8601格式完成时间
- **Agent**: `{{agent.name}}` — 执行Agent标识
- **Version**: `{{asset.version}}` — 使用的资产版本

## Handover Criteria & Context

> **阶段完成的严格验收标准和标准化交接流程**

### Mandatory Acceptance Criteria (必须全部满足)

```
✅ AC-001: {验收标准1} - [已验证/未验证]
✅ AC-002: {验收标准2} - [已验证/未验证]
✅ AC-003: {验收标准3} - [已验证/未验证]
✅ AC-004: 所有 Quality Validation 检查项通过 - [是/否]
✅ AC-005: 所有 Decision Checkpoints 已记录 - [是/否]
✅ AC-006: 所有 Errors 已处理或记录 - [是/否]
```

### Deliverables Checklist

| ID | 交付物名称 | 格式 | 必填 | 验证标准 | 状态 |
|----|------------|------|------|----------|------|
| DEL-001 | {交付物1} | .md/.json/.yaml | 是 | {验证方式} | ☐ |
| DEL-002 | {交付物2} | .md/.json/.yaml | 是 | {验证方式} | ☐ |
| DEL-003 | {交付物3} | .md/.json/.yaml | 否 | {验证方式} | ☐ |

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "{{current_stage}}"
    to_stage: "{{next_stage}}"
    handover_id: "HO-{{timestamp}}-{{sequence}}"
    timestamp: "{{ISO8601}}"
    prepared_by: "{{agent.name}}"
    
  summary:
    status: "completed/partial/blocked"
    completion_percentage: {{0-100}}
    quality_score: {{0-100}}
    total_duration: "{{duration}}"
    
  artifacts:
    delivered:
      - name: "{交付物名称}"
        path: "{文件路径}"
        version: "{版本}"
        checksum: "{MD5/SHA256}"
      
  decisions:
    - id: "DC-XXX"
      description: "{决策描述}"
      rationale: "{决策理由}"
      alternatives_considered: ["{备选方案}"]
      
  open_issues:
    blocking:
      - id: "ISSUE-XXX"
        description: "{问题描述}"
        impact: "{影响分析}"
        required_action: "{需要的行动}"
    non_blocking:
      - id: "ISSUE-XXX"
        description: "{问题描述}"
        planned_resolution: "{计划解决方案}"
        
  risks:
    - id: "RISK-XXX"
      description: "{风险描述}"
      probability: "high/medium/low"
      impact: "high/medium/low"
      mitigation: "{缓解措施}"
      
  recommendations:
    - "{给下一阶段的建议1}"
    - "{给下一阶段的建议2}"
    
  quality_metrics:
    kpi_results:
      - kpi_id: "KPI-001"
        value: {{实际值}}
        target: {{目标值}}
        status: "pass/fail"
```

### Next Stage Notification

完成 Handover Context 后,必须:
1. 更新 Global Context 中的阶段状态
2. 通知下一阶段的负责人(Agent或人工)
3. 归档当前阶段的所有工作产物
4. 记录阶段完成时间戳
