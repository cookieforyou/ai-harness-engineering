---
name: review-code
description: "review code execution prompt for E2E delivery workflow"
type: execution
version: "1.2.0"
author: AI Harness Engineering Team
created: 2026-04-01
updated: 2026-05-07
status: active
tags: ['prompt', 'ai-execution']
---
# Prompt: 代码审查场景执行 Prompt

## Overview

本 Prompt 用于指导 AI Agent 执行代码审查流程，包括审查准备、问题识别、评审意见生成和质量评估。

## Execution Variables

| 变量名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| `repo_url` | string | 是 | 代码仓库地址 | "https://github.com/org/repo" |
| `branch_name` | string | 是 | 待审查分支 | "feature/new-login" |
| `base_branch` | string | 是 | 基准分支 | "main" |
| `commit_range` | string | 是 | 提交范围 | "abc123..def456" |
| `pr_number` | number | 是 | PR 编号 | 123 |
| `pr_title` | string | 是 | PR 标题 | "实现用户登录功能" |
| `pr_description` | string | 是 | PR 描述 | 包含功能说明和变更范围 |
| `reviewer` | string | 是 | 审查人 | "reviewer_name" |
| `author` | string | 是 | 代码作者 | "author_name" |
| `primary_language` | string | 是 | 主要语言 | "TypeScript" |
| `changed_files` | string[] | 是 | 变更文件列表 | ["src/auth/login.ts", ...] |
| `complexity_level` | enum | 否 | 复杂度等级 | LOW/MEDIUM/HIGH |
| `security_sensitive` | boolean | 否 | 是否涉及安全敏感代码 | true/false |

## Chain of Thought

### Step 1: 变更范围分析

```
输入: changed_files, commit_range
分析:
1. 统计变更文件数量和类型
2. 识别核心变更文件和辅助变更
3. 确定变更所属模块/功能
4. 评估影响边界
```

### Step 2: 多维度审查

```
审查维度:
1. 功能正确性
   - 代码逻辑是否符合需求
   - 边界条件处理是否完整
   - 错误处理是否得当

2. 代码质量
   - 是否遵循编码规范
   - 命名是否清晰准确
   - 函数是否过长需要拆分

3. 性能考虑
   - 是否有性能瓶颈
   - 数据库查询是否优化
   - 是否有不必要的循环

4. 安全审查
   - 输入验证是否完整
   - 是否有注入风险
   - 敏感数据是否脱敏

5. 测试覆盖
   - 单元测试是否充分
   - 边界条件是否有覆盖
   - 集成测试是否完整
```

### Step 3: 问题分级

```
分级标准:
- BLOCKER: 阻塞性问题，必须修复
  * 功能逻辑错误
  * 安全漏洞
  * 严重的性能问题

- MAJOR: 主要问题，建议修复
  * 代码可读性问题
  * 缺少必要的注释
  * 测试覆盖不足

- MINOR: 次要问题，可选修复
  * 编码风格不一致
  * 微小的优化建议
  * 代码格式问题

- COMMENT: 评论建议
  * 讨论性问题
  * 架构建议
  * 经验分享
```

### Step 4: 综合评估

```
评估维度:
1. 代码质量评分 (1-5)
2. 测试覆盖率评估
3. 安全风险评估
4. 建议行动
```

## Error Handling

### 识别信号

| 信号类型 | 检测条件 | 优先级 |
|----------|----------|--------|
| 代码逻辑不清晰 | 超过 3 种理解方式 | HIGH |
| 缺少测试 | 新增代码测试覆盖率 < 70% | HIGH |
| 安全风险 | 检测到潜在安全漏洞模式 | CRITICAL |
| 依赖问题 | 引入高风险依赖 | HIGH |
| 冲突风险 | 与基准分支有潜在冲突 | MEDIUM |

### 处理方式

