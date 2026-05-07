---
name: {scenario-name}
description: Execution prompt for {scenario-name} scenario
type: execution
version: "1.2.0"
stage: "{stage-name}"
author: AI Harness Engineering Team
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
status: active
tags: [<tag1>, <tag2>]
---

# {Scenario Title} - Execution Prompt

> **版本**: {version} | **适用阶段**: {stage} | **预计工时**: {estimated_time}
> 
> **重要**: 此 Prompt 为 AI 执行的完整脚本,必须严格按照以下步骤执行

## Task Description

{清晰描述此场景的具体任务目标,包括:
- 要解决的核心问题
- 期望达成的业务目标
- 成功的关键标准
}

## Input Variables (变量定义)

> **AI 在执行前必须确认以下变量已填充**,如未填充则请求用户提供

| Variable | Type | Required | Default | Description | Validation |
|----------|------|----------|---------|-------------|------------|
| `var_name` | string | true | - | {变量描述} | {验证规则} |
| `var_name` | number | false | 0 | {变量描述} | {验证规则} |
| `var_name` | array | true | [] | {变量描述} | {验证规则} |
| `var_name` | enum | true | - | {选项A\|选项B\|选项C} | {验证规则} |

### Variable Examples

```yaml
# 示例: 展示变量的正确格式
var_name: "example value"
var_number: 42
var_array:
  - item1
  - item2
var_enum: "option_a"
```

## Chain of Thought (思维链)

> **AI 必须按照以下思维链逐步执行**,每完成一步后进行自我验证

```
Step 1: [THINK] 理解目标和上下文
   ├─ 输入: {需要的输入}
   ├─ 思考: {关键问题}
   ├─ 验证: {如何验证理解正确}
   └─ 输出: {中间产物}
   ↓
Step 2: [ANALYZE] 分析和分解
   ├─ 输入: {上一步输出}
   ├─ 思考: {关键问题}
   ├─ 验证: {如何验证分析正确}
   └─ 输出: {中间产物}
   ↓
Step 3: [DESIGN] 设计方案
   ├─ 输入: {上一步输出}
   ├─ 思考: {关键问题}
   ├─ 验证: {如何验证设计合理}
   └─ 输出: {中间产物}
   ↓
Step 4: [IMPLEMENT] 执行实现
   ├─ 输入: {上一步输出}
   ├─ 思考: {关键问题}
   ├─ 验证: {如何验证实现正确}
   └─ 输出: {中间产物}
   ↓
Step 5: [VERIFY] 验证输出
   ├─ 输入: {上一步输出}
   ├─ 执行: Output Validation Checklist
   ├─ 验证: 所有检查项通过
   └─ 输出: 最终交付物 + 验证报告
   ↓
Step 6: [HANDOVER] 准备交接
   ├─ 生成: Handover Context
   ├─ 更新: Global Context
   └─ 通知: 下一阶段
```

## Execution Flow (执行流程)

### Phase 1: Preparation (准备阶段)

**目标**: {此阶段的目标}

**步骤**:
1. {步骤1描述}
   - 操作: {具体操作}
   - 验证: {如何验证}
2. {步骤2描述}
   - 操作: {具体操作}
   - 验证: {如何验证}

**产出**: {此阶段的产出}

### Phase 2: Analysis (分析阶段)

**目标**: {此阶段的目标}

**步骤**:
1. {步骤1描述}
   - 操作: {具体操作}
   - 验证: {如何验证}
2. {步骤2描述}
   - 操作: {具体操作}
   - 验证: {如何验证}

**产出**: {此阶段的产出}

### Phase 3: Execution (执行阶段)

**目标**: {此阶段的目标}

**步骤**:
1. {步骤1描述}
   - 操作: {具体操作}
   - 验证: {如何验证}
2. {步骤2描述}
   - 操作: {具体操作}
   - 验证: {如何验证}

**产出**: {此阶段的产出}

### Phase 4: Validation (验证阶段)

**目标**: 验证所有产出符合质量标准

**步骤**:
1. 执行 Output Validation Checklist
2. 记录验证结果
3. 处理未通过的检查项

**产出**: 验证报告

## Output Format (输出格式)

> **AI 必须严格遵循以下输出格式**,不得随意更改结构

```markdown
# {Scenario Name} - Deliverables

## Executive Summary

- **Status**: [completed | partial | blocked]
- **Completion**: {percentage}%
- **Quality Score**: {score}/100
- **Duration**: {execution_time}
- **Key Findings**: {关键发现摘要}

## Detailed Outputs

### 1. {交付物1名称}

{交付物1的详细内容}

### 2. {交付物2名称}

{交付物2的详细内容}

### 3. {交付物3名称}

{交付物3的详细内容}

## Validation Report

### V-001: Completeness Check
- [ ] Item 1: [PASS/FAIL] - {说明}
- [ ] Item 2: [PASS/FAIL] - {说明}
- Overall: [PASS/FAIL]

### V-002: Consistency Check
- [ ] Item 1: [PASS/FAIL] - {说明}
- [ ] Item 2: [PASS/FAIL] - {说明}
- Overall: [PASS/FAIL]

### V-003: Accuracy Check
- [ ] Item 1: [PASS/FAIL] - {说明}
- [ ] Item 2: [PASS/FAIL] - {说明}
- Overall: [PASS/FAIL]

### Validation Summary
- Total Checks: {number}
- Passed: {number}
- Failed: {number}
- Status: [PASS/FAIL]

## Decision Log

| ID | Decision | Rationale | Alternatives Considered |
|----|----------|-----------|------------------------|
| DC-001 | {决策} | {理由} | {备选方案} |

## Issues & Risks

### Open Issues
- **ISSUE-001**: {问题描述}
  - Impact: {影响}
  - Action Required: {需要的行动}

### Identified Risks
- **RISK-001**: {风险描述}
  - Probability: [High/Medium/Low]
  - Impact: [High/Medium/Low]
  - Mitigation: {缓解措施}

## Next Steps

1. {建议的下一步行动1}
2. {建议的下一步行动2}
3. {建议的下一步行动3}

## Handover Context

```yaml
handover:
  from_stage: "{current_stage}"
  to_stage: "{next_stage}"
  status: "completed/partial/blocked"
  artifacts:
    - name: "{artifact_name}"
      path: "{file_path}"
  open_issues: []
  recommendations: []
