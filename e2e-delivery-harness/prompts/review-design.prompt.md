---
name: review-design
description: review design execution prompt for E2E delivery workflow
type: execution
version: "1.1.0"
stage: review-design
---

# Prompt: 技术方案评审场景执行 Prompt

## 概述

本 Prompt 用于指导 AI Agent 执行技术方案评审工作。

## Input Variables

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
## 自我验证报告

### V-001: 评审完整性
- [ ] 所有评审维度覆盖
- [ ] 评审意见有依据

### V-002: 评审准确性
- [ ] 问题识别准确
- [ ] 建议可行

### 验证结果
- 验证通过: [是/否]
```

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

## Output Format

> Standard output structure for review-design deliverables