1. **代码逻辑不清晰**
   - 要求作者添加详细注释
   - 建议重构为更清晰的逻辑
   - 提供具体的改进建议

2. **缺少测试**
   - 列出需要补充的测试场景
   - 提供测试用例模板
   - 标记必须覆盖的关键路径

3. **安全风险检测**
   - 详细描述漏洞原理
   - 提供修复建议
   - 标记为 BLOCKER 级别

### 升级条件

```
CRITICAL 升级条件:
- 发现安全漏洞 (SQL注入、XSS、敏感信息泄露等)
- 功能逻辑严重错误
- 引入已知的依赖漏洞

HIGH 升级条件:
- 代码无法编译或运行
- 缺少关键测试
- 违反团队核心规范
```

## Output Validation

### 必须包含的字段

- [ ] `review_id`: 审查唯一标识符
- [ ] `summary`: 审查总结
- [ ] `files_reviewed`: 已审查文件列表
- [ ] `issues_found`: 问题列表 (含分级)
- [ ] `approval_status`: 审查结论 APPROVED/CHANGES_REQUESTED/REJECTED
- [ ] `quality_score`: 质量评分 (1-5)
- [ ] `action_items`: 行动项列表

### 问题格式

```typescript
interface CodeIssue {
  file: string;           // 文件路径
  line: number;            // 行号
  severity: 'BLOCKER' | 'MAJOR' | 'MINOR' | 'COMMENT';
  category: string;        // 问题类别
  title: string;           // 问题标题
  description: string;     // 详细描述
  suggestion: string;      // 修复建议
  reference?: string;      // 参考资料链接
}
```

### Quality Standards

| 检查项 | 标准 |
|--------|------|
| 问题识别准确率 | ≥ 85% |
| 问题分级准确性 | ≥ 90% |
| 建议可执行性 | 100% |
| 审查完整性 | 覆盖所有变更文件 |



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



## Handover Preparation

```markdown
## Code Review Handover Context

### PR 基础信息
- PR编号: {pr_number}
- 分支: {branch_name} → {base_branch}
- 作者: {author}
- 变更文件数: {file_count}

### 审查结论
- 状态: {approval_status}
- 质量评分: {quality_score}/5
- 问题总数: {issue_count}
  - BLOCKER: {blocker_count}
  - MAJOR: {major_count}
  - MINOR: {minor_count}

### 待处理项
- 必须修复: {must_fix_items}
- 建议修复: {suggested_items}

### Next Steps
- 等待作者修复: {pending_fixes}
- 需要再次审查: {needs_reexamination}
```

## Execution Constraints

1. **客观公正**: 基于代码规范和最佳实践评价，不针对个人
2. **建设性**: 提供具体可行的改进建议
3. **高效**: 优先关注高风险问题
4. **安全优先**: 重点审查安全敏感代码

## Task Description

> Describe the specific task for the review-code scenario execution.
> AI must understand the context, objectives, and success criteria before proceeding.

## Execution Flow

> Step-by-step execution sequence for review-code

### Phase 1: Analysis
- Understand requirements and context
- Identify constraints and dependencies

### Phase 2: Execution
- Perform core review-code activities
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
## Code Review Deliverables

### Summary
- Status: [completed | partial | blocked]
- Completion: [percentage]

### Key Outputs
1. **Review Report**: Categorized findings with severity levels
2. **Defect List**: Issues with location, description, and fix suggestions
3. **Security Findings**: Vulnerability discoveries (if any)
4. **Approval Decision**: Pass / needs changes / reject with rationale
5. **Quality Metrics**: Complexity, duplication, and coverage statistics

### Validation Checklist
- [ ] Defect detection rate is 85% or higher
- [ ] Review turnaround time is 24 hours or less
- [ ] Zero P0/P1 security vulnerabilities are missed
- [ ] Feedback is actionable and specific

### Next Steps
- [ ] Request author to address findings
- [ ] Re-review after fixes are applied
```