```
```

## Error Handling (错误处理)

> **AI 遇到以下情况时必须按指定流程处理**

### Error Classification

| Level | Code | Description | Action |
|-------|------|-------------|--------|
| P0 - Critical | ERR-CRITICAL | 阻塞性错误,无法继续 | 立即停止,升级人工 |
| P1 - Major | ERR-MAJOR | 严重错误,影响核心功能 | 尝试修复,失败则升级 |
| P2 - Minor | ERR-MINOR | 一般错误,可降级处理 | 记录并继续 |
| P3 - Warning | ERR-WARNING | 警告信息,不影响执行 | 记录并继续 |

### Error Scenario 1: {错误场景名称}

**识别信号**: {明确的触发条件}

**处理流程**:
```
IF {触发条件}
THEN
  1. {处理步骤1}
  2. {处理步骤2}
  3. {处理步骤3}
  4. IF 处理失败 THEN 升级到人工
END
```

**降级方案**: {如果自动处理失败的备选方案}

**升级条件**: {什么情况下需要人工介入}

### Error Scenario 2: {错误场景名称}

**识别信号**: {明确的触发条件}

**处理流程**:
```
IF {触发条件}
THEN
  1. {处理步骤1}
  2. {处理步骤2}
  3. {处理步骤3}
  4. IF 处理失败 THEN 升级到人工
END
```

**降级方案**: {如果自动处理失败的备选方案}

**升级条件**: {什么情况下需要人工介入}

### Error Logging

每次遇到错误必须记录:
```yaml
error_log:
  - error_id: "ERR-{timestamp}-{sequence}"
    timestamp: "{{ISO8601}}"
    level: "P0/P1/P2/P3"
    type: "{错误类型}"
    description: "{详细描述}"
    action_taken: "{采取的行动}"
    result: "resolved/unresolved/escalated"
```

## Output Validation (输出验证)

> **在生成最终输出前,AI 必须完成以下验证步骤**

### Mandatory Validation Checklist

**V-001: Completeness Validation**
- [ ] All required sections are present
- [ ] All variables have been filled
- [ ] All deliverables have been generated
- [ ] No placeholder text remains (e.g., {TODO}, [placeholder])

**V-002: Consistency Validation**
- [ ] Terminology is consistent throughout
- [ ] Data values match across sections
- [ ] No contradictory statements
- [ ] References point to existing assets

**V-003: Accuracy Validation**
- [ ] All calculations are correct
- [ ] All facts are verified
- [ ] All assumptions are documented
- [ ] Standards and best practices followed

**V-004: Quality Validation**
- [ ] Output meets defined KPIs
- [ ] Formatting follows specifications
- [ ] Language is clear and professional
- [ ] Structure is logical and readable

### Validation Failure Protocol

```
IF any validation check fails
THEN
  1. Document the failed check and reason
  2. Assess severity (P0/P1/P2/P3)
  3. For P0/P1: MUST fix before proceeding
  4. For P2/P3: Can document as known issue with justification
  5. Re-run validation until all checks pass or are accepted
  6. Record final validation status
END
```

### Self-Assessment

AI must provide a self-assessment:
- Confidence Level: [High/Medium/Low]
- Areas of Uncertainty: {list any uncertainties}
- Recommendations for Human Review: {what needs human attention}

## Constraints & Requirements (约束与要求)

### Mandatory Constraints

1. **Language**: {输出语言要求,如: 中文}
2. **Format**: {格式要求,如: Markdown}
3. **Length**: {长度限制,如: 不超过5000字}
4. **Style**: {风格要求,如: 专业、简洁}
5. **Standards**: {需遵循的标准,如: ISO/IEC 25010}

### Quality Requirements

| Requirement | Standard | Verification Method |
|-------------|----------|--------------------|
| {要求1} | {标准} | {验证方法} |
| {要求2} | {标准} | {验证方法} |
| {要求3} | {标准} | {验证方法} |

### Performance Expectations

- **Execution Time**: {预期执行时间}
- **Resource Usage**: {资源使用限制}
- **Accuracy Target**: {准确性目标}

## Examples (示例)

### Example 1: {示例场景}

**Input**:
```yaml
{示例输入}
```

**Expected Output**:
```markdown
{期望输出}
```

**Key Learnings**:
- {关键学习点1}
- {关键学习点2}

## Tone and Style Guidelines

- **Tone**: {语气要求,如: Professional, objective}
- **Voice**: {语态要求,如: Active voice preferred}
- **Terminology**: {术语使用规范}
- **Formatting**: {格式化规范,如: Use tables for structured data}

## References

- Related Scenario: [link to scenario]
- Related Skill: [link to skill]
- Related Instruction: [link to instruction]
- Standards: [link to standards]

---

**Prompt Version**: {version}  
**Last Updated**: {date}  
**Author**: AI Harness Engineering Team
