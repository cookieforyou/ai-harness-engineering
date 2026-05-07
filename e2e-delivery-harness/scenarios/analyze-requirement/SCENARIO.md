---
name: analyze-requirement
description: "需求分析场景，负责将原始业务需求转换为结构化的需求规格说明书"
type: scenario
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['workflow', 'process']
---
# Analyze Requirement

## Purpose

将原始业务需求转换为结构化的需求规格说明书，确保需求的完整性、一致性和可追溯性。

## Chain of Thought

> AI 执行时的思维引导，帮助逐步完成需求分析工作

### Think-Aloud Protocol

```
[THINK] 理解业务背景和目标
   ↓
[ANALYZE] 识别干系人和诉求
   ↓
[GATHER] 收集和整理需求
   ↓
[MODEL] 构建业务模型
   ↓
[SPECIFY] 编写需求规格
   ↓
[VALIDATE] 与干系人确认
```

### Step-by-Step Reasoning

**Step 1: 业务理解**
- 问：业务背景和核心目标是什么？
- 验证：与业务方确认理解
- 检查：是否了解行业背景和约束

**Step 2: 干系人分析**
- 问：谁是主要干系人？他们各自的诉求是什么？
- 验证：列出干系人矩阵
- 检查：是否覆盖所有关键干系人

**Step 3: 需求收集**
- 问：收集到的需求是否完整？
- 验证：需求覆盖业务场景
- 检查：功能需求与非功能需求

**Step 4: 业务建模**
- 问：业务流程是否清晰？
- 验证：绘制业务流程图
- 检查：识别关键路径和分支

**Step 5: 需求规格化**
- 问：需求是否SMART？
- 验证：每条需求可测试
- 检查：需求可追溯到业务目标

## Decision Checkpoints

| 检查点 | 条件 | 决策 |
|--------|------|------|
| DC-001 | 干系人确认 | 是否与所有关键干系人确认需求？ |
| DC-002 | 需求完整性 | 是否覆盖所有业务场景？ |
| DC-003 | 需求可测试性 | 每条需求是否有验收标准？ |
| DC-004 | 优先级排序 | 需求优先级是否经过共识？ |

## Error Handling

### 需求模糊

| 属性 | 值 |
|------|-----|
| **识别信号** | 需求描述含糊不清，存在多种理解 |
| **处理方式** | 1. 列出所有可能的理解；2. 与业务方澄清；3. 选择最合理理解；4. 记录决策依据 |
| **升级条件** | 业务方无法澄清超过3次 |

### 干系人冲突

| 属性 | 值 |
|------|-----|
| **识别信号** | 不同干系人对同一需求有矛盾要求 |
| **处理方式** | 1. 识别冲突点；2. 分析各方诉求；3. 提出折中方案；4. 高层拍板 |
| **升级条件** | 无法达成共识超过2轮 |

### 需求蔓延

| 属性 | 值 |
|------|-----|
| **识别信号** | 需求范围不断扩大，超出原定边界 |
| **处理方式** | 1. 标记新增需求；2. 评估影响；3. 与产品负责人确认；4. 调整范围或延期 |
| **升级条件** | 影响超过20%原定范围 |




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
| `REQ-COVER` | ≥95% | 需求覆盖率：已分析需求占总需求比例 |
| `STAKEHOLDER-ID` | 100% | 干系人识别率：关键干系人全部识别 |
| `AC-CLARITY` | ≥90% | 验收标准清晰度：可量化验收标准占比 |

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
✅ 需求规格说明书已完成
✅ 干系人分析报告已输出
✅ 业务流程图已绘制
✅ 用例模型已构建
✅ 需求已评审通过
✅ 所有疑问已澄清
```

### Handover Context Template

```yaml
handover:
  header:
    from_stage: "requirement-analysis"
    to_stage: "system-design"
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
| **Agent** | `../../agents/analyze-requirement.agent.md` | 需求分析角色 |
| **Prompt** | `../../prompts/analyze-requirement.prompt.md` | 需求分析提示词 |
| **Instruction** | `../../instructions/analyze-requirement.instructions.md` | 需求分析技术指令 |
| **Skill** | `../../skills/analyze-requirement/SKILL.md` | 需求分析技能 |

## Prerequisites

### 必需前置条件

1. 业务方提出需求请求
2. 具备项目背景信息
3. 可联系到关键干系人

### 期望输入

| 输入项 | 必填 | 描述 |
|--------|------|------|
| `project_name` | 是 | 项目名称 |
| `raw_requirements` | 是 | 原始需求描述 |
| `stakeholders` | 否 | 已知干系人列表 |
| `business_context` | 否 | 业务背景信息 |
