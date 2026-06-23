---
name: review-design
description: "review design execution prompt for E2E delivery workflow"
type: prompt
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
language: "zh-CN"
tags: ['prompt', 'ai-execution']
---
# Prompt: 技术方案评审场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行技术方案评审工作。

## Input Variables

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**，每完成一步后进行自我验证

```
Step 1: [THINK] 理解任务目标和上下文
   ├─ 输入: 相关输入变量
   ├─ 思考: 任务的核心目标是什么？关键约束有哪些？
   ├─ 验证: 确认理解准确，无遗漏
   └─ 输出: 任务分析摘要
   ↓
Step 2: [ANALYZE] 分析需求和约束条件
   ├─ 输入: 任务分析摘要
   ├─ 思考: 有哪些关键决策点？可能的风险是什么？
   ├─ 验证: 分析全面，考虑了所有重要因素
   └─ 输出: 分析报告
   ↓
Step 3: [DESIGN] 设计解决方案
   ├─ 输入: 分析报告
   ├─ 思考: 最优方案是什么？有无备选方案？
   ├─ 验证: 方案可行且符合最佳实践
   └─ 输出: 设计方案
   ↓
Step 4: [IMPLEMENT] 执行和实施
   ├─ 输入: 设计方案
   ├─ 思考: 如何高质量地实施？需要注意什么？
   ├─ 验证: 实施符合设计规范
   └─ 输出: 实施成果
   ↓
Step 5: [VERIFY] 验证结果和质量
   ├─ 输入: 实施成果
   ├─ 执行: 质量检查和验证
   ├─ 验证: 满足所有验收标准
   └─ 输出: 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段 Agent
```




| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `design_doc` | string | 是 | 设计文档路径 | "design.md" |
| `design_type` | enum | 是 | 设计类型 | ARCHITECTURE/API/DB/FEATURE |
| `reviewer` | string[] | 是 | 评审人 | ["专家A", "专家B"] |
| `review_focus` | string[] | 否 | 评审重点 | ["性能", "安全"] |

## Chain of Thought

```
1. [THINK] 理解需求 → 业务背景和目标？
2. [THINK] 分析方案 → 技术方案完整性？
3. [THINK] 评估风险 → 潜在风险？
4. [THINK] 检查合规 → 符合规范？
5. [VALIDATE] 综合结论 → 评审结论
6. [OUTPUT] 输出报告 → 评审报告
```

## Error Handling

### EH-1: 方案信息不足

```
IF 缺少关键设计信息
THEN
  1. 列出缺失信息
  2. 要求补充
END
```

## Output Validation

### 验证清单

```markdown
## Self-Validation Report

### V-001: 评审完整性
- [ ] 所有评审维度覆盖
- [ ] 评审意见有依据

### V-002: 评审准确性
- [ ] 问题识别准确
- [ ] 建议可行

### 验证结果
- 验证通过: [是/否]
```



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



## Handover 准备

```yaml
handover_to_design_team:
  deliverable: "技术评审报告"
  status: "通过/不通过/有条件通过"

  summary:
    review_items: N
    passed: N
    concerns: N
    risks: N

  concerns:
    - item: "问题"
      severity: "高/中/低"
      suggestion: "建议"

  conclusion: "评审结论"
```

## Constraints

1. **客观公正**: 基于事实评审
2. **建设性**: 提供可行建议
3. **全面性**: 覆盖所有维度

## Task Description

> Describe the specific task for the review-design scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for review-design

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core review-design activities
- Apply best practices and standards

### Phase 3: Validation
- Verify outputs against acceptance criteria
- Ensure completeness and quality



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



## Output Format

```markdown
## Design Review Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Review Report**: Findings organized by category and severity
2. **Action Items**: Required changes with owners and deadlines
3. **Approval Status**: Pass / conditional pass / reject
4. **Risk Assessment**: Design risks and mitigation recommendations
5. **Traceability Check**: Requirements-to-design coverage verification

### Validation Checklist
- [ ] Issue detection rate is 95% or higher
- [ ] Review turnaround is 2 days or less
- [ ] Defect escape rate after review is 5% or lower
- [ ] All findings have clear remediation guidance

### Next Steps
- [ ] Communicate review results to design team
- [ ] Track action items to closure
```

## 相关资产

- [harness-engineering.md](../standards/harness-engineering.md) — 六层驾驭模型对齐标准
- [id-generation-quantification.md](../standards/id-generation-quantification.md) — KPI量化体系与指标定义
- [output-quality-rubric.md](../standards/output-quality-rubric.md) — 输出质量评分与验证标准

